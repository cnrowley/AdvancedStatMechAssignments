import numpy as np
import mdtraj as md
from itertools import combinations

def best_hummer_q(traj, native):
    """Compute the fraction of native contacts according the definition from
    Best, Hummer and Eaton [1]
    
    Parameters
    ----------
    traj : md.Trajectory
        The trajectory to do the computation for
    native : md.Trajectory
        The 'native state'. This can be an entire trajecory, or just a single frame.
        Only the first conformation is used
        
    Returns
    -------
    q : np.array, shape=(len(traj),)
        The fraction of native contacts in each frame of `traj`
        
    References
    ----------
    ..[1] Best, Hummer, and Eaton, "Native contacts determine protein folding
          mechanisms in atomistic simulations" PNAS (2013)
    """
    
    BETA_CONST = 50  # 1/nm
    LAMBDA_CONST = 1.8
    NATIVE_CUTOFF = 0.45  # nanometers
    
    # get the indices of all of the heavy atoms
    heavy = native.topology.select_atom_indices('heavy')
    # get the pairs of heavy atoms which are farther than 3
    # residues apart
    heavy_pairs = np.array(
        [(i,j) for (i,j) in combinations(heavy, 2)
            if abs(native.topology.atom(i).residue.index - \
                   native.topology.atom(j).residue.index) > 3])
    
    # compute the distances between these pairs in the native state
    heavy_pairs_distances = md.compute_distances(native[0], heavy_pairs)[0]

    # and get the pairs s.t. the distance is less than NATIVE_CUTOFF
    native_contacts = heavy_pairs[heavy_pairs_distances < NATIVE_CUTOFF]
    
    # now compute these distances for the whole trajectory
    r = md.compute_distances(traj, native_contacts)
    # and recompute them for just the native state
    r0 = md.compute_distances(native[0], native_contacts)
    
    q = np.mean(1.0 / (1 + np.exp(BETA_CONST * (r - LAMBDA_CONST * r0))), axis=1)
    return q

trajectory = md.load('mdcrd.netcdf', top='protein_hmr.prmtop')
trajectory_nosolv=trajectory.remove_solvent()
sasa = md.shrake_rupley(trajectory_nosolv)
total_sasa = sasa.sum(axis=1)

# calculate radius 
rg=md.compute_rg(trajectory_nosolv)

# read experimental NMR structure

exptl=md.load('exptl.pdb')

heavy_atoms = [atom.index for atom in trajectory_nosolv.topology.atoms if atom.element.symbol != 'H' and not atom.residue.is_water]

print(heavy_atoms)

trajectory_nosolv.superpose(exptl, atom_indices=heavy_atoms)
trajectory_nosolv.save_pdb("traj.pdb")

# calculate rmsd of trajectory relative to NMR structure (heavy atoms only)

heavy_rmds_to_exptl = md.rmsd(trajectory_nosolv, exptl, 0, atom_indices=heavy_atoms)

# calculate DSSP secondary structures for trajectory
ss=md.compute_dssp(trajectory_nosolv, simplified=True)

beta_percent=[]

hbonds=[]

for (i, s) in enumerate(ss):
    hbonds.append(md.baker_hubbard(trajectory_nosolv[i], periodic=False))

    count=0
    beta=0

    for e in s:
        if(e=='E'):
            beta=beta+1
        count=count+1
    beta_percent.append(float(beta)/count)
    
h_traj=[]

for h in hbonds:
    h_traj.append(len(h))

q = best_hummer_q(trajectory_nosolv, exptl)

fhout=open('mdtraj.txt', 'w')

for i, (h, s, contacts, rmsd, beta, g) in enumerate(zip(h_traj, total_sasa, q, heavy_rmds_to_exptl, beta_percent, rg)):
    fhout.write(str(i) + ',' + str(h) + ',' + str(s) + ',' +
                str(contacts) +  ',' + str(rmsd) + ',' + str(beta) + ',' + str(g)+ '\n')

fhout.close()


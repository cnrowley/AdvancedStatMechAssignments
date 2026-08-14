"""Compute the molecular feature set used by the ml_classifier models from a raw SMILES string.

The training CSVs (positive_training.csv, negative_training.csv, testset.csv) ship with these
descriptors already computed; the script that originally generated them is not part of this
repository. This module reconstructs each feature from RDKit so that predict.py can score a new
SMILES string against a saved model. Two features (contains_isoprene_subunit and
contains_glycosylation) are not standard RDKit descriptors and have no unambiguous definition, so
they are implemented here as substructure-match heuristics (see the SMARTS patterns below) rather
than reproductions of the original (unavailable) code -- treat those two columns as approximate.
"""

from rdkit import Chem
from rdkit.Chem import Descriptors

# All RDKit fragment-count descriptors (fr_*) used by the training data.
_FRAGMENT_DESCRIPTORS = [name for name in dir(Descriptors) if name.startswith('fr_')]

# Terpenoid/isoprenoid repeat-unit pattern (head-to-tail -CH2-C(CH3)=CH-CH2- linkage), e.g. as
# found in geraniol, limonene, squalene. Does not match free isoprene itself (two terminal =CH2
# groups), which is intentional -- this targets the polymerized/natural-product motif.
_ISOPRENE_PATTERN = Chem.MolFromSmarts('CC(C)=CC')

# Anomeric ring carbon (bonded to a ring oxygen) that also bears an exocyclic oxygen linked to
# another carbon, i.e. a glycosidic C-O-C bond. Free sugars (anomeric -OH, not attached to
# anything) do not match; glycosides (sugar attached to an aglycone or another sugar) do.
_GLYCOSYLATION_PATTERN = Chem.MolFromSmarts('[#6;R]([#8;R])[#8;!R][#6]')


def compute_feature_dict(smiles):
    """Return {feature_name: value} for every column the ml_classifier models expect, or None
    if the SMILES string could not be parsed."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    mol_h = Chem.AddHs(mol)
    atom_counts = {}
    for atom in mol_h.GetAtoms():
        symbol = atom.GetSymbol()
        atom_counts[symbol] = atom_counts.get(symbol, 0) + 1

    quaternary_carbons = sum(
        1 for atom in mol.GetAtoms()
        if atom.GetSymbol() == 'C'
        and atom.GetDegree() == 4
        and atom.GetTotalNumHs() == 0
        and all(neighbor.GetSymbol() == 'C' for neighbor in atom.GetNeighbors())
    )

    ring_sizes = [len(ring) for ring in mol.GetRingInfo().AtomRings()]

    features = {
        'NHOHCount': Descriptors.NHOHCount(mol),
        'NOCount': Descriptors.NOCount(mol),
        'NumAliphaticCarbocycles': Descriptors.NumAliphaticCarbocycles(mol),
        'NumAliphaticHeterocycles': Descriptors.NumAliphaticHeterocycles(mol),
        'NumAliphaticRings': Descriptors.NumAliphaticRings(mol),
        'NumAromaticCarbocycles': Descriptors.NumAromaticCarbocycles(mol),
        'NumAromaticHeterocycles': Descriptors.NumAromaticHeterocycles(mol),
        'NumAromaticRings': Descriptors.NumAromaticRings(mol),
        'NumHAcceptors': Descriptors.NumHAcceptors(mol),
        'NumHDonors': Descriptors.NumHDonors(mol),
        'NumHeteroatoms': Descriptors.NumHeteroatoms(mol),
        'NumRadicalElectrons': Descriptors.NumRadicalElectrons(mol),
        'NumRotatableBonds': Descriptors.NumRotatableBonds(mol),
        'NumSaturatedCarbocycles': Descriptors.NumSaturatedCarbocycles(mol),
        'NumSaturatedHeterocycles': Descriptors.NumSaturatedHeterocycles(mol),
        'NumSaturatedRings': Descriptors.NumSaturatedRings(mol),
        'NumValenceElectrons': Descriptors.NumValenceElectrons(mol),
        'TPSA': Descriptors.TPSA(mol),
        'MolMR': Descriptors.MolMR(mol),
        'MolWt': Descriptors.MolWt(mol),
        'MolLogP': Descriptors.MolLogP(mol),
        'BalabanJ': Descriptors.BalabanJ(mol),
        'BertzCT': Descriptors.BertzCT(mol),
        'Num_H': atom_counts.get('H', 0),
        'Num_B': atom_counts.get('B', 0),
        'Num_C': atom_counts.get('C', 0),
        'Num_N': atom_counts.get('N', 0),
        'Num_O': atom_counts.get('O', 0),
        'Num_F': atom_counts.get('F', 0),
        'Num_S': atom_counts.get('S', 0),
        'Num_Cl': atom_counts.get('Cl', 0),
        'Num_Br': atom_counts.get('Br', 0),
        'Num_I': atom_counts.get('I', 0),
        'NumChiralCenters': len(Chem.FindMolChiralCenters(mol, includeUnassigned=True, useLegacyImplementation=False)),
        'NumQuaternaryCarbons': quaternary_carbons,
        'max_ring_size': max(ring_sizes) if ring_sizes else 0,
        'contains_isoprene_subunit': int(mol.HasSubstructMatch(_ISOPRENE_PATTERN)),
        'contains_glycosylation': int(mol.HasSubstructMatch(_GLYCOSYLATION_PATTERN)),
    }

    for name in _FRAGMENT_DESCRIPTORS:
        features[name] = getattr(Descriptors, name)(mol)

    return features


def build_feature_vector(smiles, feature_names):
    """Return a list of feature values in the order given by feature_names, or None if the
    SMILES string could not be parsed."""
    features = compute_feature_dict(smiles)
    if features is None:
        return None

    missing = [name for name in feature_names if name not in features]
    if missing:
        raise KeyError(f"Cannot compute required feature(s): {missing}")

    return [features[name] for name in feature_names]

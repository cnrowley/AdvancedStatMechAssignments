"""Shared RDKit descriptor calculation for the ml_melting_point models.

Factored out of melting_point_lr.py/melting_point_mlp.py/melting_point_rf.py, which each used to
carry their own copy of this function. The original had a copy-pasted bug: Descriptors.fr_ArN was
computed (and listed as a column) twice, which silently created a duplicate 'fr_ArN' column in
the training data. Fixed here by listing it once.
"""

from rdkit import Chem
from rdkit.Chem import Descriptors

FEATURE_NAMES = [
    'NHOHCount', 'NOCount', 'NumAliphaticCarbocycles', 'NumAliphaticHeterocycles',
    'NumAliphaticRings', 'NumAromaticCarbocycles', 'NumAromaticHeterocycles',
    'NumAromaticRings', 'NumHAcceptors', 'NumHDonors', 'NumHeteroatoms',
    'NumRadicalElectrons', 'NumRotatableBonds', 'NumSaturatedCarbocycles',
    'NumSaturatedHeterocycles', 'NumSaturatedRings', 'NumValenceElectrons',
    'qed', 'TPSA', 'MolMR', 'BalabanJ', 'BertzCT', 'fr_Al_OH', 'fr_Al_OH_noTert',
    'fr_ArN', 'fr_Ar_COO', 'fr_Ar_NH', 'fr_Ar_OH', 'fr_COO',
    'fr_COO2', 'fr_C_O', 'fr_C_O_noCOO', 'fr_C_S', 'fr_HOCCN', 'fr_Imine',
    'fr_NH0', 'fr_NH1', 'fr_NH2', 'fr_N_O', 'fr_Ndealkylation1',
    'fr_Ndealkylation2', 'fr_Nhpyrrole', 'fr_SH', 'fr_aldehyde',
    'fr_alkyl_carbamate', 'fr_alkyl_halide', 'fr_allylic_oxid', 'fr_amide',
    'fr_amidine', 'fr_aniline', 'fr_aryl_methyl', 'fr_azide', 'fr_azo',
    'fr_barbitur', 'fr_benzene', 'fr_benzodiazepine', 'fr_bicyclic', 'fr_diazo',
    'fr_dihydropyridine', 'fr_epoxide', 'fr_ester', 'fr_ether', 'fr_furan',
    'fr_guanido', 'fr_halogen', 'fr_hdrzine', 'fr_hdrzone', 'fr_imidazole',
    'fr_imide', 'fr_isocyan', 'fr_isothiocyan', 'fr_ketone', 'fr_ketone_Topliss',
    'fr_lactam', 'fr_lactone', 'fr_methoxy', 'fr_morpholine', 'fr_nitrile',
    'fr_nitro', 'fr_nitro_arom_nonortho', 'fr_nitroso', 'fr_oxazole',
    'fr_oxime', 'fr_para_hydroxylation', 'fr_phenol', 'fr_phenol_noOrthoHbond',
    'fr_phos_acid', 'fr_phos_ester', 'fr_piperdine', 'fr_piperzine', 'fr_priamide',
    'fr_prisulfonamd', 'fr_pyridine', 'fr_quatN', 'fr_sulfide', 'fr_sulfonamd',
    'fr_sulfone', 'fr_term_acetylene', 'fr_tetrazole', 'fr_thiazole', 'fr_thiocyan',
    'fr_thiophene', 'fr_unbrch_alkane', 'fr_urea', 'MolWt', 'MolLogP',
]


def calculate_descriptors(smiles):
    """Return the descriptor list (in FEATURE_NAMES order) for a SMILES string, or None if it
    could not be parsed."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None

    return [
        Descriptors.NHOHCount(mol), Descriptors.NOCount(mol),
        Descriptors.NumAliphaticCarbocycles(mol), Descriptors.NumAliphaticHeterocycles(mol),
        Descriptors.NumAliphaticRings(mol), Descriptors.NumAromaticCarbocycles(mol),
        Descriptors.NumAromaticHeterocycles(mol), Descriptors.NumAromaticRings(mol),
        Descriptors.NumHAcceptors(mol), Descriptors.NumHDonors(mol),
        Descriptors.NumHeteroatoms(mol), Descriptors.NumRadicalElectrons(mol),
        Descriptors.NumRotatableBonds(mol), Descriptors.NumSaturatedCarbocycles(mol),
        Descriptors.NumSaturatedHeterocycles(mol), Descriptors.NumSaturatedRings(mol),
        Descriptors.NumValenceElectrons(mol), Descriptors.qed(mol),
        Descriptors.TPSA(mol), Descriptors.MolMR(mol), Descriptors.BalabanJ(mol),
        Descriptors.BertzCT(mol), Descriptors.fr_Al_OH(mol), Descriptors.fr_Al_OH_noTert(mol),
        Descriptors.fr_ArN(mol), Descriptors.fr_Ar_COO(mol),
        Descriptors.fr_Ar_NH(mol), Descriptors.fr_Ar_OH(mol), Descriptors.fr_COO(mol),
        Descriptors.fr_COO2(mol), Descriptors.fr_C_O(mol), Descriptors.fr_C_O_noCOO(mol),
        Descriptors.fr_C_S(mol), Descriptors.fr_HOCCN(mol), Descriptors.fr_Imine(mol),
        Descriptors.fr_NH0(mol), Descriptors.fr_NH1(mol), Descriptors.fr_NH2(mol),
        Descriptors.fr_N_O(mol), Descriptors.fr_Ndealkylation1(mol),
        Descriptors.fr_Ndealkylation2(mol), Descriptors.fr_Nhpyrrole(mol),
        Descriptors.fr_SH(mol), Descriptors.fr_aldehyde(mol),
        Descriptors.fr_alkyl_carbamate(mol), Descriptors.fr_alkyl_halide(mol),
        Descriptors.fr_allylic_oxid(mol), Descriptors.fr_amide(mol),
        Descriptors.fr_amidine(mol), Descriptors.fr_aniline(mol),
        Descriptors.fr_aryl_methyl(mol), Descriptors.fr_azide(mol),
        Descriptors.fr_azo(mol), Descriptors.fr_barbitur(mol),
        Descriptors.fr_benzene(mol), Descriptors.fr_benzodiazepine(mol),
        Descriptors.fr_bicyclic(mol), Descriptors.fr_diazo(mol),
        Descriptors.fr_dihydropyridine(mol), Descriptors.fr_epoxide(mol),
        Descriptors.fr_ester(mol), Descriptors.fr_ether(mol),
        Descriptors.fr_furan(mol), Descriptors.fr_guanido(mol),
        Descriptors.fr_halogen(mol), Descriptors.fr_hdrzine(mol),
        Descriptors.fr_hdrzone(mol), Descriptors.fr_imidazole(mol),
        Descriptors.fr_imide(mol), Descriptors.fr_isocyan(mol),
        Descriptors.fr_isothiocyan(mol), Descriptors.fr_ketone(mol),
        Descriptors.fr_ketone_Topliss(mol), Descriptors.fr_lactam(mol),
        Descriptors.fr_lactone(mol), Descriptors.fr_methoxy(mol),
        Descriptors.fr_morpholine(mol), Descriptors.fr_nitrile(mol),
        Descriptors.fr_nitro(mol),
        Descriptors.fr_nitro_arom_nonortho(mol), Descriptors.fr_nitroso(mol),
        Descriptors.fr_oxazole(mol), Descriptors.fr_oxime(mol),
        Descriptors.fr_para_hydroxylation(mol), Descriptors.fr_phenol(mol),
        Descriptors.fr_phenol_noOrthoHbond(mol), Descriptors.fr_phos_acid(mol),
        Descriptors.fr_phos_ester(mol), Descriptors.fr_piperdine(mol),
        Descriptors.fr_piperzine(mol), Descriptors.fr_priamide(mol),
        Descriptors.fr_prisulfonamd(mol), Descriptors.fr_pyridine(mol),
        Descriptors.fr_quatN(mol), Descriptors.fr_sulfide(mol),
        Descriptors.fr_sulfonamd(mol), Descriptors.fr_sulfone(mol),
        Descriptors.fr_term_acetylene(mol), Descriptors.fr_tetrazole(mol),
        Descriptors.fr_thiazole(mol), Descriptors.fr_thiocyan(mol),
        Descriptors.fr_thiophene(mol), Descriptors.fr_unbrch_alkane(mol),
        Descriptors.fr_urea(mol), Descriptors.MolWt(mol), Descriptors.MolLogP(mol),
    ]

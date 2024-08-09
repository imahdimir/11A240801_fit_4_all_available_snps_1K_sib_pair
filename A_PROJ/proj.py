"""

    Project-wide constants, directories, and file paths, file path patterns.

    """

from pathlib import Path

PROJ_DATA = Path('/var/genetics/ws/mahdimir/local/prj_data/24Q3/11A240801_merge_gt_data_by_SNPs_1K_sib_pair')

class Directory :
    p = PROJ_DATA

    inp = p / 'inp'
    med = p / 'med'
    out = p / 'out'

    # snps_by_chr = inp / 'snps_by_chr'
    gt_by_individual = inp / 'gt_by_individual'

DIR = Directory()

class FilePath :
    d = DIR

    # lift snps from imputed data, that are drawn randomly with some conditions
    lift_snps = d.inp / 'snps.lift.bed'

    # lifted SNSPs from GRCH37 to GRCH38 (from imputed data to WGS data)
    lifted_snps = d.inp / 'snps.lifted'

    # rsids to be used in the analysis, with index (to use as a map for file names)
    rsids = d.med / 'rsids.parquet'


FILE_PATH = FilePath()

class FilePathPattern :
    pass

FILE_PATH_PAT = FilePathPattern()


class Var :
    rsid = 'rsid'
    iid = 'IID'

    id1 = 'ID1'
    id2 = 'ID2'
    inf_type = 'InfType'
    fs = 'FS'
    po = 'PO'
    iid = 'IID'
    check = 'Check'
    suf = 'suffix'
    fol = 'folder'
    path = 'path'
    s1_check = 'S1Check'
    s2_check = 'S2Check'
    fn = 'fn'
    g1 = 'g1'
    g2 = 'g2'
    g1_plus_g2 = 'g1_plus_g2'
    g1_minus_g2 = 'g1_minus_g2'
    g1_hat = 'g1_hat'
    g2_hat = 'g2_hat'
    g1_plus_g2_hat = 'g1_plus_g2_hat'
    g1_minus_g2_hat = 'g1_minus_g2_hat'


VAR = Var()

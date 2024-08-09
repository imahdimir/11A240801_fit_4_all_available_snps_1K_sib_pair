"""

    Project-wide constants, directories, and file paths, file path patterns.

    """

from pathlib import Path

PROJ_DATA = Path('/var/genetics/ws/mahdimir/local/prj_data/24Q3/11A240801_fit_4_all_available_snps_1K_sib_pair')

class Directory :
    p = PROJ_DATA

    inp = p / 'inp'
    med = p / 'med'
    out = p / 'out'

    # snps_by_chr = inp / 'snps_by_chr'

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

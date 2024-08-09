"""

    Project-wide constants, directories, and file paths, file path patterns.

    """

from pathlib import Path

PROJ_DATA = Path('/var/genetics/ws/mahdimir/local/prj_data/24Q3/11A240801_fit_4_all_available_snps_1K_sib_pair')

class Dir :
    inp = PROJ_DATA / 'inp'
    med = PROJ_DATA / 'med'
    out = PROJ_DATA / 'out'

    # snps_by_chr = inp / 'snps_by_chr'

DIR = Dir()

class FilePath :
    # lift snps from imputed data, that are drawn randomly with some conditions
    lift_snps = DIR.med / 'snps.lift.bed'
    # lifted SNSPs from GRCH37 to GRCH38 (from imputed data to WGS data)
    lifted_snps = DIR.out / 'snps.lifted'


FILE_PATH = FilePath()

class FilePathPattern :
    pass

FILE_PATH_PAT = FilePathPattern()

"""

    """

PROJ_DATA = '/var/genetics/ws/mahdimir/local/prj_data/24Q3/11A240801_fit_4_all_available_snps_1K_sib_pair'

class Dir :
    inp = PROJ_DATA / 'inp'
    med = PROJ_DATA / 'med'
    out = PROJ_DATA / 'out'

    snps_by_chr = inp / 'snps_by_chr'


DIR = Dir()

class FilePathPattern :
    snps_by_chr = str(DIR.snps_by_chr / 'c{chr_num}.txt')

FILE_PATH_PAT = FilePathPattern()

class Files :
    all_snps = DIR.med / 'snps.lift.bed'

FILE = Files()

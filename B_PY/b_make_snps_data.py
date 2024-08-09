"""

    """

import pandas as pd


from A_PROJ.proj import FILE_PATH, DIR


##
fps = DIR.inp.glob('*.parquet')
list(fps)


##






##
# # reading a parquet file for a single individual to see how it is structured, I forgot the structure of the parquet file

fn = '/var/genetics/ws/mahdimir/local/prj_data/24Q3/09A240711_verify_all_individual_IDs_are_available/med/gt_by_individual/6019200_24053_0_0.dragen.hard-filtered.vcf.filtered.parquet'

df = pd.read_parquet(fn)

##
fn = '/var/genetics/ws/mahdimir/local/prj_data/24Q3/11A240801_fit_4_all_available_snps_1K_sib_pair/inp/chr_pos_rsid_map.p'

df1 = pd.read_parquet(fn)

##

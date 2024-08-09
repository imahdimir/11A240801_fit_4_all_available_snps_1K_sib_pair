"""

    """

import pandas as pd


from A_PROJ.proj import FILE_PATH, DIR, VAR


##
# read all the list of rsids that are common in [filtered] WGS and imputed data
rsid_df = pd.read_parquet(FILE_PATH.rsids)

##
# get the first rsid to test/develop code
idx, row = next(rsid_df.iterrows())
rsid = row[VAR.rsid]
rsid

##
def get_iid_from_fn(fn):
    return int(fn.split('_')[0])

# get all the parquet files for gt by individual
# each file contains the gt data for an individual for different rsids
fps = DIR.gt_by_individual.glob('*.parquet')


# to gather all the genotype(gt) data for a single rsid
gts_df = pd.DataFrame()

##
def add_ind_gt_to_agg_df(ind_fp, gts_df, rsid):
    print(ind_fp)

    # read individual gt data
    ind_df = pd.read_parquet(ind_fp)

    # add individual gt to the aggreate on rsid data with iid
    if rsid in ind_df.columns:
        print('yes')

        ind_df[VAR.iid] = get_iid_from_fn(_fp.name)
        ind_df = ind_df[[VAR.iid, rsid]]

        # adding individual data to the aggregate dataframe
        gts_df = pd.concat([gts_df, ind_df], axis = 0)

    return gts_df

##
# loop through the first 10 individual files to test the code
for _fp in fps[:10]:
    gts_df = add_ind_gt_to_agg_df(_fp, gts_df, rsid)



##





##






##
# # reading a parquet file for a single individual to see how it is structured, I forgot the structure of the parquet file

fn = '/var/genetics/ws/mahdimir/local/prj_data/24Q3/09A240711_verify_all_individual_IDs_are_available/med/gt_by_individual/6019200_24053_0_0.dragen.hard-filtered.vcf.filtered.parquet'

ind_df = pd.read_parquet(fn)

##
fn = '/var/genetics/ws/mahdimir/local/prj_data/24Q3/11A240801_fit_4_all_available_snps_1K_sib_pair/inp/chr_pos_rsid_map.p'

df1 = pd.read_parquet(fn)

##

"""

    """

import pandas as pd
import time

from A_PROJ.proj import FILE_PATH , DIR , VAR , FILE_PATH_PATRN , PROJ_DATA

D = DIR
FP = FILE_PATH
FPP = FILE_PATH_PATRN
V = VAR
PD = PROJ_DATA

def get_iid_from_fn(fn) :
    return int(fn.split('_')[0])

def add_ind_gt_to_agg_df(ind_fp , gts_df , rsid) :
    # read individual gt data
    ind_df = pd.read_parquet(ind_fp)

    if rsid in ind_df.columns :

        ind_df[VAR.iid] = get_iid_from_fn(ind_fp.name)
        ind_df = ind_df[[VAR.iid , rsid]]

        # add individual gt to the aggreate on rsid data with iid
        gts_df = pd.concat([gts_df , ind_df] , axis = 0)

    else :
        pass

    return gts_df

def get_all_individuals_for_one_snp(rsid) :
    gts_df = pd.DataFrame()

    # get all the parquet files for gt by individual
    # each file contains the gt data for an individual for different rsids
    fps = DIR.gt_by_individual.glob('*.parquet')

    start_time = time.time()

    for _fp in list(fps) :
        gts_df = add_ind_gt_to_agg_df(_fp , gts_df , rsid)

    end_time = time.time()  # Stop the timer
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f'Time elapsed: {elapsed_time} seconds')
    print(rsid, 'df shape:', gts_df.shape)

    return gts_df

def get_10_rsids_gts(rsid_df) :
    for idx , rsid in rsid_df.iloc[:10].iterrows() :
        gts_df = get_all_individuals_for_one_snp(rsid[VAR.rsid])
        fn = FPP.wgs_gt_by_snp.format(rsid_idx = idx)
        gts_df.to_parquet(fn , index = False)

def main() :
    pass

    ##
    start_time = time.time()

    # read all the list of rsids that are common in [filtered] WGS and imputed data
    rsid_df = pd.read_parquet(FILE_PATH.rsids)
    get_10_rsids_gts(rsid_df)

    end_time = time.time()  # Stop the timer
    elapsed_time = end_time - start_time  # Calculate the elapsed time
    print(f'Time elapsed: {elapsed_time} seconds')

    ##

    ##

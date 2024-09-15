"""

    """

import pandas as pd
import time

##
from A_PROJ.proj import FILE_PATH, DIR, VAR,FILE_PATH_PATRN, PROJ_DATA

##
D = DIR
FP = FILE_PATH
FPP = FILE_PATH_PATRN
V = VAR
PD = PROJ_DATA

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

# to gather all the genotype(gt) data for a single rsid
gts_df = pd.DataFrame()

##
def add_ind_gt_to_agg_df(ind_fp, gts_df, rsid):
    # print(ind_fp.name)

    # read individual gt data
    ind_df = pd.read_parquet(ind_fp)

    if rsid in ind_df.columns:
        # print('yes')

        ind_df[VAR.iid] = get_iid_from_fn(_fp.name)
        ind_df = ind_df[[VAR.iid, rsid]]

        # add individual gt to the aggreate on rsid data with iid
        gts_df = pd.concat([gts_df, ind_df], axis = 0)

    else:
        # print(f'{rsid} is not available.')
        pass

    return gts_df


##

# get all the parquet files for gt by individual
# each file contains the gt data for an individual for different rsids
fps = DIR.gt_by_individual.glob('*.parquet')

##
gts_df = pd.DataFrame()

# loop through the first 10 individual files to test the code
for _fp in list(FPS)[:100]:
    gts_df = add_ind_gt_to_agg_df(_fp, gts_df, rsid)

##
gts_df.to_parquet(FPP.wgs_gt_by_snp.format(rsid_idx = idx), index=False)

##
def loop_through_all_individuals_for_one_snp(rsid_idx, rsid):
    gts_df = pd.DataFrame()

    # get all the parquet files for gt by individual
    # each file contains the gt data for an individual for different rsids
    fps = DIR.gt_by_individual.glob('*.parquet')

    for _fp in list(fps)[:100]:
        gts_df = add_ind_gt_to_agg_df(_fp, gts_df, rsid)

    fo = FPP.wgs_gt_by_snp.format(rsid_idx = rsid_idx)
    print(fo)
    gts_df.to_parquet(fo, index=False)

    return gts_df

##
start_time = time.time()  # Start the timer

# Execute the function with arguments
gts_df = loop_through_all_individuals_for_one_snp(idx, rsid)

end_time = time.time()  # Stop the timer

elapsed_time = end_time - start_time  # Calculate the elapsed time

print(f'Time elapsed: {elapsed_time} seconds')

##
from multiprocessing import Pool

##
starmap_arg = zip(rsid_df.index, rsid_df[VAR.rsid])

with Pool(20) as p:
    p.starmap(loop_through_all_individuals_for_one_snp, starmap_arg)

##

# The problem is that the runtime is too long, for just 1 snp it takes 20 mins
# so it is not feasible to run the code for all the snps

# I need to find a way to make the code faster

##

# now I want to find a way to read 100 or 1000 files at a time

##

import dask.dataframe as dd
import os

from dask.distributed import Client

# Create a Dask client and specify the number of cores
client = Client(n_workers=20)

##
# Directory containing the Parquet files

# parquet_directory = "path_to_your_parquet_files"

# Get all Parquet file paths
# parquet_files = [os.path.join(parquet_directory, f) for f in os.listdir(parquet_directory) if f.endswith('.parquet')]

fps = DIR.gt_by_individual.glob('*.parquet')

# Define a function to read a single Parquet file and add the filename as a column
def read_parquet_with_filename(file_path):
    df = dd.read_parquet(file_path, engine='pyarrow')
    filename = os.path.basename(file_path)
    df['filename'] = filename
    return df

start_time = time.time()  # Start the timer

# Use Dask to read and concatenate all Parquet files
df = dd.concat([read_parquet_with_filename(file) for file in fps])

# Compute the final DataFrame (if you need it as a pandas DataFrame)
final_df = df.compute()

elapsed_time = end_time - start_time  # Calculate the elapsed time

print(f'Time elapsed: {elapsed_time} seconds')

##


##
import polars as pl
import os
from multiprocessing import Pool, cpu_count

##
def read_parquet_with_filename(file_path):
    df = pl.read_parquet(file_path)
    filename = os.path.basename(file_path)
    df = df.with_columns(pl.lit(filename).alias('filename'))
    return df

def parallel_read_parquet(parquet_files):
    # Use all available CPU cores or specify a custom number
    with Pool(20) as pool:
        dfs = pool.map(read_parquet_with_filename, parquet_files)
    # Concatenate all the DataFrames into one
    return dfs

def outer_merge_dataframes(dfs):
    merged_df = dfs[0]
    for df in dfs[1:]:
        merged_df = merged_df.join(df, on=merged_df.columns, how="outer")
    return merged_df


##
# Directory containing Parquet files
parquet_directory = D.gt_by_individual
parquet_directory

##
# Get all Parquet file paths
parquet_files = [os.path.join(parquet_directory, f) for f in os.listdir(parquet_directory) if f.endswith('.parquet')]

##
# Perform the parallel read and merge
start_time = time.time()  # Start the timer


# Perform the parallel read and merge
merged_df = parallel_read_parquet(parquet_files)


end_time = time.time()  # Stop the timer

elapsed_time = end_time - start_time  # Calculate the elapsed time

print(f'Time elapsed: {elapsed_time} seconds')

# Save or further process the DataFrame
merged_df.write_parquet(PD / "merged_output.parquet")

##




##




##


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

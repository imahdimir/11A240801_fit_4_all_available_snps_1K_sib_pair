"""

    """

import pandas as pd


##

# # reading a parquet file for a single individual to see how it is structured, I forgot the structure of the parquet file

fn = '/var/genetics/ws/mahdimir/local/prj_data/24Q3/09A240711_verify_all_individual_IDs_are_available/med/gt_by_individual/6019200_24053_0_0.dragen.hard-filtered.vcf.filtered.parquet'

df = pd.read_parquet(fn)

##
fn = '/var/genetics/ws/mahdimir/local/prj_data/24Q3/11A240801_fit_4_all_available_snps_1K_sib_pair/inp/chr_pos_rsid_map.p'

df1 = pd.read_parquet(fn)

##



##


##

##

fn = '/var/genetics/ws/mahdimir/chr_pos_rsid_map.p'

df1 = pd.read_parquet(fn)

##

# are lifted and original snps the same?

f2 = '/var/genetics/ws/mahdimir/local/prj_data/24Q2/6A240625_liftover_GRCH37_2_GRCH38/out/snps.lifted'
df2 = pd.read_csv(f2 , sep= '\t' , header=None , names=['chr', 'start','end', 'rsid'])

f3 = '/var/genetics/ws/mahdimir/local/prj_data/24Q2/6A240625_liftover_GRCH37_2_GRCH38/med/snps.lift.bed'
df3 = pd.read_csv(f3 , sep= '\t' , header=None , names=['chr', 'start','end', 'rsid'])

##
df4 = df2.merge(df3, on=['chr', 'start', 'end'], how='outer', indicator=True)

##
df3['rsid'].nunique()

##
df3.drop_duplicates(subset=['rsid']).shape

##
df3.drop_duplicates(subset=['chr', 'start', 'end']).shape

##
df3.drop_duplicates().shape

##
import subprocess
import os

def get_git_repo_name():
    try:
        # Run the git rev-parse command to get the top-level directory of the repo
        result = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'],
            capture_output=True,
            text=True,
            check=True
        )
        # Get the top-level directory path and extract the repo name
        repo_path = result.stdout.strip()
        repo_name = os.path.basename(repo_path)
        return repo_name
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None

repo_name = get_git_repo_name()
if repo_name:
    print(f"Current Git repository name: {repo_name}")
else:
    print("Failed to get Git repository name.")






##
from pathlib import Path

Path.cwd()

##






##
all_snps = set(df.columns)






##

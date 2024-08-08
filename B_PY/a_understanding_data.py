"""

    """

import pandas as pd


##

f3 = '/var/genetics/ws/mahdimir/local/prj_data/24Q2/6A240625_liftover_GRCH37_2_GRCH38/med/snps.lift.bed'
df = pd.read_csv(f3 , sep= '\t' , header=None , names=['chr', 'start', 'end', 'rsid'])

##

# are all rows unique in the original snps?

df.shape[0] == df.drop_duplicates().shape[0]

# No, they are not unique, so I should drop not unique rows

##

df = df.drop_duplicates()

##

# are rsids unique in the original snps?
df.shape[0] == df['rsid'].nunique()

# Yes

##

# are locations unique?
df.shape[0] == df.drop_duplicates(subset=['chr', 'start', 'end']).shape[0]

# No, some locations have multiple rsids

##

# how many non-unique locations are there?
df.shape[0] - df.drop_duplicates(subset=['chr', 'start', 'end']).shape[0]

df1 = df[df.duplicated(subset=['chr', 'start', 'end'], keep=False)]

# There are only 7 locations with multiple rsids in the original snps
# so it is not a big deal to drop them

# drop duplicated rows as duos remove both/any dups, don't keep any of them

df = df.drop_duplicates(subset=['chr', 'start', 'end'], keep=False)

##

# check chr and start are unique
df.shape[0] == df.drop_duplicates(subset=['chr', 'start']).shape[0]

# yes

##




##




##
# are lifted and original snps the same?

f2 = '/var/genetics/ws/mahdimir/local/prj_data/24Q2/6A240625_liftover_GRCH37_2_GRCH38/out/snps.lifted'
df2 = pd.read_csv(f2 , sep= '\t' , header=None , names=['chr', 'start','end', 'rsid'])


##
df4 = df2.merge(df , on=['chr', 'start', 'end'] , how= 'outer' , indicator=True)

##
df['rsid'].nunique()

##
df.drop_duplicates(subset=['chr', 'start', 'end']).shape

##
df.drop_duplicates().shape

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

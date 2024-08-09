"""

    """

import pandas as pd
from A_PROJ.proj import FILE_PATH

##

fp = FILE_PATH.lift_snps

df = pd.read_csv(fp ,
                 sep = '\t' ,
                 header = None ,
                 names = ['chr' , 'start' , 'end' , 'rsid'])

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
df.shape[0] == df.drop_duplicates(subset = ['chr' , 'start' , 'end']).shape[0]

# No, some locations have multiple rsids

##

# how many non-unique locations are there?
df.shape[0] - df.drop_duplicates(subset = ['chr' , 'start' , 'end']).shape[0]

df1 = df[df.duplicated(subset = ['chr' , 'start' , 'end'] , keep = False)]

# There are only 7 locations with multiple rsids in the original snps
# so it is not a big deal to drop them

# drop duplicated rows as duos remove both/any dups, don't keep any of them

df = df.drop_duplicates(subset = ['chr' , 'start' , 'end'] , keep = False)

##

# check chr and start are unique
df.shape[0] == df.drop_duplicates(subset = ['chr' , 'start']).shape[0]

# yes

##

# understanding lifted data

# are lifted and original snps the same?

f2 = '/var/genetics/ws/mahdimir/local/prj_data/24Q2/6A240625_liftover_GRCH37_2_GRCH38/out/snps.lifted'
dfb = pd.read_csv(f2 ,
                  sep = '\t' ,
                  header = None ,
                  names = ['chr' , 'start' , 'end' , 'rsid'])

##
df4 = dfb.merge(df ,
                on = ['chr' , 'start' , 'end'] ,
                how = 'outer' ,
                indicator = True)

# no they are not the same

##

# are set of rsids the same in both data?

set(dfb['rsid']) == set(df['rsid'])

# no unfortunately

##

# do we have new rsids in the lifted files?
# check if all lifted rsids are in the original snps if yes
# then we don't have new rsids

dfb['rsid'].isin(df['rsid']).all()

# no, we have new rsids in the lifted data

##

# how many new rsids do we have in the lifted data?
dfb[~dfb['rsid'].isin(df['rsid'])].shape

# 14 rows, the same number of duplicated rows on rsid in the original snps
# but this accident is not related to the new rsids in the lifted data
# because I already dropped the duplicated rows in the original snps

df1 = dfb[~dfb['rsid'].isin(df['rsid'])]

# I just drop the new rsids in the lifted data

dfb = dfb[dfb['rsid'].isin(df['rsid'])]


##

# just to make sure that we have all the lifted rsids in the original snps
# after dropping the new rsids
dfb['rsid'].isin(df['rsid']).all()

##




##







##


##


##

##
df['rsid'].nunique()

##
df.drop_duplicates(subset = ['chr' , 'start' , 'end']).shape

##
df.drop_duplicates().shape

##
import subprocess
import os

def get_git_repo_name() :
    try :
        # Run the git rev-parse command to get the top-level directory of the repo
        result = subprocess.run(['git' , 'rev-parse' , '--show-toplevel'] ,
                capture_output = True ,
                text = True ,
                check = True)
        # Get the top-level directory path and extract the repo name
        repo_path = result.stdout.strip()
        repo_name = os.path.basename(repo_path)
        return repo_name
    except subprocess.CalledProcessError as e :
        print(f"An error occurred: {e}")
        return None

repo_name = get_git_repo_name()
if repo_name :
    print(f"Current Git repository name: {repo_name}")
else :
    print("Failed to get Git repository name.")

##
from pathlib import Path

Path.cwd()

##


##
all_snps = set(df.columns)

##

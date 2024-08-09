"""

    """

import pandas as pd
import numpy as np

from A_PROJ.proj import FILE_PATH

##

fp1 = FILE_PATH.lift_snps

df = pd.read_csv(fp1 ,
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

fp2 = FILE_PATH.lifted_snps
dfb = pd.read_csv(fp2 ,
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

# make sure index is unique (should be unique already)
# I need it to be unique to use it as a map for file names

dfb.index.is_unique

# yes it is

##

dfb.to_parquet(FILE_PATH.rsids)

##

# reading the parquet file to make sure it is saved correctly

dfc = pd.read_parquet(FILE_PATH.rsids)


##
dfb.eq(dfc).all().all()

# yes, they are the same

##
np.all(dfb.index == dfc.index)

# yes, the index is the same
# thanks god!

##

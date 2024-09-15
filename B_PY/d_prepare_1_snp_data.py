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

RSID = 'rs11586607'

FN = D.wgs_gt_by_snp / '8.parquet'

def main() :
    pass

    ##
    df_snp_gt = pd.read_parquet(FN)

    ##
    df_sibs_map = pd.read_parquet(FP.sibs_map)

    ##
    df_sibs_map = df_sibs_map[[V.id1 , V.id2]]

    ##
    df_sibs_map = df_sibs_map.astype('string')

    ##
    df_snp_gt[V.iid] = df_snp_gt[V.iid].astype('string')
    df_snp_gt = df_snp_gt.set_index(V.iid)

    ##
    df = df_sibs_map.copy()

    ##
    df[V.g1] = df[V.id1].map(df_snp_gt[RSID])
    df[V.g2] = df[V.id2].map(df_snp_gt[RSID])

    ##
    df = df.dropna()

    ##
    df[V.g1_plus_g2] = df[V.g1] + df[V.g2]
    df[V.g1_minus_g2] = df[V.g1] - df[V.g2]

    ##
    df.to_parquet(FP.sibs_rs11586607, index = False)

    ##
    fn = '/var/genetics/ws/mahdimir/local/prj_data/24Q2/4A240411_plot_all_70_bins/med/hc/c1.prq'

    df1 = pd.read_parquet(fn)

    ##
    df1 = df1[[V.iid , RSID]]

    ##
    df1 = df1.set_index(V.iid)

    df[V.g1_hat] = df[V.id1].map(df1[RSID])
    df[V.g2_hat] = df[V.id2].map(df1[RSID])

    ##
    df[V.g1_plus_g2_hat] = df[V.g1_hat] + df[V.g2_hat]

    ##
    df[V.g1_minus_g2_hat] = df[V.g1_hat] - df[V.g2_hat]

    ##
    df.to_parquet(FP.imputed_rs11586607 , index = False)

    ##

    ##

    ##

    ##

    ##

    ##
    'Tammy Tan^1'
    ##

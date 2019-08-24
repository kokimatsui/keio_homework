#!-*-coding:utf-8-*-
import os
import sys
import numpy as np
import pandas as pd
__all__ = ["load","df2mat"]

def load( filename ):
    """
    CSVを読み込んでDataframeに変換する
    """
    file = os.path.dirname( os.path.abspath(__file__) ) + "/../dataset/" + filename

    return pd.read_csv( file )


def df2mat( df , columns ):
    """
    Dataframeから特定の列を取得して行列に変換する
    """
    Y = np.array( df.loc[ : , columns ]  , dtype=np.float64)
    if len( columns ) <= 1:
        Y = Y.T[0]

    return Y

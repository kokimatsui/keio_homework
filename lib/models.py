#!-*-coding:utf-8-*-
import os
import sys
import numpy as np
sys.path.append( "../" )
import lib

__all__ = ["random_effect"]

def random_effect( df , group , X_cols , Y_cols ):
    """
    変量効果モデル
    """
    fixed = _convert( df=df , group=group )
    params = {}
    for key , value in fixed.items():
        X = lib.df2mat( df=value , columns=X_cols )
        Y = lib.df2mat( df=value , columns=Y_cols )
        b = lib.reg( X=X , Y=Y )
        params[key] = b

    return params



def _convert( df , group ):
    fixed = {}
    for key , value in df.groupby(group).groups.items():
        fixed[ key ] = df.iloc[ value , : ]

    return fixed

#!-*-coding:utf-8-*-
import sys
import numpy as np
from numpy.random import *

__all__ = ["u","var","t"]

def u( X ):
    """
    母平均
    """
    vars = []
    if X.ndim == 1:
        for i in range( 0 , 1000 ):
            samp = _sampling( X=X )
            vars.append( np.average( samp ) )

        return np.average( np.array( vars ) )

def var( X ):
    """
    不偏分散
    """
    if X.ndim == 1:
        return np.var( X , ddof=1 )

def t( X , beta ):
    """
    t値
    """
    if X.ndim == 1:
        t = ( np.average( X ) ) / np.sqrt( np.var( X , ddof=1 ) / len( X ) )

    return round( t , 5 )



def _sampling( X ):
    """
    ランダムサンプリング
    """
    if X.ndim == 1:
        return choice( X , len( X ) - 5 )

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

def t( X , Y , beta ):
    """
    t値
    """
    X_bar = np.average( X )
    Y_hat = np.dot( X , beta )
    std_error = np.sqrt( ( np.sum( (  Y - Y_hat  ) ** 2 ) / ( len( Y ) - 2 ) ) / np.sum( ( X - X_bar )**2 ) )

    return ( beta / std_error )



def _sampling( X ):
    """
    ランダムサンプリング
    """
    if X.ndim == 1:
        return choice( X , len( X ) - 5 )

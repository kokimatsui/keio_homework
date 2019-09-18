#!-*-coding:utf-8-*-
import sys
import numpy as np
from scipy.stats import t as t_test
from numpy.random import *

__all__ = ["u","var","t","t_level"]

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


def t( X , Y , beta , beta_01=0 ):
    """
    t値
    """
    st_err  = std_error( X=X , Y=Y , beta=beta )

    return ( ( beta - beta_01 ) / st_err )

def std_error( X , Y , beta ):

    X_bar = np.average( X )
    Y_hat = np.dot( X , beta )
    st_err = np.sqrt( ( np.sum( (  Y - Y_hat  ) ** 2 ) / ( len( Y ) - 2 ) ) / np.sum( ( X - X_bar )**2 ) )

    return st_err


def t_level( free , level=5 ):
    """
    統計的に有意か調査
    """

    return t_test.ppf( q=( 1 - level * 0.01 ) , df=free )

def conf_inter( beta , free , se ):
    pass


def _sampling( X ):
    """
    ランダムサンプリング
    """
    if X.ndim == 1:
        return choice( X , len( X ) - 5 )

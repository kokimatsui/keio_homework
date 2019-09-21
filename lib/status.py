#!-*-coding:utf-8-*-
import sys
import numpy as np
from scipy.stats import t as t_test
from numpy.random import *

__all__ = ["u","var","t","t_level","conf_inter","std_error","t_v2","std_error_v2"]

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
    """
    標準誤差
    """
    X_bar = np.average( X )
    Y_hat = np.dot( X , beta )
    st_err = np.sqrt( ( np.sum( (  Y - Y_hat  ) ** 2 ) / ( len( Y ) - 2 ) ) / np.sum( ( X - X_bar )**2 ) )

    return st_err


def t_v2( X , Y , beta , beta_01=0 , num=0 ):
    """
    t値
    """
    t = []
    for i in range( len( beta ) ):
        st_err = std_error_v2( X=X , Y=Y , beta=beta , num=i )
        print( st_err )
        t.append( ( ( beta[i] - beta_01 ) / st_err ) )

    return np.array( t )


def std_error_v2( X , Y , beta , num=0 ):
    """
    標準誤差
    """
    Y_hat = np.dot( X , beta )
    RSS = ( np.sum( (  Y - Y_hat  ) ** 2 ) )
    X_Sq = np.sum( X[:,num] ** 2 )
    N = ( len( Y ) - 2 )
    S_sq = RSS / N

    return np.sqrt( S_sq / X_Sq )


def t_level( free , level=5 ):
    """
    統計的に有意か調査
    """

    return t_test.ppf( q=( 1 - level * 0.01 ) , df=free )


def conf_inter( beta , t , free , se ):
    """
    95%信頼区間の上限と下限を算出
    """
    a1 = ( beta - t * se )
    a2 = ( beta + t * se )
    if a1 < a2:
        return { "Lower" : a1 , "Upper" : a2 }
    else:
        return { "Lower" : a2 , "Upper" : a1 }

def _sampling( X ):
    """
    ランダムサンプリング
    """
    if X.ndim == 1:
        return choice( X , len( X ) - 5 )

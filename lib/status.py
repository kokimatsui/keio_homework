#!-*-coding:utf-8-*-
import sys
import numpy as np
from scipy.stats import t as t_test
from numpy.random import *

__all__ = ["u","var","t","t_level","conf_inter","std_error","t_v2","std_error_v2","R_Squere"]

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


def t_v2( X , Y , beta , beta_01=0 ):
    """
    t値
    """
    t = []
    for i in range( len( beta ) ):
        st_err = std_error_v2( X=X , Y=Y , beta=beta , num=i )
        t.append( ( ( beta[i] - 0  ) / st_err ) )


    return np.array( t )


def std_error_v2( X , Y , beta , num=0 ):
    """
    標準誤差
    """
    X_col = X[:,num]
    Y_hat = np.dot( X , beta )
    RSS = np.sum( (  Y - Y_hat  ) ** 2 )
    if np.max( X_col ) == 1.0 and np.min( X_col ) == 1.0:

        return np.sqrt( RSS / ( len( Y ) - len( beta ) ) )
    else:
        X_Sq = np.sum( ( ( X_col - np.average( X_col ) ) ) ** 2 )
        S_sq = RSS / ( len( Y ) - 2 )

        return np.sqrt( S_sq / X_Sq )


def t_level( free , level=5 ):
    """
    統計的に有意か調査
    """

    return t_test.ppf( q=( 1 - level * 0.01 ) , df=free )


def conf_inter( beta ):
    """
    95%信頼区間の上限と下限を算出
    """
    a1 = ( beta - 1.96 * 0.30119363859716236 )
    a2 = ( beta + 1.96 * 0.30119363859716236 )
    if a1 < a2:
        return { "Lower" : a1 , "Upper" : a2 }
    else:
        return { "Lower" : a2 , "Upper" : a1 }

def R_Squere( Y , X , beta ):
    """
    自由度調整済み決定係数
    """
    Y_bar = np.average( Y )
    Y_hat = np.dot( X , beta )
    R = 1 - ( ( np.sum( ( Y - Y_hat ) ** 2 ) / ( len( Y ) - len( beta ) - 1 ) ) / ( np.sum( ( Y - Y_bar )**2 ) / ( len( Y ) - 1 ) ) )

    return R


def _sampling( X ):
    """
    ランダムサンプリング
    """
    if X.ndim == 1:
        return choice( X , len( X ) - 5 )

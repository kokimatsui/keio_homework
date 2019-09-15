#!-*-coding:utf-8-*-
import numpy as np

__all__ = ["reg"]

def reg( X , Y ):
    """
    回帰分析
    """
    X_tX = np.dot( X.T , X )
    X_tY = np.dot( X.T , Y )
    beta = np.dot( np.linalg.inv( X_tX ) , X_tY )

    return beta

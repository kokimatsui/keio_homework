#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np

#####データを読み取る#####
artifical_dataset = lib.load( filename="artificial.csv" )
explanatories = ["x1","x2"]
explained = ["y"]

#####各変数を定義#####
X = lib.df2mat( df=artifical_dataset , columns=explanatories )
Y = lib.df2mat( df=artifical_dataset , columns=explained )

#####演算#####
X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )

lib.add_suffix( b )

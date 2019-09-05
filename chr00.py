#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np

#####データを読み取る#####
artifical_dataset = lib.load( filename="artificial.csv" )
explanatories = ["x1","const"]
explained = ["y"]

#####各変数を定義#####
X = lib.df2mat( df=artifical_dataset , columns=explanatories )
Y = lib.df2mat( df=artifical_dataset , columns=explained )


#####演算#####
X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )

print( "大問1.1の回答" )
lib.add_suffix( b )

print( "大問1.2の回答" )
beta_1 = b[0]
X1 = lib.df2mat( df=artifical_dataset , columns=["x1"] )
print( "t値 :" , lib.t( X=X1  , beta=beta_1 ) )

print( "大問1.3の回答" )
#ここに回答プログラムを記載する

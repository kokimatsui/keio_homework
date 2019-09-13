#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np

#####データを読み取る#####
artifical_dataset = lib.load( filename="artificial.csv" )
explanatories = ["const","x1"]
explained = ["y"]

#####各変数を定義#####
X = lib.df2mat( df=artifical_dataset , columns=explanatories )
Y = lib.df2mat( df=artifical_dataset , columns=explained )


#####演算#####
X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )

print( "<大問1.1の回答>" )
lib.add_suffix( b )

print( "<大問1.2の回答>" )
t = lib.t( X=X , Y=Y , beta=b )[0]
print( "t value :" ,  )
print( "自由度998で、2.581を基準にしたところ 2.581 <" , t , "なので、1%水準でβ0 = 0は棄却される" )

print( "<大問1.3の回答>" )
artifical_dataset = lib.load( filename="artificial.csv" )
explanatories = ["x1","x2","x3","const"]
explained = ["y"]

X = lib.df2mat( df=artifical_dataset , columns=explanatories )
Y = lib.df2mat( df=artifical_dataset , columns=explained )

#####演算#####
X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )
lib.add_suffix( b )

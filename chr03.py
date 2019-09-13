#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np

#####データを読み取る#####
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["const","lsales","lmktval"]
explained = ["lsalary"]

print( "大問3.1の回答" )
X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
Y = lib.df2mat( df=CEOSAL2_dataset , columns=explained )

X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )
lib.add_suffix( b )

print( "大問3.2の回答" )
#####データを読み取る#####
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["const","lsales","lmktval","profits"]
explained = ["lsalary"]

X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
Y = lib.df2mat( df=CEOSAL2_dataset , columns=explained )

X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )
#lib.add_suffix( b )

print( "大問3.3の回答" )
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["const","lsales","lmktval","profits","ceoten"]
explained = ["lsalary"]

X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
Y = lib.df2mat( df=CEOSAL2_dataset , columns=explained )

X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )
#lib.add_suffix( b )

print( str( 0.01168 * 100 ) , "%" )

print( "大問3.4の回答" )
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["profits","lmktval"]

X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
coef = np.corrcoef( X.T )
print( "相関係数は : ", coef  )
print( "分析結果における係数の標準誤差が大きくなる\nt値が小さくなる\n決定係数が大きな値となる\n回帰係数の符号が本来なるべきものとは逆の符号となる" )

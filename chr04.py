#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np


LOANAPP_dataset = lib.load( filename="LOANAPP.csv" )
explanatories = ["const","white"]
explained = ["approve"]

#####各変数を定義#####
X = lib.df2mat( df=LOANAPP_dataset , columns=explanatories )
Y = lib.df2mat( df=LOANAPP_dataset , columns=explained )

print( "大問4.1の回答" )
print( "係数が正になる" )

print( "大問4.2の回答" )
X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )
lib.add_suffix( b )

t = lib.t( X=X , Y=Y , beta=b )[0]
print( "t値 :", t )
print( "1%有意で" , round( b[1] , 3  ) )
print( "未回答" )

print( "大問4.3の回答" )
#ここに回答プログラムを記載する
explanatories = ["const","white","hrat","obrat","loanprc","unem","male","married","dep","sch","cosign","chist","pubrec","mortlat1","mortlat2","vr"]
explained = ["approve"]

#####各変数を定義#####
X = lib.df2mat( df=LOANAPP_dataset , columns=explanatories )
Y = lib.df2mat( df=LOANAPP_dataset , columns=explained )

X_tX = np.dot( X.T , X )
X_tY = np.dot( X.T , Y )
b = np.dot( np.linalg.inv( X_tX ) , X_tY )
t = lib.t( X=X , Y=Y , beta=b )[0]
print( "t値 :", t )
lib.add_suffix( b )
print( "依然として差別は存在する" )

print( "大問4.4の回答" )
#ここに回答プログラムを記載する

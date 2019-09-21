#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
3 Multiple Regression
"""
lib.title("#############3 Multiple Regression#############")
#####データを読み取る#####
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["const","lsales","lmktval"]
explained = ["lsalary"]

"""
3-1の解答
"""
lib.chaper( "大問3.1の回答" )
X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
Y = lib.df2mat( df=CEOSAL2_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( coefs=b , labels=explanatories )
print("\n")

"""
3-2の解答
"""
lib.chaper( "大問3.2の回答" )
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["const","lsales","lmktval","profits"]
explained = ["lsalary"]

X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
Y = lib.df2mat( df=CEOSAL2_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( coefs=b , labels=explanatories )
print( "真数条件を満たさないためと答えたいところであるが、回帰パラメータの値が正であることから解答不能" )
print("\n")

"""
3-3の解答
"""
lib.chaper( "大問3.3の回答" )

#####データを読み取る#####
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["const","lsales","lmktval","profits","ceoten"]
explained = ["lsalary"]

#####説明変数を定義#####
X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
Y = lib.df2mat( df=CEOSAL2_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )

#####解答#####
print( str( 0.01168 * 100 ) , "%" )
print("\n")

"""
3-4の解答
"""
lib.chaper( "大問3.4の回答" )
#####データを読み取る#####
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["profits","lmktval"]

#####説明変数を定義#####
X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
coef = np.corrcoef( X.T )

#####解答#####
print( "相関係数は : ", coef  )
print( "分析結果における係数の標準誤差が大きくなる\nt値が小さくなる\n決定係数が大きな値となる\n回帰係数の符号が本来なるべきものとは逆の符号となる" )
print("\n")

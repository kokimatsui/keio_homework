#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
8 Instrumental Variable And 2SLS
"""
lib.title("#############8 Instrumental Variable And 2SLS#############")

FERTIL2_dataset = lib.load( filename="FERTIL2.csv" )
FERTIL2_dataset = lib.cross_var( df=FERTIL2_dataset , var1="age" , var2="age" )

"""
8-1の解答
"""
lib.chaper("<8.1の解答>")
#####説明変数を定義#####
explanatories = ["const","educ","age","age*age"]
explained = ["children"]

X = lib.df2mat( df=FERTIL2_dataset , columns=explanatories )
Y = lib.df2mat( df=FERTIL2_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( coefs=b , labels=explanatories )
const , educ , age , age_aqure = b[0] , b[1] , b[2] , b[3]
y = educ * 100

print( y )
print( "9人減る" )

print("\n")

"""
8-2の解答
"""
lib.chaper("<8.2の解答>")
#####説明変数を定義#####
explanatories = ["const","frsthalf"]
explained = ["educ"]

X = lib.df2mat( df=FERTIL2_dataset , columns=explanatories )
Y = lib.df2mat( df=FERTIL2_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
t = lib.t_v2( X=X , Y=Y , beta=b )
lib.add_suffix( coefs=t , labels=explanatories )
lib.add_suffix( coefs=b , labels=explanatories )
print( "有意性があるから、相関が強いとみてIVとして不適" )
print("\n")

"""
8-3の解答
"""
lib.chaper("<8.3の解答>")
print( "IVでは、educの係数が大きくなり、educの出生への影響が高いということがわかる" )
print("\n")

"""
8-4の解答
"""
lib.not_done("<8.4の解答>")
#####説明変数を定義#####
explanatories = ["const","educ","age","age*age","frsthalf","electric","tv","bicycle"]
explained = ["children"]
FERTIL2_dataset = lib.rm( df=FERTIL2_dataset , cols=explanatories , string="." )
X = lib.df2mat( df=FERTIL2_dataset , columns=explanatories )
Y = lib.df2mat( df=FERTIL2_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( coefs=b , labels=explanatories )
print( "後ほど確認" )

print()
print("\n")

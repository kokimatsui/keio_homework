#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
7 Panel Data
"""
lib.title("#############7 Panel Data#############")

grunfeld_dataset = lib.load( filename="grunfeld.csv" )

"""
7-1の解答
"""
lib.chaper("<7.1の解答>")
explanatories = ["const","value","capital"]
explained = ["invest"]

#B = lib.random_effect( df=grunfeld_dataset , group="year" , X_cols=explanatories , Y_cols=explained )
X = lib.df2mat( df=grunfeld_dataset , columns=explanatories )
Y = lib.df2mat( df=grunfeld_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
print("提出の時は、βにちゃんと係数をいれましょう ")
lib.add_suffix( coefs=b , labels=explanatories )
print("\n")

"""
7-2の解答
"""
lib.not_done ("<7.2の解答>")
print( "土屋くんに聞く" )
firms = list( set( list( grunfeld_dataset["firm"] ) ) )

for i in range( len( firms ) ):
    print(firms[i])
    this = "hetero"+str(i)
    hetero = lib.replace(df=grunfeld_dataset["firm"],frm=firms[i],to=1)
    grunfeld_dataset = lib.add_col( df=grunfeld_dataset , col=this , val=hetero )
    explanatories = ["const","value","capital",this]
    explained = ["invest"]
    X = lib.df2mat( df=grunfeld_dataset , columns=explanatories )
    Y = lib.df2mat( df=grunfeld_dataset , columns=explained )
    b = lib.reg( X=X , Y=Y )
    lib.add_suffix( coefs=b , labels=explanatories )
    print("\n")

"""
7-3の解答
"""
lib.not_done("<7.3の解答>")
print( "土屋くんに聞く" ) 
print("\n")

"""
7-4の解答
"""
lib.title("<7.4の解答>")
print("\n")

"""
7-5の解答
"""
lib.title("<7.5の解答>")
print("\n")

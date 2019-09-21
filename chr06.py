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
grouped_firm = lib.grouping( df=grunfeld_dataset , name="firm" )
grouped_year = lib.grouping( df=grunfeld_dataset , name="year" )
explanatories = ["const","value","capital"]
explained = ["invest"]

#B = lib.random_effect( df=grunfeld_dataset , group="year" , X_cols=explanatories , Y_cols=explained )
X = lib.df2mat( df=grunfeld_dataset , columns=explanatories )
Y = lib.df2mat( df=grunfeld_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( coefs=b , labels=explanatories )
print("\n")

"""
7-2の解答
"""
lib.not_done("<7.2の解答>")
print("\n")

"""
7-3の解答
"""
lib.not_done("<7.3の解答>")
print("\n")

"""
7-4の解答
"""
lib.not_done("<7.4の解答>")
print("\n")

"""
7-5の解答
"""
lib.not_done("<7.5の解答>")
print("\n")

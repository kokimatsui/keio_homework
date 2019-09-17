#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
2 Simple Regression
"""

CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["salary"]
explained = ["lsalary"]

#####各変数を定義#####
X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )

"""
2-1の解答
"""
print( "<大問2.1の回答>" )
print( "Salaryの平均値 :" , round( np.average( X ) , 3  ) )
print("\n")

"""
2-2の解答
"""
print( "<大問2.2の回答>" )
ceoten = CEOSAL2_dataset[ CEOSAL2_dataset["ceoten"] <=0  ]
print( "CEOの在任期間が0の人の数 :", len( ceoten ) )
print("\n")

"""
2-3の解答
"""
print( "<大問2.3の回答>" )
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["const","ceoten"]
explained = ["lsalary"]

X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
Y = lib.df2mat( df=CEOSAL2_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( b )
print("\n")

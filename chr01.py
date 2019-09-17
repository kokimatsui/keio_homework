#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np

CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["salary"]
explained = ["lsalary"]

#####各変数を定義#####
X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )


print( "<大問2.1の回答>" )
#ここに回答プログラムを記載する
print( "Salaryの平均値 :" , round( np.average( X ) , 3  ) )
print("\n")

print( "<大問2.2の回答>" )
#ここに回答プログラムを記載する
ceoten = CEOSAL2_dataset[ CEOSAL2_dataset["ceoten"] <=0  ]
print( "CEOの在任期間が0の人の数 :", len( ceoten ) )
print("\n")

print( "<大問2.3の回答>" )
#ここに回答プログラムを記載する
CEOSAL2_dataset = lib.load( filename="CEOSAL2.csv" )
explanatories = ["const","ceoten"]
explained = ["lsalary"]

X = lib.df2mat( df=CEOSAL2_dataset , columns=explanatories )
Y = lib.df2mat( df=CEOSAL2_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( b )

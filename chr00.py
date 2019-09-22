#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
1 Matrix Calculus
"""
lib.title("#############1 Matrix Calculus#############")
#####データを読み取る#####
artifical_dataset = lib.load( filename="artificial.csv" )
explanatories = ["x1" ,"x2"]
explained = ["y"]

#####各変数を定義#####
X = lib.df2mat( df=artifical_dataset , columns=explanatories )
Y = lib.df2mat( df=artifical_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )


"""
1-1の解答
"""
lib.chaper( "<大問1.1の回答>" )

#####解答#####
lib.add_suffix( b )
print("\n")

"""
1-2の解答
"""
lib.chaper( "<大問1.2の回答>" )

#####各変数を定義#####
t = lib.t( X=X , Y=Y , beta=b )[0]
print( "t value :" , t )
print( "自由度998で、2.581を基準にしたところ 2.581 <" , t , "なので、1%水準でβ0 = 0は棄却される" )
print("\n")

"""
1-3の解答
"""
lib.chaper( "<大問1.3の回答>" )

#####各変数を定義#####
artifical_dataset = lib.load( filename="artificial.csv" )
explanatories = ["const","x1","x2","x3"]
explained = ["y"]

X = lib.df2mat( df=artifical_dataset , columns=explanatories )
Y = lib.df2mat( df=artifical_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( b )
print("\n")

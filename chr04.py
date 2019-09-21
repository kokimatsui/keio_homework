#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
5 Inference
"""
lib.title("#############5 Inference#############")
VOTE_dataset = lib.load( filename="VOTE1.csv" )

"""
5-1の解答
"""
lib.chaper("<5.1の解答>")
print("expendAが1%上がると、voteAがβ1だけ上昇する")
print("\n")

"""
5-2の解答
"""
lib.chaper("<5.2の解答>")
print( "β1 - β2 = 0" )
print("\n")

"""
5-3の解答
"""
lib.chaper("<5.3の解答>")
#####説明変数を定義#####
explanatories = ["const","lexpendA","lexpendB","prtystrA"]
explained = ["voteA"]

X = lib.df2mat( df=VOTE_dataset , columns=explanatories )
Y = lib.df2mat( df=VOTE_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
t_expendA = lib.t( X=X , Y=Y , beta=b )[1]

lib.add_suffix( coefs=b , labels=explanatories )
print( "Aの支出は" + str( b[1] ) + "であり、t値が" +\
 str( round( t_expendA , 3 ) ) + "であり1%有意であることから、結果に大きな影響を与えると言える" )

print("\n")


"""
5-4の解答
"""
lib.not_done("<5.4の解答>")
t = lib.t( X=X , Y=Y , beta=b , beta_01=b[2] )
print( t )
sys.exit()
print("\n")

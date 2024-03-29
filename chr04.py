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
print("expendAが1%上がると、voteAが100分のβ1だけ上昇する")
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
print( "Aの支出は、正に、Bの支出は負に影響を与えている" )
print( "Aの支出は" + str( b[1] ) + "であり、t値が" +\
 str( round( t_expendA , 3 ) ) + "であり1%有意であることから、結果に大きな影響を与えると言える" )

print( "利用はできるが、係数が逆なのでイコールとして採択はできない" )

print("\n")


"""
5-4の解答
"""
lib.not_done("<5.4の解答>")
lexA = lib.df2mat( df=VOTE_dataset , columns=["lexpendA"] )
lexB = lib.df2mat( df=VOTE_dataset , columns=["lexpendB"] )
offset = lexA + lexB
explanatories = ["const","col"]
explained = ["voteA"]
VOTE_dataset = lib.df_assign( df=VOTE_dataset , col="offset" , val=offset )
X = lib.df2mat( df=VOTE_dataset , columns=explanatories )
Y = lib.df2mat( df=VOTE_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
t = lib.t_v2( X=X , Y=Y , beta=b )
lib.add_suffix( coefs=t , labels=explanatories )
print('保留')
print( "AもBも、1%有意で効果がある " )
print("\n")

#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
6 Inference2
"""
lib.title("#############6 Inference2#############")
#####データを読み取る#####
HPRICE_dataset = lib.load( filename="HPRICE1.csv" )
explanatories = ["const","sqrft","bdrms"]
explained = ["lprice"]

#####各変数を定義#####
X = lib.df2mat( df=HPRICE_dataset , columns=explanatories )
Y = lib.df2mat( df=HPRICE_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )

"""
6-1の解答
"""
lib.chaper("<6.1の解答>")
#####解答#####
lib.add_suffix( b , labels=explanatories )
print("\n")

"""
6-2の解答
"""
lib.chaper("<6.2の解答>")
#####回帰係数の取得#####
const , sqrft , bdrms = b[0] , b[1] , b[2]
y_bdrms = bdrms

#####解答#####
print( "bdrmsの数が1単位上がると、priceは" + str( round( y_bdrms , 4 ) ) + "%上がる" )
print("\n")


"""
6-3の解答
"""
lib.chaper("<6.3の解答>")
#####回帰係数の取得#####
const , sqrft , bdrms = b[0] , b[1] , b[2]
y_sqrft = 140 * sqrft
print( "bedroomが1増えた場合は" + str( round( y_bdrms , 4 ) ) + "%の伸び率だったのに対し、\
y_sqrftが140増えた場合は" + str( round(  y_sqrft , 4 ) ) + "%の伸び率だった" )
print( "両者とも間取りは同じであるはずなのに、約2倍の結果の差が見られた" )
print("\n")

"""
6-4の解答
"""
lib.not_done("<6.4の解答>")
print("未解答")
print("\n")

"""
6-5の解答
"""
lib.chaper("<6.5の解答>")
y_pred = 2438 * sqrft + 4 * bdrms + const
print( "sqrftが2438で、bdrmsが4のとき、物件価値は" + str( y_pred ) + "と推計される " )
print("\n")

"""
6-6の解答
"""
lib.chaper("<6.6の解答>")
y_teach = 300000
residual = np.abs( y_teach - np.exp( y_pred ) )
print( str( round( residual , 3 ) ) + "円分overpayしている " )
print("\n")

"""
6-7の解答
"""
lib.not_done("<6.7の解答>")
print("\n")

"""
6-8の解答
"""
lib.not_done("<6.8の解答>")
print("\n")

"""
6-9の解答
"""
lib.not_done("<6.9の解答>")
print("\n")

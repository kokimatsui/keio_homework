#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
6 Inference2
"""

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
lib.add_suffix( b , labels=explanatories )

"""
6-2の解答
"""
bdrms = b[2]
y = bdrms
print( "bdrmsの数が1単位上がると、priceは" + str(round( y , 4 )) + "%上がる" )


"""
6-3の解答
"""


"""
6-4の解答
"""

"""
6-5の解答
"""

"""
6-6の解答
"""

"""
6-7の解答
"""

"""
6-8の解答
"""

"""
6-9の解答
"""

#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np
"""
4 Multiple Regression
"""
print("#############4 Multiple Regression#############")
LOANAPP_dataset = lib.load( filename="LOANAPP.csv" )
explanatories = ["const","white"]
explained = ["approve"]

#####各変数を定義#####
X = lib.df2mat( df=LOANAPP_dataset , columns=explanatories )
Y = lib.df2mat( df=LOANAPP_dataset , columns=explained )

"""
4-1の解答
"""
print( "大問4.1の回答" )
print( "係数が正の状態で、統計的に有意な値をとる" )
print("\n")

"""
4-2の解答
"""
print( "大問4.2の回答" )
b = lib.reg( X=X , Y=Y )
lib.add_suffix( b )
t = lib.t( X=X , Y=Y , beta=b )[0]
print( "t値 :", t )
print( "1%有意で" , round( b[1] , 3  ) )
print( "大きい" )
print("\n")

"""
4-3の解答
"""
print( "大問4.3の回答" )
#####説明変数を定義#####
explanatories = ["const","white","hrat","obrat","loanprc","unem","male","married","dep","sch","cosign","chist","pubrec","mortlat1","mortlat2","vr"]
explained = ["approve"]

#####各変数を定義#####
X = lib.df2mat( df=LOANAPP_dataset , columns=explanatories )
Y = lib.df2mat( df=LOANAPP_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
t = lib.t( X=X , Y=Y , beta=b )[1]

#####解答#####
print( "t値の1%水準" , lib.t_level( free=( X.shape[0] - len( b ) ) , level=1 ) )
print( "t値 :", t )
print( "whiteの値が" + str( round( b[1] , 3 ) ) + "であり、統計的に1%有意であることから依然として差別は存在する" )
print("\n")

"""
4-4の解答
"""
print( "大問4.4の回答" )
#####説明変数を定義#####
LOANAPP_dataset = lib.cross_var( df=LOANAPP_dataset , var1="white" , var2="obrat" )
explanatories = ["const","white*obrat","white","hrat","obrat","loanprc","unem","male","married","dep","sch","cosign","chist","pubrec","mortlat1","mortlat2","vr"]
explained = ["approve"]

#####各変数を定義#####
X = lib.df2mat( df=LOANAPP_dataset , columns=explanatories )
Y = lib.df2mat( df=LOANAPP_dataset , columns=explained )
b = lib.reg( X=X , Y=Y )
t = lib.t( X=X , Y=Y , beta=b )[1]

#####解答#####
print( "t値の1%水準" , lib.t_level( free=( X.shape[0] - len( b ) ) , level=1 ) )
print( "t値 :", t )
print( "obratとwhiteの交差項は1%で統計的に有意" )
print("\n")

"""
4-5の解答
"""
print( "大問4.5の回答" )
#####回帰式を定義#####
const , a = b[0] ,b[4]
y = a * 32 + const

#####各変数を定義#####
obrat = lib.df2mat( df=LOANAPP_dataset , columns=["obrat"] )
obrat_bar = np.average( obrat )
inter = lib.conf_inter( beta=a , t=lib.t( X=X , Y=Y , beta=b )[4] , free=( X.shape[0] - len( b ) - 1  ) , se=lib.std_error( X=X , Y=Y , beta=b ) )

#####解答#####
print( "obratの値が32のときyの値は" , y , "なので、承認されていない" )
print( "32は、だいたいobratの標本平均である" + str( round( obrat_bar , 3 ) ) + "と近い" )
print( a )
print( inter )
print( "Obtain a 95% confidence interval for this effectはまだ答えていない" )


print("\n")

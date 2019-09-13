#!-*-coding:utf-8-*-
import lib
import sys
import numpy as np

#####データを読み取る#####
grunfeld_dataset = lib.load( filename="grunfeld.csv" )
explanatories = ["value","capital"]
explained = ["invest"]

FERTIL2_dataset = lib.load( filename="FERTIL2.RAW" )

#####各変数を定義#####
X = lib.df2mat( df=grunfeld_dataset , columns=explanatories )
Y = lib.df2mat( df=grunfeld_dataset , columns=explained )


print( "大問2.1の回答" )
#ここに回答プログラムを記載する


print( "大問2.2の回答" )
#ここに回答プログラムを記載する

print( "大問2.3の回答" )
#ここに回答プログラムを記載する

print( "大問2.4の回答" )
#ここに回答プログラムを記載する

print( "大問2.5の回答" )
#ここに回答プログラムを記載する

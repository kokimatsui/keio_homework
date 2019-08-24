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

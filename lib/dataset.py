#!-*-coding:utf-8-*-
import os
import sys
import numpy as np
import pandas as pd
__all__ = ["load","df2mat","cross_var","grouping","rm"]

datasetpath = os.path.dirname( os.path.abspath(__file__) ) + "/../dataset/"

def load( filename ):
    """
    CSVを読み込んでDataframeに変換する
    """
    root, ext = os.path.splitext( filename )
    file = datasetpath + filename

    if ext == ".csv":
        print( "CSV file detected" )
        df = pd.read_csv( file )

    elif ext == ".RAW":
        print( "RAW file detected" )
        df = _raw2csv( root=root , file=file )

    else:
        print( "Unknown format" )
        sys.exit()


    return df



def rm( df , cols , string ):
    """
    stringに指定された不正文字列をdataframeから除去する
    """
    rems = []
    if "const" in cols: cols.remove( "const" )
    for i in range( len( df ) ):
        for col in cols:
            if df.ix[i,col] == string and i not in rems:
                rems.append( i )

    for rm in rems:
        df = df.drop( rm )


    return df


def df2mat( df , columns ):
    """
    Dataframeから特定の列を取得して行列に変換する
    """
    df = df.assign(const=1)
    Y = np.array( df.loc[ : , columns ]  , dtype=np.float64)
    if len( columns ) <= 1:
        Y = Y.T[0]

    return Y



def cross_var( df , var1 , var2 ):
    """
    交差項を作成する
    """
    df[str(var1)+"*"+str(var2)] = df.loc[ : , var1 ] * df.loc[ : , var2 ]

    return df

def grouping( df , name ):
    """
    DataFrame型をnameによってグルーピングする
    """

    return df.groupby(name)


def _raw2csv( root , file ):
    """
    rawファイルをcsvに出力する
    """
    if os.path.exists( datasetpath + root + ".csv" ):
        df = pd.read_csv( file )
    else:
        labels_file = datasetpath + root + ".txt"
        if not os.path.exists( labels_file ):
            print( "Please Generate label file" )
            sys.exit()

        labels_obj = open( labels_file , "r" )
        labels = labels_obj.read()
        labels_obj.close()
        rawdata = open(file, "r")
        raw = rawdata.read()
        raw = raw.split("\n")
        raw_arr = []
        for line in raw:
            tmp = line.strip().split(" ")
            l_in = [x for x in tmp if x]
            if len( l_in ) != 0:
                raw_arr.append( l_in )

        df = pd.DataFrame( np.array( raw_arr ) , columns=labels.split(",") )
        df.to_csv( datasetpath + root + ".csv" )
        rawdata.close()

    return df

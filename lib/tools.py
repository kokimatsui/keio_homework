#!-*-coding:utf-8-*-
__all__ = ["add_suffix"]

def add_suffix( coefs ):
    """
    回帰係数を添え字付きで出力する
    """
    for i in range( len( coefs ) ):
        print( "β " + str(i) + "の値は" + str( round( coefs[i] , 5  ) ) )

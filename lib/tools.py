#!-*-coding:utf-8-*-
__all__ = ["add_suffix"]

def add_suffix( coefs , labels=None ):
    """
    回帰係数を添え字付きで出力する
    """
    for i in range( len( coefs ) ):
        if labels is not None:
            print( str(labels[i]) + "の値は" + str( coefs[i] ) )
        else:
            print( "β " + str(i) + "の値は" + str( coefs[i] ) )

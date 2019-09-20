#!-*-coding:utf-8-*-
from colorama import Fore, Back, Style

__all__ = ["add_suffix","chaper","title","not_done"]

def add_suffix( coefs , labels=None ):
    """
    回帰係数を添え字付きで出力する
    """
    for i in range( len( coefs ) ):
        if labels is not None:
            print( str(labels[i]) + "の値は" + str( coefs[i] ) )
        else:
            print( "β " + str(i) + "の値は" + str( coefs[i] ) )

def title( text ):
    """
    タイトルを出力する
    """
    print( Fore.YELLOW + str( text ) + Style.RESET_ALL )


def chaper( text ):
    """
    章を出力する
    """
    print( Fore.GREEN + str( text ) + Style.RESET_ALL )


def not_done( text ):
    """
    未解答のテキストを赤色で出力
    """
    print( Fore.RED + str( text ) + Style.RESET_ALL )

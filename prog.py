#!-*-coding:utf-8-*-
from colorama import Fore, Back, Style

solved = 25
all = 37

print( Fore.YELLOW + "回答率" + str( round( solved / all , 3 ) * 100  ) + "%" + Style.RESET_ALL )

#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import datenlib


def main():
    print('\x1B[H\x1B[J')
    return_value = db_start()
    return 0 if(return_value == 0) else return_value


def db_start():
    isCES = False
    
    print(f"DATEN database management software\n{datenlib.daten('channel')} | {datenlib.daten('version')}\n")
    while(not isCES):
        DecodeCMD = command_asked()
        result = datenlib.PARSIGN((DecodeCMD.upper()).replace(';', ''))
        print(result if(result != '') else '')

    return 0


def create_blank(linelen, select_name = 0):
    result = ''
    select = select_name + 2 if(select_name != 0) else 2
    
    for loop in range(0, linelen + select):
        result += ' '
    return result


def command_asked():
    
    select = ''
    UserCMD = input(f'{select} ▶▶ ')

    if(UserCMD != ''):
        while(UserCMD[-1] != ';'):
            linelen = create_blank(len(UserCMD), len(select))
            NewLine_input = input(f'{linelen} ↪ ')
            if(NewLine_input != ''):
                UserCMD += ' ' + NewLine_input if(NewLine_input != ';') else NewLine_input
    return UserCMD


if __name__ == "__main__":
    main()

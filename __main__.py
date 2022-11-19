#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import datenlib


global select
select = ''

def main():
    print('\x1B[H\x1B[J')
    return_value = db_start()
    return 0 if(return_value == 0) else return_value


def db_start():
    isCES = False
    
    print(datenlib.dateninfo())
    
    try:
        while(not isCES):
            DecodeCMD = command_asked()
            result = datenlib.PARSIGN((DecodeCMD.upper()))
            print(result if(result != '') else '')
        return 0
    except:
        return -1


def create_blank(linelen, select_name = 0):
    result = ''
    select = select_name + 1 if(select_name != 0) else 1
    
    for loop in range(0, linelen + select):
        result += ' '
    return result


def command_asked():
    
    global select
    UserCMD = input(f'{select} ▶ ')

    if(UserCMD != ''):
        while(UserCMD[-1] != ';'):
            linelen = create_blank(len(UserCMD), len(select))
            NewLine_input = input(f'{linelen} ↪ ')
            if(NewLine_input != ''):
                UserCMD += ' ' + NewLine_input if(NewLine_input != ';') else NewLine_input
    return UserCMD


if __name__ == "__main__":
    main()
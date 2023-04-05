#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import RichSupport as RS

def S_Warn(command, code):
    Warnlist = {
                'try' : '다음 변경사항은 저장되지 않았습니다!'
    }
    return f'''{RS.line_creater(25)}\n{RS.richtext(f'{command}\n{Warnlist(code)}', 'YELLOW')}\n{RS.line_creater(25)}\n\n'''

def S_Error(command, code):
    return

def S_Unknown(command, code):
    return
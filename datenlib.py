#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import datensupport as dtspt
import __main__ as cr


global now_select
now_select = ''

def daten(value):
    case = {'version' : 'v0.0',
            'channel' : 'Development'}
    return case[value]


def isSemitwo(command):
    splitcommand = command.split(';')
    return False if(len(splitcommand) > 2) else True

def isHELP(command):
    commandlist = command.split(' ')
    return True if('HELP' in commandlist[0]) else False

def isDATA(command):
    commandlist = command.split(' ')
    return True if(commandlist[0] == 'DATA') else False

def isIMPORT(command):
    commandlist = command.split(' ')
    return True if('IMPORT' in commandlist[0]) else False

def isEXPORT(command):
    commandlist = command.split(' ')
    return True if('EXPORT' in commandlist[0]) else False

def isCLEAR(command):
    return True if(command == 'CLEAR') else False

def isINFO(command):
    return True if(command == 'INFO') else False

def isQUIT(command):
    return True if(command == 'QUIT' or command == 'EXIT') else False


def PARSIGN(command):
    result = ''
    
    while(True):
        if(isSemitwo(command)):
            command = command.replace(';', '')
            
            if(isHELP(command)):
                if(command == 'HELP'):
                    print(dtspt.help_str('all'))
                    break
                else:
                    commandlist = command.split(' ')
                    if(commandlist[1] == 'DATA'):
                        print(dtspt.help_str('data'))
                    else:
                        print(dtspt.syntaxerror(command, 'uhl'))
                    break
                
            elif(isDATA(command)):
                commandlist = command.split(' ', 2)
                
                if(len(commandlist) >= 2):
                    if(commandlist[1] == 'CREATE'):
                        if(len(commandlist) >= 3):
                            create_data(commandlist[2])
                        else:
                            result = dtspt.syntaxerror(command, 'dce')
                        break
                    
                    elif(commandlist[1] == 'REMOVE'):
                        if(len(commandlist) >= 3):
                            remove_data(commandlist[2])
                        else:
                            result = dtspt.syntaxerror(command, 'dce')
                        break
                    
                    elif(commandlist[1] == 'LIST'):
                        index = 0
                        get_datalist = datalist()
                        print(f'\n{dtspt.line_creater(10)}[ List of databases ]{dtspt.line_creater(10)}\n')
                        if(len(get_datalist) != 0):
                            for value in get_datalist:
                                index += 1
                                print(f'    [{index}] {value}')
                        else:
                            print(dtspt.richtext('    [!] No databases currently exist.', 'YELLOW'))
                        print(f'\n{dtspt.line_creater(21 + 20)}\n')
                        break
                
                    elif(commandlist[1] == 'SELECT'):
                        if(len(commandlist) >= 3):
                            data_select(commandlist[2])
                        else:
                            result = dtspt.syntaxerror(command, 'dce')
                        break
                    
                    elif(commandlist[1] == 'UNSELECT'):
                        if(not len(commandlist) >= 3):
                            if(now_select != ''):
                                data_unselect()
                            else:
                                result = (dtspt.richtext('[!] Database is not already selected\n', 'YELLOW'))
                        else:
                            result = dtspt.syntaxerror(command, 'apr')
                        break
                    
                    else:
                        print(dtspt.syntaxerror(command, 'ukn'))
                        break
                    
                else:
                    result = dtspt.syntaxerror(command, 'ukn')
                    break
            
            elif(isIMPORT(command)):
                return
            
            elif(isEXPORT(command)):
                commandlist = command.split(' ')
                if(len(commandlist) >= 2):
                    if(commandlist[1] == ''):
                        print(dtspt.syntaxerror(command, 'epe'))
                    else:
                        undername = commandlist[1].replace(' ', '_')
                        if((commandlist[1][len(commandlist[1]) - 1:len(commandlist[1])]) == ''):
                            print(dtspt.syntaxerror(command, 'dbb'))
                        elif(not os.path.isfile(f'{undername}.dt')):
                            print(dtspt.syntaxerror(command, 'ukf'))
                        else:
                            if(len(commandlist) == 3):
                                try:
                                    if('.csv' in commandlist[2]):
                                        print(dtspt.syntaxerror(command, 'nnn'))
                                    else:
                                        if(not os.path.isdir(commandlist[2])):
                                            print(dtspt.syntaxerror(command, 'pua'))
                                        elif('"' in commandlist[2]):
                                            print(dtspt.syntaxerror(command, 'tai'))
                                        else:
                                            export_path = commandlist[2].replace("'", '')
                                            if(os.path.isfile(export_path)):
                                                print(dtspt.syntaxerror(export_path, 'ctu'))
                                            else:
                                                export(undername, export_path)
                                except:
                                    print(dtspt.syntaxerror(command, 'pua'))
                                    
                            elif(len(commandlist) > 3):
                                print(dtspt.syntaxerror(command, 'apr'))
                            elif(len(commandlist) == 2):
                                export(undername)
                            else:
                                print(dtspt.syntaxerror(command, 'cse'))
                else:
                    if(now_select == ''):
                        print(dtspt.syntaxerror(command, 'epe'))
                    else:
                        export(now_select)
                        
                break
            
            elif(isCLEAR(command)):
                print('\x1B[H\x1B[J')
                print(dateninfo())
                break
            
            elif(isINFO(command)):
                print(dateninfo())
                break
            
            elif(isQUIT(command)):
                print(dtspt.richtext('↪ Saving all data currently...', 'GREEN'))
                quit()
                
            elif(command == ''):
                break
            
            else:
                result = dtspt.syntaxerror(command, 'ukn')
                break
        else:
            print(dtspt.syntaxerror(command, 'smt'))
            break
            
    return result


def create_data(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(dtspt.syntaxerror(name, 'des'))
    elif("'" in name or '"' in name):
        print(dtspt.syntaxerror(name, 'afe'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(dtspt.syntaxerror(name, 'den'))
        elif(name == ''):
            print(dtspt.syntaxerror(name, 'dbb'))
        elif(os.path.isfile(f'{undername}.dt')):
            print(dtspt.syntaxerror(name, 'dtu'))
        else:
            returnvalue = file_manage_system('create', undername)
            if(returnvalue):
                print(dtspt.richtext(f'↪ Successfully created a database with \'{undername}\'!', 'GREEN'))
    return None


def data_select(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(dtspt.syntaxerror(name, 'des'))
    elif("'" in name or '"' in name):
        print(dtspt.syntaxerror(name, 'afe'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(dtspt.syntaxerror(name, 'den'))
        elif(name == ''):
            print(dtspt.syntaxerror(name, 'dbb'))
        elif(not os.path.isfile(f'{undername}.dt')):
            print(dtspt.syntaxerror(name, 'ukf'))
        else:
            global now_select
            now_select = undername
            cr.select = now_select
    return None


def data_unselect():
    global now_select
    now_select = ''
    cr.select = now_select
    return None


def remove_data(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(dtspt.syntaxerror(name, 'des'))
    elif("'" in name or '"' in name):
        print(dtspt.syntaxerror(name, 'afe'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(dtspt.syntaxerror(name, 'den'))
        elif(name == ''):
            print(dtspt.syntaxerror(name, 'dbb'))
        elif(not os.path.isfile(f'{undername}.dt')):
            print(dtspt.syntaxerror(name, 'ukf'))
        elif(now_select == undername):
            print(dtspt.syntaxerror(name, 'sfd'))
        else:
            returnvalue = file_manage_system('remove', undername)
            if(returnvalue):
                print(dtspt.richtext(f'↪ Successfully removed the database at \'{undername}\'!', 'GREEN'))
    return None


def datalist():
    return [file for file in os.listdir(os.getcwd()) if file.endswith('.dt')]


def file_manage_system(file_mode, file_name):
    file_path = f'{file_name}.dt'
    
    if(file_mode == 'create'):
        
        try:
            file = open(file_path, mode = 'x', encoding = 'UTF-8')
            file.close()
            return True
        except:
            print(dtspt.syntaxerror(file_name, 'fer'))
            return False
    
    if(file_mode == 'remove'):
        try:
            os.remove(file_path)
            return True
        except:
            print(dtspt.syntaxerror(file_name, 'fre'))
            return False
        
        
def dateninfo():
    return (f"DATEN database management software\n{daten('channel')} | {daten('version')}\n")
        
   
def export(select_db = now_select, sav_path = ''):
    
    if(sav_path == ''):
        sav_path = (f'{select_db}.csv')
    else:
        sav_path = sav_path + (f'/{select_db}.csv')
    
    if(select_db == ''):
        print(dtspt.syntaxerror(':: EXPORT ERROR ::', 'epe'))
    elif(os.path.isfile(sav_path)):
        print(dtspt.syntaxerror(sav_path, 'ctu'))
    else:
        try:
            file = open(f'{sav_path}', mode = 'x', encoding = 'UTF-8')
            file.close()
            print(dtspt.richtext(f'↪ Successfully exported to csv file! ==> \'{sav_path}\'', 'GREEN'))
        except:
            print(dtspt.syntaxerror(sav_path, 'cse'))
        
    return None
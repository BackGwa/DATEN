#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_END = '\033[0m'

def daten(value):
    case = {'version' : 'v0.0',
            'channel' : 'Development'}
    return case[value]

def isHELP(command):
    commandlist = command.split(' ')
    return True if('HELP' in commandlist[0]) else False

def isDATA(command):
    commandlist = command.split(' ')
    return True if(commandlist[0] == 'DATA') else False

def isCLEAR(command):
    return True if(command == 'CLEAR') else False

def isINFO(command):
    return True if(command == 'INFO') else False

def isQUIT(command):
    return True if(command == 'QUIT' or command == 'EXIT') else False

def PARSIGN(command):
    result = ''
    
    while(True):
        if(isHELP(command)):
            if(command == 'HELP'):
                print('''
                    
=============================[ List of DATEN commands ]=============================

    HELP {VALUE}        =>  Outputs all commands.
    DATA {MODE} {VALUE} =>  Database management commands.
    CLEAR               =>  Clears all content on the current screen.
    INFO                =>  Outputs information from the current DATEN software.
    QUIT & EXIT         =>  Shutdown the DATEN software.

====================================================================================

''')
                break
            else:
                commandlist = command.split(' ')
                if(commandlist[1] == 'DATA'):
                    print('''
                          
=============================[ Commands for DATA ]=============================

    CREATE {FILE_NAME}  =>  Create a new database.
    REMOVE {FILE_NAME}  =>  Removes an existing database.

===============================================================================
                          
''')
                else:
                    print(syntaxerror(command, 'uhl'))
                break
            
        elif(isDATA(command)):
            commandlist = command.split(' ', 2)
            
            if(commandlist[1] == 'CREATE'):
                if(len(commandlist) >= 3):
                    create_data(commandlist[2])
                else:
                    result = syntaxerror(command, 'dce')
                break
            
            elif(commandlist[1] == 'REMOVE'):
                if(len(commandlist) >= 3):
                    remove_data(commandlist[2])
                else:
                    result = syntaxerror(command, 'dce')
                break
            else:
                result = syntaxerror(command, 'ukn')
                break
        
        elif(isCLEAR(command)):
            print('\x1B[H\x1B[J')
            break
        
        elif(isINFO(command)):
            print(f"DATEN database management software\n{daten('channel')} | {daten('version')}\n")
            break
        
        elif(isQUIT(command)):
            print(richtext('↪ Saving all data currently...', 'GREEN'))
            quit()
            
        elif(command == ''):
            break
        
        else:
            result = syntaxerror(command, 'ukn')
            break
            
    return result

def create_data(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(syntaxerror(name, 'des'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(syntaxerror(name, 'den'))
        elif(name == ''):
            print(syntaxerror(name, 'dbb'))
        elif(os.path.isfile(f'{undername}.dt')):
            print(syntaxerror(name, 'dtu'))
        else:
            returnvalue = file_manage_system('create', undername)
            if(returnvalue):
                print(richtext(f'↪ Successfully created a database with \'{undername}\'!', 'GREEN'))
    return None

def remove_data(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(syntaxerror(name, 'des'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(syntaxerror(name, 'den'))
        elif(name == ''):
            print(syntaxerror(name, 'dbb'))
        elif(not os.path.isfile(f'{undername}.dt')):
            print(syntaxerror(name, 'ukf'))
        else:
            returnvalue = file_manage_system('remove', undername)
            if(returnvalue):
                print(richtext(f'↪ Successfully removed the database at \'{undername}\'!', 'GREEN'))
    return None

def syntaxerror(command, errcode):
    case = {'ukn' : f'{command}\nThis type of command is not supported!',
            'dce' : f'{command}\nThe name of the database for executing the command is not defined!',
            'des' : f'\'{command}\'\nDatabase name must not contain spaces at the end!',
            'den' : f'\'{command}\'\nThe first character in the database name cannot be a number!',
            'fer' : f'\'{command}\'\nThere was an error creating the following database file!',
            'fre' : f'\'{command}\'\nError removing the following database files!',
            'ukf' : f'\'{command}\'\nThis database file does not exist!',
            'dtu' : f'\'{command}\'\nThis database file already exists!',
            'dbb' : f'It is impossible to leave the database name blank!',
            'uhl' : f'{command}\nThe following help does not exist!'}
    
    return richtext('\n============================================================\n' + '↪ ' + case[errcode] + '\n============================================================', 'RED')

def richtext(text, color):
    if(color == 'RED'):
        return COLOR_RED + text + COLOR_END
    elif(color == 'YELLOW'):
        return COLOR_YELLOW + text + COLOR_END
    elif(color == 'GREEN'):
        return COLOR_GREEN + text + COLOR_END
    
def file_manage_system(file_mode, file_name):
    
    file_path = f'{file_name}.dt'
    
    if(file_mode == 'create'):
        
        try:
            file = open(file_path, mode = 'x', encoding = 'UTF-8')
            file.close()
            return True
        except:
            print(syntaxerror(file_name, 'fer'))
            return False
    
    if(file_mode == 'remove'):
        try:
            os.remove(file_path)
            return True
        except:
            print(syntaxerror(file_name, 'fre'))
            return False
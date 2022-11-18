#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import __main__ as cr

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_END = '\033[0m'


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

def isEXPORT(command):
    return True if(command == 'EXPORT') else False

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
                    print(help_str('all'))
                    break
                else:
                    commandlist = command.split(' ')
                    if(commandlist[1] == 'DATA'):
                        print(help_str('data'))
                    else:
                        print(syntaxerror(command, 'uhl'))
                    break
                
            elif(isDATA(command)):
                commandlist = command.split(' ', 2)
                
                if(len(commandlist) >= 2):
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
                    
                    elif(commandlist[1] == 'LIST'):
                        index = 0
                        get_datalist = datalist()
                        print(f'\n{line_creater(10)}[ List of databases ]{line_creater(10)}\n')
                        if(len(get_datalist) != 0):
                            for value in get_datalist:
                                index += 1
                                print(f'    [{index}] {value}')
                        else:
                            print(richtext('    [!] No databases currently exist.', 'YELLOW'))
                        print(f'\n{line_creater(21 + 20)}\n')
                        break
                
                    elif(commandlist[1] == 'SELECT'):
                        if(len(commandlist) >= 3):
                            data_select(commandlist[2])
                        else:
                            result = syntaxerror(command, 'dce')
                        break
                    
                    elif(commandlist[1] == 'UNSELECT'):
                        if(not len(commandlist) >= 3):
                            if(now_select != ''):
                                data_unselect()
                            else:
                                result = (richtext('[!] Database is not already selected\n', 'YELLOW'))
                        else:
                            result = syntaxerror(command, 'apr')
                        break
                    
                    else:
                        print(syntaxerror(command, 'ukn'))
                        break
                    
                else:
                    result = syntaxerror(command, 'ukn')
                    break
            
            elif(isEXPORT(command)):
                commandlist = command.split(' ')
                if(len(commandlist) > 3):
                    result = syntaxerror(command, 'apr')
                else:
                    if(now_select != ''):
                        export(now_select)
                    else:
                        result = syntaxerror(command, 'epe')
                break
            
            elif(isCLEAR(command)):
                print('\x1B[H\x1B[J')
                print(dateninfo())
                break
            
            elif(isINFO(command)):
                print(dateninfo())
                break
            
            elif(isQUIT(command)):
                print(richtext('↪ Saving all data currently...', 'GREEN'))
                quit()
                
            elif(command == ''):
                break
            
            else:
                result = syntaxerror(command, 'ukn')
                break
        else:
            print(syntaxerror(command, 'smt'))
            break
            
    return result


def create_data(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(syntaxerror(name, 'des'))
    elif("'" in name or '"' in name):
        print(syntaxerror(name, 'afe'))
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


def data_select(name):
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
        print(syntaxerror(name, 'des'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(syntaxerror(name, 'den'))
        elif(name == ''):
            print(syntaxerror(name, 'dbb'))
        elif(not os.path.isfile(f'{undername}.dt')):
            print(syntaxerror(name, 'ukf'))
        elif(now_select == undername):
            print(syntaxerror(name, 'sfd'))
        else:
            returnvalue = file_manage_system('remove', undername)
            if(returnvalue):
                print(richtext(f'↪ Successfully removed the database at \'{undername}\'!', 'GREEN'))
    return None


def datalist():
    return [file for file in os.listdir(os.getcwd()) if file.endswith('.dt')]


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
            'uhl' : f'{command}\nThe following help does not exist!',
            'apr' : f'{command}\nAdditional factor not verified exist! These additional factor are not allowed!',
            'sfd' : f'\'{command}\'\nThe currently selected database cannot be deleted!',
            'afe' : f'{command}\nDatabase name cannot contain quotation marks!',
            'smt' : f'{command}\nYou have used more than one semicolon. These commands are not allowed!',
            'epe' : f'No database defined to export!',
            'ctu' : f'File {command} already exists! The export operation has been canceled to prevent file conflicts!',
            'cse' : f'Error saving file {command}!'}
    
    return richtext(f'{line_creater(60)}\n' + '↪ ' + case[errcode] + f'\n{line_creater(60)}\n', 'RED')


def richtext(text, color):
    if(color == 'RED'):
        return COLOR_RED + text + COLOR_END
    elif(color == 'YELLOW'):
        return COLOR_YELLOW + text + COLOR_END
    elif(color == 'GREEN'):
        return COLOR_GREEN + text + COLOR_END


def line_creater(value):
    result = ''
    for i in range(0, value):
        result += '='
    return result


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
        
        
def dateninfo():
    return (f"DATEN database management software\n{daten('channel')} | {daten('version')}\n")
        
   
def export(select_db, sav_path = f'{now_select}.csv'):
    if(select_db == ''):
        print(syntaxerror(':: EXPORT ERROR ::', 'epe'))
    elif(os.path.isfile(sav_path)):
        print(syntaxerror(sav_path, 'ctu'))
    else:
        try:
            print(richtext(f'↪ Successfully exported to csv file! => \'{now_select}\'', 'GREEN'))
        except:
            print(syntaxerror(sav_path, 'cse'))
        
    return None
        
def help_str(value):
    if(value == 'all'):
        return (f'''
                    
{line_creater(30)}[ List of DATEN commands ]{line_creater(30)}

    HELP    [-VALUE]            =>  Outputs all commands.
    DATA    [OPTION] [VALUE]    =>  Database management commands.
    VIEW    [OPTION]            =>  Displays the contents of the currently selected database.
    EXPORT  [-VALUE] [-VALUE]   =>  Export the database to the csv extension.
    CLEAR                       =>  Clears all content on the current screen.
    INFO                        =>  Outputs information from the current DATEN software.
    QUIT & EXIT                 =>  Shutdown the DATEN software.

{line_creater(26 + 60)}
''')
    elif(value == 'data'):
        return (f'''
                          
{line_creater(30)}[ Commands for DATA ]{line_creater(30)}

    CREATE [FILE_NAME]  =>  Create a new database.
    REMOVE [FILE_NAME]  =>  Removes an existing database.
    SELECT [FILE_NAME]  =>  Select the database.
    UNSELECT            =>  unselect the database.
    LIST                =>  Returns a list of all data.

{line_creater(21 + 60)}
''')
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import RichSupport as RS
import __main__ as cr


# [ 코드 전체 수정을 요구 ]

# [ ]   ==>   문법 오류 검사 기능을 함수화
# [ ]   ==>   문법 오류 시에 출력 메세지도 함수화
# [ ]   ==>   문법 오류 검사 기능 알고리즘 단순화

global now_select
now_select = ''


# [문법 오류] : 세미콜론 2개 이상 사용
def isSemitwo(command):
    splitcommand = command.split(';')
    return False if(len(splitcommand) > 2) else True

# [명령] : HELP
def isHELP(command):
    commandlist = command.split(' ')
    return True if('HELP' in commandlist[0]) else False

# [명령] : DATA
def isDATA(command):
    commandlist = command.split(' ')
    return True if(commandlist[0] == 'DATA') else False

# [명령] : VIEW
def isVIEW(command):
    commandlist = command.split(' ')
    return True if('VIEW' in commandlist[0]) else False

# [명령] : IMPORT
def isIMPORT(command):
    commandlist = command.split(' ')
    return True if('IMPORT' in commandlist[0]) else False

# [명령] : EXPORT
def isEXPORT(command):
    commandlist = command.split(' ')
    return True if('EXPORT' in commandlist[0]) else False

# [명령] : CLEAR
def isCLEAR(command):
    return True if(command == 'CLEAR') else False

# [명령] : INFO
def isINFO(command):
    return True if(command == 'INFO') else False

# [명령] : QUIT & EXIT & DEC
def isQUIT(command):
    return True if(command == 'QUIT' or command == 'EXIT' or command == 'DEC') else False


# [함수] : 명령어 파싱
def PARSIGN(command):
    result = ''
    
    while(True):
        if(isSemitwo(command)):
            command = command.replace(';', '')
            
            if(isHELP(command)):
                if(command == 'HELP'):
                    print(RS.help_command('all'))
                    break
                else:
                    commandlist = command.split(' ')
                    if(commandlist[1] == 'DATA'):
                        print(RS.help_command('data'))
                    else:
                        print(RS.syntaxerror(command, 'uhl'))
                    break
                
            elif(isDATA(command)):
                commandlist = command.split(' ', 2)
                
                if(len(commandlist) >= 2):
                    if(commandlist[1] == 'CREATE'):
                        if(len(commandlist) >= 3):
                            create_data(commandlist[2])
                        else:
                            result = RS.syntaxerror(command, 'dce')
                        break
                    
                    elif(commandlist[1] == 'REMOVE'):
                        if(len(commandlist) >= 3):
                            remove_data(commandlist[2])
                        else:
                            result = RS.syntaxerror(command, 'dce')
                        break
                    
                    elif(commandlist[1] == 'LIST'):
                        index = 0
                        get_datalist = datalist()
                        print(f'\n{RS.line_creater(10)}[ List of databases ]{RS.line_creater(10)}\n')
                        if(len(get_datalist) != 0):
                            for value in get_datalist:
                                index += 1
                                print(f'    [{index}] {value}')
                        else:
                            print(RS.richtext('    [!] No databases currently exist.', 'YELLOW'))
                        print(f'\n{RS.line_creater(21 + 20)}\n')
                        break
                
                    elif(commandlist[1] == 'SELECT'):
                        if(len(commandlist) >= 3):
                            data_select(commandlist[2])
                        else:
                            result = RS.syntaxerror(command, 'dce')
                        break
                    
                    elif(commandlist[1] == 'UNSELECT'):
                        if(not len(commandlist) >= 3):
                            if(now_select != ''):
                                data_unselect()
                            else:
                                result = (RS.richtext('[!] Database is not already selected\n', 'YELLOW'))
                        else:
                            result = RS.syntaxerror(command, 'apr')
                        break
                    
                    else:
                        print(RS.syntaxerror(command, 'ukn'))
                        break
                    
                else:
                    result = RS.syntaxerror(command, 'ukn')
                    break
            
            elif(isVIEW(command)):
                return
            
            elif(isIMPORT(command)):
                commandlist = command.split(' ')
                commandlist[1] = commandlist[1].replace("'", '')
                
                if('"' in commandlist[1]):
                    print(RS.syntaxerror(command, 'tai'))
                    break
                
                if(len(commandlist) == 2 and (not os.path.isfile(commandlist[1]))):
                    print(RS.syntaxerror(command, 'icv'))
                    break

                if(len(commandlist) >= 2):
                    try:
                        filename = os.path.splitext(os.path.basename(commandlist[1]).replace(' ', '_'))[0]
                    except:
                        print(RS.syntaxerror(command, 'ifd'))
                        break
                    
                    if(len(commandlist) == 2 and now_select == ''):
                        if(os.path.isfile((os.path.basename(filename + '.dt')))):
                            print(RS.richtext('A database with the following name exists.\nDo you want to combine the database with the current file?\n\n', 'YELLOW'))
                            userchoice = input('[Selection Mode]\n(Y / N) ▶▶ ')
                            
                            if(userchoice.lower() == 'y'):
                                print(RS.richtext('Database merged successfully.', 'GREEN'))
                            elif(userchoice.lower() == 'n'):
                                print(RS.richtext('Operation cancelled!', 'YELLOW'))
                            else:
                                print(RS.richtext('The command was canceled because an invalid option was selected!', 'YELLOW'))
                                break
                        else:
                            print(RS.richtext('You have created a new database with the name of the imported file!', 'GREEN'))
                            file_manage_system('create', os.path.basename(filename))
                    else:
                        try:              
                            if(len(commandlist) == 3 and (not os.path.isfile(commandlist[2]))):
                                print(RS.syntaxerror(command, 'dnc'))
                                break
                            
                            elif(len(commandlist) > 3):
                                print(RS.syntaxerror(command, 'apr'))
                                break
                                
                        except:
                            print(RS.syntaxerror(command, 'exp'))
                            break
                else:
                    print(RS.syntaxerror(command, 'epi'))
                    break
                    
                return result
            
            elif(isEXPORT(command)):
                commandlist = command.split(' ')
                if(len(commandlist) >= 2):
                    if(commandlist[1] == ''):
                        print(RS.syntaxerror(command, 'epe'))
                    else:
                        undername = commandlist[1].replace(' ', '_')
                        if((commandlist[1][len(commandlist[1]) - 1:len(commandlist[1])]) == ''):
                            print(RS.syntaxerror(command, 'dbb'))
                        elif(not os.path.isfile(f'{undername}.dt')):
                            print(RS.syntaxerror(command, 'ukf'))
                        else:
                            if(len(commandlist) == 3):
                                try:
                                    if(os.path.splitext(commandlist[2])[-1] == '.csv'):
                                        print(RS.syntaxerror(command, 'nnn'))
                                    else:
                                        if(not os.path.isdir(commandlist[2])):
                                            print(RS.syntaxerror(command, 'pua'))
                                        elif('"' in commandlist[2]):
                                            print(RS.syntaxerror(command, 'tai'))
                                        else:
                                            export_path = commandlist[2].replace("'", '')
                                            if(os.path.isfile(export_path)):
                                                print(RS.syntaxerror(export_path, 'ctu'))
                                            else:
                                                export(undername, export_path)
                                except:
                                    print(RS.syntaxerror(command, 'pua'))
                                    
                            elif(len(commandlist) > 3):
                                print(RS.syntaxerror(command, 'apr'))
                            elif(len(commandlist) == 2):
                                export(undername)
                            else:
                                print(RS.syntaxerror(command, 'cse'))
                else:
                    if(now_select == ''):
                        print(RS.syntaxerror(command, 'epe'))
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
                print(RS.richtext('↪ Saving all data currently...', 'GREEN'))
                quit()
                
            elif(command == ''):
                break
            
            else:
                result = RS.syntaxerror(command, 'ukn')
                break
        else:
            print(RS.syntaxerror(command, 'smt'))
            break
            
    return result


# [함수] : 데이터베이스 생성
def create_data(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(RS.syntaxerror(name, 'des'))
    elif("'" in name or '"' in name):
        print(RS.syntaxerror(name, 'afe'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(RS.syntaxerror(name, 'den'))
        elif(name == ''):
            print(RS.syntaxerror(name, 'dbb'))
        elif(os.path.isfile(f'{undername}.dt')):
            print(RS.syntaxerror(name, 'dtu'))
        else:
            returnvalue = file_manage_system('create', undername)
            if(returnvalue):
                print(RS.richtext(f'↪ Successfully created a database with \'{undername}\'!', 'GREEN'))
    return None

# [함수] : 데이터베이스 선택
def data_select(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(RS.syntaxerror(name, 'des'))
    elif("'" in name or '"' in name):
        print(RS.syntaxerror(name, 'afe'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(RS.syntaxerror(name, 'den'))
        elif(name == ''):
            print(RS.syntaxerror(name, 'dbb'))
        elif(not os.path.isfile(f'{undername}.dt')):
            print(RS.syntaxerror(name, 'ukf'))
        else:
            global now_select
            now_select = undername
            cr.select = now_select
    return None

# [함수] : 데이터베이스 선택 취소
def data_unselect():
    global now_select
    now_select = ''
    cr.select = now_select
    return None

# [함수] : 데이터베이스 제거
def remove_data(name):
    if((name[len(name)-1:len(name)] == ' ')):
        print(RS.syntaxerror(name, 'des'))
    elif("'" in name or '"' in name):
        print(RS.syntaxerror(name, 'afe'))
    else:
        undername = name.replace(' ', '_')
        if(name[0:1].isdigit()):
            print(RS.syntaxerror(name, 'den'))
        elif(name == ''):
            print(RS.syntaxerror(name, 'dbb'))
        elif(not os.path.isfile(f'{undername}.dt')):
            print(RS.syntaxerror(name, 'ukf'))
        elif(now_select == undername):
            print(RS.syntaxerror(name, 'sfd'))
        else:
            returnvalue = file_manage_system('remove', undername)
            if(returnvalue):
                print(RS.richtext(f'↪ Successfully removed the database at \'{undername}\'!', 'GREEN'))
    return None

# [함수] : 데이터베이스 리스트 보여주기
def datalist():
    return [file for file in os.listdir(os.getcwd()) if file.endswith('.dt')]

# [함수] : 파일 관리
def file_manage_system(file_mode, file_name):
    file_path = f'{file_name}.dt'
    
    if(file_mode == 'create'):
        
        try:
            file = open(file_path, mode = 'x', encoding = 'UTF-8')
            file.close()
            return True
        except:
            print(RS.syntaxerror(file_name, 'fer'))
            return False
    
    if(file_mode == 'remove'):
        try:
            os.remove(file_path)
            return True
        except:
            print(RS.syntaxerror(file_name, 'fre'))
            return False
        
# [함수] : DATEN　정보 출력
def dateninfo():
    return (f"DATEN database management software\n{RS.daten_info('channel')} | {RS.daten_info('version')}\n")
        
# [함수] : 내보내기
def export(select_db = now_select, sav_path = ''):
    
    if(sav_path == ''):
        sav_path = (f'{select_db}.csv')
    else:
        sav_path = sav_path + (f'/{select_db}.csv')
    
    if(select_db == ''):
        print(RS.syntaxerror(':: EXPORT ERROR ::', 'epe'))
    elif(os.path.isfile(sav_path)):
        print(RS.syntaxerror(sav_path, 'ctu'))
    else:
        try:
            file = open(f'{sav_path}', mode = 'x', encoding = 'UTF-8')
            file.close()
            print(RS.richtext(f'↪ Successfully exported to csv file! ==> \'{sav_path}\'', 'GREEN'))
        except:
            print(RS.syntaxerror(sav_path, 'cse'))
        
    return None
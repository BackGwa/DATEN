COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_END = '\033[0m'


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
            'tai' : f'{command}\nDouble quotes are not allowed when enclosing a path name! Please use small quotation marks!',
            'smt' : f'{command}\nYou have used more than one semicolon. These commands are not allowed!',
            'epe' : f'No database defined to export!',
            'ctu' : f'File {command} already exists! The export operation has been canceled to prevent file conflicts!',
            'cse' : f'Error saving file {command}!',
            'pua' : f'{command}\nThe path of the file to be saved is invalid!',
            'nnn' : f'{command}\nEnter directory path only! Paths containing file names are not allowed!'}
    
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


def help_str(value):
    if(value == 'all'):
        return (f'''
                
{line_creater(45)}[ List of DATEN commands ]{line_creater(45)}

                                  {richtext('{ * All DATEN commands require a semicolon! }', 'YELLOW')}

    HELP    [-VALUE]                    =>  Outputs all commands.
    DATA    [OPTION] [VALUE]            =>  Database management commands.
    VIEW    [OPTION]                    =>  Displays the contents of the currently selected database.
    IMPORT  [PATH] [-VALUE] [-OPTION]   =>  Gets the database of the .csv extension. {richtext('{The command is not currently implemented!}', 'RED')}
    EXPORT  [-VALUE] [-PATH]            =>  Export the database to the .csv extension.
    CLEAR                               =>  Clears all content on the current screen.
    INFO    [-VALUE]                    =>  Outputs information from the current DATEN software.
    QUIT & EXIT & DEC                   =>  Shutdown the DATEN software.


{line_creater(26 + 90)}
''')
    elif(value == 'data'):
        return (f'''
                          
{line_creater(30)}[ Commands for DATA ]{line_creater(30)}


    CREATE  [FILE_NAME]     =>  Create a new database.
    REMOVE  [FILE_NAME]     =>  Removes an existing database.
    SELECT  [FILE_NAME]     =>  Select the database.
    UNSELECT                =>  unselect the database.
    LIST                    =>  Returns a list of all data.


{line_creater(21 + 60)}
''')
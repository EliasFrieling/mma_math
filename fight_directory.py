'''
Created on Dec 28, 2018

@author: Elias

this will create a dictionary of every single ufc fighter with their opponents and whether they have won or lost against those opponents
This starts at UFC 1 an goes to UFC Fight Night 83: Cerrone vs. Oliveira which took place on 2/21/16
NOTE: This data is pulled from an excel spreadsheet made by u/geyges on reddit
'''
import xlrd

workbook = xlrd.open_workbook(r'D:\workspace\MMA30-27\MMA30-27\UFCFights2-23-16.xlsx')
worksheet = workbook.sheet_by_index(0)

start_row = 0
end_row = 3570
fighterACol = 9
fighterBCol = 10
fighterA_win_or_loss_col = 11
fighterB_win_or_loss_col = 12

def my_dictionary(fighters):
    """This is the main method that will build up the dictionary. It will start in the designated start row in the excel file
    in this case that row will be the first fight of UFC 31. It will then go to the last row of the file"""
    for start_row in range(end_row):
        fighterA = worksheet.cell(start_row, fighterACol).value
        fighterB = worksheet.cell(start_row, fighterBCol).value
        fighterA_win_or_loss = worksheet.cell(start_row, fighterA_win_or_loss_col).value
        fighterB_win_or_loss = worksheet.cell(start_row, fighterB_win_or_loss_col).value
        #If fighter A is not already in this dictionary this will add them to it, if fighter B is also not in the dictionary it will add them as well
        #If fighter B is in the dictionary it will append fight to their record
        if fighterA not in fighters:
            fighters = add_to_dictionary(fighterA, fighterB, fighterA_win_or_loss, fighters)
            if fighterB not in fighters:
                fighters = add_to_dictionary(fighterB, fighterA, fighterB_win_or_loss, fighters)
            elif fighterB in fighters:
                fighters = add_to_record(fighterB, fighterA, fighterB_win_or_loss, fighters)
        
        elif not is_rematch(fighterA, fighterB, fighters):
            fighters = add_to_record(fighterA, fighterB, fighterA_win_or_loss, fighters)
            if fighterB not in fighters:
                fighters = add_to_dictionary(fighterB, fighterA, fighterB_win_or_loss, fighters)
            else:
                fighters = add_to_record(fighterB, fighterA, fighterB_win_or_loss, fighters)
                   
        elif is_rematch(fighterA, fighterB, fighters):
            fighters = add_rematch_to_dictionary(fighterA, fighterB, fighterA_win_or_loss, fighterB_win_or_loss, fighters)
    
    return fighters
def add_to_dictionary(fighterA, fighterB, fighterA_win_or_loss, fighters):
    """ adds fighterA to the dictionary with the opponent being fighterB"""
    fighters[fighterA] = [[fighterB , [fighterA_win_or_loss]]]
    return fighters

def add_to_record(fighterA, fighterB, fighterA_win_or_loss, fighters):
    """Adds another fight to a fighters record in the dictionary"""
    previous = fighters.pop(fighterA)
    previous.append([fighterB,[fighterA_win_or_loss]])
    fighters[fighterA] = previous
    return fighters

def is_rematch(fighterA, fighterB, fighters):
    """Returns true if fighterA has already fought fighterB"""
    for i in range(len(fighters[fighterA])):
        if fighters[fighterA][i][0] == fighterB:
            return True
    else:
        return False

def add_rematch_to_dictionary(fighterA, fighterB, fighterA_win_or_loss, fighterB_win_or_loss, fighters):
    """ Adds a rematch to the dictionary. For example if fighter A has beaten fighter B twice it will look like
    fight A: [[fighter B] , [win, win]] """
    for i in range(len(fighters[fighterA])):
        if fighters[fighterA][i][0] == fighterB:
            previousA = fighters.pop(fighterA)
            previousA[i][1].append(fighterA_win_or_loss)
            fighters[fighterA] = previousA
        for i in range(len(fighters[fighterB])):
            if fighters[fighterB][i][0] ==fighterA:
                previousB = fighters.pop(fighterB)
                previousB[i][1].append(fighterB_win_or_loss)
                fighters[fighterB] = previousB
    return fighters   
fighters = my_dictionary({})

print(fighters)
        
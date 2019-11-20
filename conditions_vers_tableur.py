
""" 

##
## Name: conditions_vers_tableur.py
## 
## Author: Dr Michael GUEDJ
##
## Description: 
##    Generation of a spreadsheet formula, based on a sequence of conditions,
##    from a text file wrote under a similar aspect that the following:
##           
##        ---------------------text file-------------------
##        Spreadsheet_Condition_1(PARAM): resulting comment
##        Spreadsheet_Condition_2(PARAM): resulting comment
##				...
##        Spreadsheet_Condition_N(PARAM): resulting comment
##        ---------------------end text file---------------
##       
##    "Spreadsheet_Condition_i(PARAM)"
##    means an spreadsheet condition (depending on the parameter PARAM)
##        
##    where PARAM is any string of characters
##    -- typically the reference of a spreadsheet cell.
##    
##    A typical use is the generation of a nested conditions formula.
##    
##
##    Nota Bene: the produced formula follows the French version
##		of the spreadsheet format for formulas.
##    
##	
##	
## Version: 0.1
##
## Date: 04/06/2018 -> 13/11/2019
##
## License: MIT LICENSE 
## -- see the file MIT-LICENSE.txt    
##
##

"""

import re

def run(cell_name, file_name):
    tmp = extract_file(file_name)
    res = generate_formula(tmp, cell_name)
    return res

def extract_file(file_name):
    lst_line = extract_lines(file_name)
    return extract_content(lst_line)

""" return a list of the line of the file file_name """
def extract_lines(file_name):
    lst_line = []
    with open(file_name, "r") as f_in:
        for line in f_in:
            s = line.replace('\n', "")
            lst_line.append(s)
    # remove the empty word in the result
    lst_line = [x for x in lst_line if x != ""]
    return lst_line    

""" returns a list of tuple (a tuple per line), 
consistent with the accepted syntax """
def extract_content(lst_line):
    res=[]    
    for line in lst_line:
        lst = re.split(":", line)
        couple = tuple(lst)
        res.append(couple)
    return res

def generate_formula(lst, note):
    res = ""
    for (x,y) in lst:
        res += "SI("
        res += x
        res += ";"+'"'+y+'";'
    res += '""'
    for i in range(len(lst)):
        res += ")"
    res = res.replace("note", note)
    return "="+res



if __name__ == "__main__":
    file_name = "conditions_1.txt"
    print(run("B4", file_name))

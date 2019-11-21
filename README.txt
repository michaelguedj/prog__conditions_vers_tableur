==============
   README 
==============

 Name: conditions_vers_tableur.py
 
 Author: Dr Michael GUEDJ

 Description: 
    Generation of a spreadsheet formula, based on a sequence of conditions,
    from a text file wrote under a similar aspect that the following:
           
        ---------------------text file-------------------
        Spreadsheet_Condition_1(PARAM): resulting comment
        Spreadsheet_Condition_2(PARAM): resulting comment
				...
        Spreadsheet_Condition_N(PARAM): resulting comment
        ---------------------end text file---------------
       
    "Spreadsheet_Condition_i(PARAM)"
    means an spreadsheet condition (depending on the parameter PARAM)
        
    where PARAM is any string of characters
    -- typically the reference of a spreadsheet cell.
    
    A typical use is the generation of a nested conditions formula.
    

    Nota Bene: the produced formula follows the French version
		of the spreadsheet format for formulas.
    
	
	
 Version: 0.1

 Date: 04/06/2018 -> 13/11/2019

 License: MIT LICENSE 
 -- see the file MIT-LICENSE.txt    





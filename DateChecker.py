#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 12:40:35 2022

@author: eyjicuff

Description: this program detects dates in the format DD/MM/YYYY
"""

import re

"ask for input"
Value = input("Type the date in the format dd/mm/yyyy: ")

"function to get the date and extract day month and year and check if its truthy"
def dateDetection (Value) :
    "Variables definition"
    valid = False
    "define the pattern to look for"
    dateRegex = re.compile(r'(\d\d)\/(\d\d)\/(\d\d\d\d)')
    
    "Start search Process"
    dates = dateRegex.search(Value)
    
    "save day, month and year"
    day = int(dates.group(1))
    month = int(dates.group(2))
    year = int(dates.group(3))
    
    "seek leap years"
    yearByFour = year % 4
    yearByHundred = year % 100 
    yearByFourHundred = year % 400
    
    "print the information gathered"
    print("The day is " + str(day))
    print("the month is " + str(month))
    print("the year is " + str(year))
    
    "Validity check, starting by the year range"
    if year >= 1000 and year <= 2999:
        
        "check for valid months"
        if month > 0 and month < 13:
            
            "check for valid months that have only 30 days"
            if (month == 4 or month == 6 or month == 9 or month == 11) and day < 31:
                valid= True
                
            "chechk for valid feburary"
            elif month == 2:
                
                "if it's not a leap year, shouldn't have more than 28 days"
                if (yearByFour != 0 and yearByHundred != 0 and yearByFourHundred != 0) and day <= 28: 
                    valid= True
                    
                "if it's a leap year, should't have more than 29 days"
                elif (yearByFour == 0 and yearByHundred == 0 and yearByFourHundred == 0) and day <=29: 
                    valid= True
                    
                "otherwise it should not be a valid feburary"
                else:
                    valid = False
                    
            "if any other month has no more than 31 days"
            elif day <= 31:
                valid =True
                
            "if it has, then is not valid"
            else: 
                valid =False
                
        "if the month is not valid"
        else:
            valid = False
            
    "if the year is not valid"
    else:
        valid =False
        
    "output if the date is valid or not"
    if valid == False:
        print("The date is not valid")
    else:
        print("The date is valid")
    
"call the function"
dateDetection(Value)
    
    
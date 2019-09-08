# -*- coding: utf-8 -*-
"""
by ngarcia

Errors and Exceptions Homework:
https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/07-Errors%20and%20Exception%20Handling/02-Errors%20and%20Exceptions%20Homework.ipynb
"""

class ErrorsAndExceptions:       
    
    def ask():
        while True:
            try: 
                q = float(input('provide an integer so I can square it '))
                x = q**2
                print('Thank you, your number is: ', x)
                break
            except TypeError:
                print('please provide an integer or floating point number!')
                continue
            except ValueError:
                print('please provide an integer or floating point number!')
                continue
            
        
            
        
        
    

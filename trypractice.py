# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 00:56:11 2019

@author: Shubh
"""

try:
    f = open('newmock.py')
    #me = su
    #x = 3/0
        

except FileNotFoundError as msg1:
    print(msg1)

except NameError as msg2:
    print(msg2)    

except Exception:
    print('something else went wrong')
    

else:
    
    print('this code is error free')

finally:
    
    print('\nand finally we finished running the whole code')
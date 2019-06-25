# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:01:33 2019

@author: ngarcia
"""
import logging
#Q1
def lesser_of_two_evens(a,b):
    if a%2 != 0 or b%2 != 0:
        return max(a,b)
    else: 
        return min(a,b)

#Q2 
def animal_crackers(text):
    temp_list = []
    text = text.lower()
    for word in text.split(" "):
        temp_list.append(word[0])
    temp_list = list(set(temp_list))
    if len(temp_list) == 1:
        return True
    else:
        return False
        
#Q3
def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or sum([n1,n2]) == 20:
        return True
    else:
        return False
    
#Q4
def old_macdonald(name):
        tmp_list = []
        for num,letter in enumerate(name):
            if num == 0 or num == 3:
                tmp_list.append(letter.upper())
            else:
                tmp_list.append(letter)
            num += 1
        return "".join(tmp_list)
            
#Q5
def master_yoda(text):
    tmp_list = text.split(" ") 
    tmp_list.reverse()
    return " ".join(tmp_list)
        
        
#Q6
def almost_there(n):
    c1 = 100
    c2 = 200
    if abs(c1-n) <= 10 or abs(c2-n) <= 10:
        return True
    else:
        return False
    
#Q7
def has_33(nums):
    tmp_list = []
    for x,num in enumerate(nums):
        if x == 0:
            continue
        elif nums[x-1]==nums[x] and nums[x] == 3:
            tmp_list.append(1)
        else:
            continue
    if len(tmp_list) == 0: 
        return False
    else:
        return True
    
   
#Q8     
def paper_doll(text):   
    try:
        tmp_list = []
        for i,letter in enumerate(text):
            x = 0
            while x<3:
                tmp_list.append(text[i])
                x += 1
        return "".join(tmp_list)
    except TypeError:
            print("Inputs must be string type")
            
#Q9    
def blackjack(a,b,c):
    if a+b+c <= 21:
        return a+b+c
    elif a == 11 or b == 11 or c == 11:        
        if a+b+c-10 <= 21:
            return a+b+c-10
        else:
            return 'BUST'
    else:
        return 'BUST'

#Q10   
def summer_69(arr):
    if len(arr) == 0:
        return 0
    else:
        tmp_list = []
        for ar in arr:
            tmp_list.append(ar)
            if ar >= 6 and ar <= 9:
                tmp_list.remove(ar)
                        
    return sum(tmp_list)

#Q11 -- 007 in a row
def spy_game(nums):
    if len(nums) == 0:
        logging.warning("no items in list")
        return False
    elif len(nums) < 3:
        logging.warning("not enough items in list")
        return False
    else:
        tmp_list = []
        for num in nums:
            if num == 0 or num == 7:
                tmp_list.append(num)
        
        x = len(tmp_list)
        if x < 2:
            return False
        else:
            #with the list of zeros and sevens, iterate through to find 007
            count_0 = 0
            count_7 = 0
            for val in tmp_list:
                
                if val == 0 and count_0 in(0,1):                     
                    #counter is either 1 or 2 at this point
                    count_0 += 1                   
                elif val == 7 and count_0 in(0,1):
                    count_7 += 1   
                    count_0 = 0
                elif val == 7 and count_0 < 2:
                    count_0 = 0
                elif count_0 == 2 and val == 7:
                    return True
                elif count_0 == 2 and val != 7:
                    count_0 += 1
                elif val ==7:
                    return True
            if count_0 >= 2:
                return False
            elif count_7 > 0:
                return False
                
                    
#Q12
def count_primes(num):
    if num < 0:
        logging.error('Negative numbers not allowed')
        return None #returns nothing for negative numbers       
    tmp_list = list(range(3,num+1,2))
    tmp_list.insert(0,2)
    divisor_list = list(range(3,round(num/2),2))
    for div in divisor_list:
        for i,j in enumerate(tmp_list): 
            if j != div and j%div == 0:
                tmp_list.pop(i)
                    
    return len(tmp_list)
        



                
            

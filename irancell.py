from random import randint, randrange, sample
import random
import pandas as pd

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def random_regulatory():
    return random.choice(['0930', '0933', '0935', '0936', '0937', '0938', '0990'])
        
numlist =[]    
for mciNumbers in range(0,1000):
    randnum = (random_regulatory()+ str(random_with_N_digits(7)) )
    numlist.append(randnum)
    print(randnum)

def export(n):	
    num_data = pd.DataFrame(n)
    datatoexcel = pd.ExcelWriter('NumData1.xlsx')
    num_data.to_excel(datatoexcel)
    datatoexcel.save()
    print('DataFrame is written to Excel File successfully.')
    	
export(numlist)


    
    
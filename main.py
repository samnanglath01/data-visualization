import numpy as np
import matplotlib.pyplot as plt
import math
######  Example 1.11 ##########
# load text file
fname = 'Sales_12_20.csv' # comma separated values
data1 = np.loadtxt(fname, delimiter=',', skiprows=1)  #skip first row
#print (data1)
data1=data1.tolist()
listsort = sorted(data1, key=lambda x: x[0])
count =0
total =0
startedYear = 2001.0
list1=[]
list2=[]
list3=[]
for i in listsort :
    if (startedYear!=i[0]):
         mean = total/count
         list1.append(mean)
         list2.append(startedYear)
         list3.append(count)
         print("totall bos chnam: ",startedYear, " is ", total,", mean = ",mean)
         mean=0
         total=0
         count =0
         startedYear=i[0]
    if (startedYear==i[0]):
     total += i[1]
     count+=1
     startedYear=i[0]
mean = total/count
list1.append(mean)
list2.append(startedYear)
list3.append(count)
startedYear=2001.0
print("total bos chnam: ",startedYear, " is ", total,", mean = ",mean)
print(list3)
#find deviation
a=0
summation=0
std= 0
for i in listsort:
     if (startedYear!=i[0]):
       std2 = summation/(list3[a]-1)
       std= math.sqrt(std2)
       print("deviation bos chnm: ",startedYear, " is ",std)
       a+=1
       deviation =0
       summation =0
       std=0
       startedYear=i[0]
     if(startedYear==i[0]):
        deviation= (i[1]-list1[a])**2
        
        summation=+ deviation
        startedYear=i[0]
print("deviation bos chnm: ",startedYear, " is ",std)
        
        
        
       
    
    
        

   
    
        
   
      
        
        

        
        

   
        
    
        

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:34:43 2023

@author: khushbu vora
"""
'''
#python while loop
a=3
while(a>0):
      print(a)
      a-=1
#1.infinte loop
#2.the else statment
a=3
while(a>0):
     print(a)
     a=-1
else:
     print("reached 0")    
#with break:
a=3
while(a>0):
     print(a)
     a-=1
     if a==1: break;
else:
    print("reached 0")    
# single stament while
a=3
while a>0: print(a); a-=1;
'''
#=================================================
#python for loop
'''
for a in range(3):
      print(a)
      
#1.print 1 to 3 
for a in range(3):
       print('\n',a+1)  
       '''
#==================================================       
# range function
#print(list(range(100)))

#print(list(range(2,7))) 
print(list(range(2,12,3)))
print(list(range(12,2,-2)))
print(list(range(12,2)))
print(list(range(2,12,-2)))
print(list(range(12,2,2)))
#====================================================
#similar construct or iterating on list
for a in [1,2,3]:
        print(a)
for i in {1,2,2,3,3,4}:
         print(i)    
for i in'wisdom':
         print(i)
         
list=['Romanian','spanish','gujrati']

for i in range(len(list)):
         print(list[i]) 
for i in range(10):
         print(i)
else: 
     print("Reached else") 
#nested for loops
for i in range(1,6):
      for j in range(i):
          print("*",end='')
      print()
#===============================
i=6
while(i>9):
    j=6
    while(j>i):
        print("*",end='')
        j-=1
    i-=1
    print()
#===============================
#1.break statment
for i in 'break':
      print(i)
      if i=='a': break;
for i in 'break':
      print(i)
      if i=='a': break;
#================================
#2.continue statment
i=0
while(i<8):
     i+=1
     if(i==6): continue
     print(i)
#===================================
i=0
while(i<8):
      if(i==6): continue
      print(i)
      i+=1
#=====================================
for i in 'selfhelp':
         pass
print(i)      
       
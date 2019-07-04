
#Inroduction to itertools

student=['A','B','C']
marks=[10,13,12]    
   
import itertools
for (s,m) in zip(student,marks):
    print(s,m)
print('hi')

customer=['A','B','C']
order=['book','cap','ring']

import itertools
for(c,o) in zip(customer,order):
    print('Hello', c,'your order is:',o)

emp=['Swpnil','Monali','Nikita']
id=[1,2,3]
salary=[35000,28000,30000]

import itertools
for(e,i,s) in zip(emp,id,salary):
    print('Hello',e,'your id is:',i,' and your salary is:',s)

import itertools
for(e,i,s) in zip(emp,id,salary):
    print('Hello ',e,'your id is:',i,'and your new salary is:',s+500)
    
    
for i in range(6):
    print(i)
    
count=0
for i in range(1,6):
    print(i+2)
print('finish')




for num1 in range(3):
    for num2 in range(3):
        print(num1,',',num2)


counter=0
while(counter<12):
    print('Hi')
    print(counter)
    counter=counter+1
print('End of the loop')   
    
total_coupouns=10
coupouns_utilized=0
while(coupouns_utilized<11):
    print('total coupouns is left:'+" "+ str(total_coupouns-coupouns_utilized))
    coupouns_utilized=coupouns_utilized+1
print('No coupons left')


marks=35
if marks<40:
    result='failed'
print(result)

    

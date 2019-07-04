#Conditional statements and list examples

marks=35
if marks<40:
    result='failed'
print(result)

    
marks=45
result= None
if marks<40:
    result='failed'
print(result)

marks=55
result= None
if marks<40:
    result='Failled'
else:
    if marks>=40 and marks<60:
        result='Avrage'
    else:
        result='out performer'
print(result)

marks=55
result=None
if marks<40:
    result='Failled'
elif marks>=40 and marks<60:
    result='Average'
else:
    result('out performer')
print(result)
# list and functions
mylist=[1,2,3,4,5,6,7,8,9,10]

mylist=[1,2,3,4,5,6,7,8,9,10]
type(mylist)

mylist[4:6]


mylist[3:5]
mylist.append(11)

mylist.insert(2,2.5)

mylist.remove(2.5)

mylist
mylist=[1,2,3,4,5,6,7,8,9,10]
mylist.insert(4,4.5)

mylist.remove(4.5)
mylist


mylist.append(20)

mylist
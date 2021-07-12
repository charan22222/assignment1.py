#Data types

#Lists

thislist = ["apple","banana","mango"]
print(thislist)

#negative indexing
thislist = ["apple","banana","mango"]
print(thislist[-1])

#append items
thislist = ["apple","banana","mango"]
thislist.append("orange")
print(thislist)

#remove specific item
thislist = ["apple","banana","mango","orange"]
thislist.remove("orange")
print(thislist)

#loop lists
thislist = ["apple","banana","mango","orange"]
for x in thislist:
    print(x)

#copy lists
thislist = ["apple","banana","mango","orange"]
mylist = thislist.copy()
print(mylist)

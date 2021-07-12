#Dictionaries

thisdict = { "brand" : "ford" ,
             "model" : "Mustang",
             "year" : 1964
             }
print(thisdict)

#access items
thisdict = { "brand" : "ford" ,
             "model" : "Mustang",
             "year" : 1964
             }
print(thislist["model"])

#add new item
thisdict = { "brand" : "ford" ,
             "model" : "Mustang",
             "year" : 1964
             }
x = thisdict.values()
print(x)
thisdict["color"] = "red"
print(x)

#change
thisdict = { "brand" : "ford" ,
             "model" : "Mustang",
             "year" : 1964
             }
thisdict["year"] = 2002
print(thisdict)

#remove
thisdict = { "brand" : "ford" ,
             "model" : "Mustang",
             "year" : 1964
             }
thisdict.pop("model")
print(thisdict)
for x in thisdict:
    print(x)
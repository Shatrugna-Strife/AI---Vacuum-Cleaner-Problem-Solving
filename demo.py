mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
list2 = []
list2 = mylist[:]

print(len(list2))
list3 = []
list3.append(list2)
list3.append([0,1])
print(list3[1])

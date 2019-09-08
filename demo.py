mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
list2 = []
list2 = mylist[:]
print(list2)
print(len(list2))
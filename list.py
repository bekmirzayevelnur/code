mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))           #listdagi dublikatlarni ochiradi
print(mylist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))              # list uzunligi

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])              #listga murojat

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)          #listdan nusxaolish

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2            # 2 ta listni bir biriga qoshish
print(list3)


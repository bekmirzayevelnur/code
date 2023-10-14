# Python 3 code to demonstrate
# property of hash()

# initializing objects
# tuple are immutable
tuple_val = (1, 2, 3, 4, 5)

# list are mutable
list_val = [1, 2, 3, 4, 5]

# Printing the hash values.
# Notice exception when trying
# to convert mutable object
print("The tuple hash value is : " + str(hash(tuple_val)))
print("The list hash value is : " + str(hash(list_val)))

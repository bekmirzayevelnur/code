from itertools import count 
iterator =(count(start = 0, step = 2)) 
print(list(next(iterator) for _ in range(5))) 
iterator = (count(start = 1, step = 2)) 
print(list(next(iterator) for _ in range(5))) 

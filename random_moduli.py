# 3 dan 9 gacha sonlar orasidan random qiladi,  9 kirmaydi
import random
print(random.randrange(3, 9))

/////////////////////////////////////////

# 3 dan 9 gacha sonlar orasidan random qiladi,  9 kiradi
import random
print(random.randint(3, 9))

///////////////////////////////////////

# string lugatdan random qiladi
import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

///////////////////////////////////////

# bu metod yordamida listni aralshtirib yuborsak bo'ladi
import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

//////////////////////////////////////

# bu metod listni ichidan 2 ta tasodifiy stringni olib beradi

import random
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))

//////////////////////////////////////

# bu metod 1 bilan 0 orasidan bitta float qiymat qaytaradi
import random
print(random.random())

///////////////////////////////////////

# bu metod ikkita raqam orasidan bitta float qiymat qaytaradi
import random
print(random.uniform(20, 60))

//////////////////////////////////////


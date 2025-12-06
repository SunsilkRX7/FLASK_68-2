"""
#
# Part:loop
# Section: while loop
# 
"""
i = 1
while i <= 5:
    print("hello world", i)
    if i == 3:
        break
    i += 1

"""
#
#Part: loop
#section: for loop
#
"""    
thiss = ["apple", "banana", "cherry"]
for x in thiss:
    print(x)
    if x == "banana":
        break
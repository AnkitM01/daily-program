# while loops
i=1
while i<10:
    i=i+1
    print(i)

i=3
while i<5:
    print("Ankit")
    i=i+1

fruits = ['apple','banana','graps','watermelon']
i=0
while i<len(fruits):
    print(fruits[i])
    i = i+1
# for loops
a=[3,4,5]
for b in a:
    print(b,end='')

# range in loop

for i in range(0,10,2): # (starting point,ending point,difference between starting n ending point)
    print(i)

# break statement

i=0
for i in range(0,20,2):
    if i==10:
        break
    print(i)

# for with else (optional)
# i=0
# for i in range(0,20,2):
#     print(i)
#     if i==11:
#         break
# else:
#     print("Not match")

# continue statement
for i in range(10):
    if i==5:
        continue
    print(i)

# pass statement
i=4
if i>0:
    pass # instruct to do nothing
while i>6:
    pass
print("Ankit is a good boy")












    
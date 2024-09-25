# what is functions
marks =[45,78,86,77]
percentage1=(sum(marks)/400)*100 #(this is also a sum function)

marks2 =[75,98,88,78]
percentage2=(sum(marks2)/400)*100
print(percentage1,percentage2)

# using functions def

def percent(marks):
    p=(sum(marks)/400)*100
    return p
marks1 =[45,78,86,77]
percentage1=percent(marks1)

marks2 =[75,98,88,78]
percentage2=percent(marks2)
print(percentage1,percentage2)

# quick quiz
# greed a user with a good day

def greet(name=" dr strange"):
    print("good day" + name)

greet(" Ankit")

def mysum(num1,num2):
    return num1+num2
greet()   # default argument
s=mysum(2,3)
print(s)









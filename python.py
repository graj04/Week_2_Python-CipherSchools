def show_loading():
    for _ in range(3):
        print(_)
        print("loading...")


a = 5
b = 7
print(a+b)
show_loading()

print(a-b)
show_loading()

print(a*b)
show_loading()

def sheldo_knock(name):
    for _ in range(3):
        print("knock knock knock",name)

sheldo_knock("gaurav")

#return statement
def add(a,b):
    return a + b 

a = add(1,2)
print(a)
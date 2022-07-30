# Local Scope
def my_func():
    y = 5
    print(y)
    
my_func()

# Global scope
y = 5
def my_func1():
    print(y)
    
def my_other_func1():
    print(y)
    
my_func1()
my_other_func1()

# Global & Local scope
y = 5
x = 10
def my_func2():
    global y
    x = 4
    print(x, y)
    
my_func2()
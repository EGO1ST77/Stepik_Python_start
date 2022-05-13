def print_texas():
    global birds
    birds = 5000
    print(f'В Техасе обитает {birds} птиц')

def print_california():
    print(f'В Калифорнии обитает {birds} птиц')

print_texas()
print_california()


x = 5

def add():
    global x
    x = 3
    x = x + 5
    print(x)

add()
print(x)
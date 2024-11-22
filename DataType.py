name = "Manoj Behera"

def show_name():
    print(name)

def show_name1():
    global name
    name = "Behera Manoj"
    print(name)

show_name()
show_name1()
show_name()
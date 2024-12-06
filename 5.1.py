


def upper_decor(fun):
    def wrapper():
        result=fun()
        return result.upper()
    return wrapper

@upper_decor
def hello_name():
    return "name"

f=upper_decor(hello_name)
print(f())


##################
def abcd():
    print("hai")
    abcd()


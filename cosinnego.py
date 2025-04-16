def fun_decor(fun):
    def wrap():
        print("*"*10)
        fun()
        print("*"*10)
    return wrap

@fun_decor
def hello():
    print("helol")

hello()
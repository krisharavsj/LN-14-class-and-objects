class employee:
    def __init__ (self):
        print("constructor")
    def __del__ (self):
        print("destructor")
def call ():
    obj=employee()
    print("creating object is done")
    return obj
print("calling the object")
obj=call()
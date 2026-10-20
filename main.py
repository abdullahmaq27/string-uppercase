class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructor called")
def create_obj():
    print("making object")
    object = employee()
    print("function ended")
    return object
print("calling create_obj()function")
obj = create_obj()


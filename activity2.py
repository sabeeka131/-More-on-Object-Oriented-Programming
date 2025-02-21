class Employee:


    #initializing
    def __init__(self):
        print('Employee created')


    #calling destructor
    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function endd...')
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
class fruit:


    def __init__(self, name, color):
        self.name = name
        self.color = color


    #instance method
    def intro(self):
        print("hello, I am", self.name)


#object Creation
apple = fruit('Apple', 'Red')
#calling Function
apple.intro()
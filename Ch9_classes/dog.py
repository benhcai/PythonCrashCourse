class Dog:
    def __init__(self):
        print(self)

    def a(self):
        print('Not using any properties of Dog class, 
                but self must still be passed')

dog = Dog()
dog.a()



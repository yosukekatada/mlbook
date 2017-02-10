class MyObject:

    STATE = None

    def get_state(self):
        return self.STATE

myobj = MyObject()
print(myobj.STATE)  # => None
MyObject.STATE = 1
print(myobj.get_state())  # => 1

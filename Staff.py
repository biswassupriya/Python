def class Staff:
    def __init__(self):
        self.firstName = "not set"
        self.modules = []
        self.noOfModules = 0
        
    def getFirstName(self):
        return self.firstName
    
    def setFirstName(self, n):
        self.firstName = n
        
def test():
    s1 = Staff()
    print("Name...")
    print(s1.getFirstName())
    s1.setFirstName("Kostas")
    print("New name...")
    print(s1.getFirstName())
class User:
    #   constructor
    def __init__(self, username, fname, lname, email, address, cc):
        self.username = username
        self.fname = fname
        self.lname = lname
        self.email = email
        self.address = address
        self.cc = cc

    def getUsername(self):
        return self.username
    
    def getFname(self):
        return self.fname

    def getLname(self):
        return self.lname

    def getEmail(self):
        return self.email

    def getAddress(self):
        return self.address

    def getCC(self):
        return self.cc

    def setAddress(self, address):
        self.address = address

    def setCC(self, cc):
        self.cc = cc

class Book:
    #   constructor
    def __init__(self, productNum, productName, price, inventory):
        self.productNum = productNum
        self.productName = productName
        self.price = price
        self.inventory = inventory

    def getProductNum(self):
        return self.getProductNum
    
    def getProductName(self):
        return self.productName

    def getPrice(self):
        return self.price

    def getInventory(self):
        return self.inventory

    def decrementInventory(self):
        self.inventory = self.inventory - 1
    

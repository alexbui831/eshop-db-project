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

class Item:
    #   constructor
    def __init__(self, productNum, productName, price, inventory):
        self.productNum = productNum
        self.productName = productName
        self.price = price
        self.inventory = inventory

    def getProductNum(self):
        return self.productNum
    
    def getProductName(self):
        return self.productName

    def getPrice(self):
        return self.price

    def getInventory(self):
        return self.inventory

    def decrementInventory(self):
        self.inventory = self.inventory - 1
    
class Cart:

    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, id):
        for x in range(len(self.items)):
            if(self.items[x].getProductNum() == id):
                del self.items[x]
                break
    
    def checkout(self):
        for x in range(len(self.items)):
            del self.items[x]

    def printCart(self):
        for x in range(len(self.items)):
            print("| Book ID:", self.items[x].getProductNum(), "| Title:", self.items[x].getProductName(), "| Price: $" + str(self.items[x].getPrice()), "|")

class History:

    def __init__(self, item, date):
        self.item = item
        self.date = date

    def printHistory(self):
        print("| Title:", self.item.getProductName(), "| Price: $" + str(self.item.getPrice()), "| Date:", self.date, "|")



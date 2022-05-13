class shoppingCart():

    # contructor
    def __init__(self, itemId = 0, cart={}):
        self.cart = cart
        self.itemId = itemId
    
    # runner method
    def runner(self):
        
        userChoice = input(f'What would you like to do with your cart? (type: "show", "add", "remove", or "quit")\n').lower()

        while True:
            if (userChoice == 'show'):
                self.show() 
            elif (userChoice == 'add'):
                self.add()
            elif (userChoice == 'remove'):
                self.remove()
            elif (userChoice == 'quit'):
                print(f'You\'ve successfully checked out {list(self.cart.values())}')
                print('Thank you for shopping at the best market in town!')
                quit()
            else:
                print('That is not a valid option... please choose again.')
                self.runner()
        

    # functionality methods
    def add(self):
        addItem = input('What item would you like to add to your shopping cart? \n').title()
        self.cart[f'{self.itemId}'] = addItem
        self.itemId += 1
        print(f'{addItem} has been added to your cart!')
        print(f'Your current cart is: {self.cart}')
        self.runner()
    

    def remove(self):
        print(f'Your current cart is {self.cart}')
        removeItem = input('What item would you like to remove? \n').title()
        if removeItem in self.cart.values():
            for key, value in dict(self.cart).items():
                if removeItem == value:
                    print(f'{removeItem} has been removed from your cart.')
                    del self.cart[key]
        else:
            print(f'{removeItem} is not in your cart.')
            self.remove()

        self.runner()


    def show(self):
        print(f'Your current cart is: {self.cart}')
        self.runner()

cart = shoppingCart()

cart.runner()

def run():
    print('Welcome to Christian\'s Superstore!')
    cart.runner()

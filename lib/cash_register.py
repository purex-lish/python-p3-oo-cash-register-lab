# # #!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = None

    def add_item(self, title, price, quantity=1):
        '''Adds an item to the register with a given title, price, and optional quantity.'''
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = (price, quantity)  # Store the last transaction

    def apply_discount(self):
        '''Applies a discount to the total amount.'''
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # totals rounded to 2 decimal places
            self.total = round(self.total, 2)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        '''Subtracts the last item from the total.'''
        if self.last_transaction is not None:
            price, quantity = self.last_transaction
            self.total -= price * quantity
            # Remove the last items from the items list
            for _ in range(quantity):
                self.items.pop()
            # Clear the last transaction
            self.last_transaction = None
            # total shouldn't go negative
            self.total = max(self.total, 0)

    def __str__(self):
        return f"Total: ${self.total:.2f}, Items: {self.items}, Discount: {self.discount}%"


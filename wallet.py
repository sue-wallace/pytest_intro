# wallet.py

# if the user tries to spend cash tehy don't have in their wallet

class InsufficientAmount(Exception):
    pass

# Defining the wallet class


class Wallet(object):

    # initialising the amount in the wallet
    # If no funds are added then this is set to zero

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    # if the user tries to spend cash, do they have enough?

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    # adding cash to the wallet balance

    def add_cash(self, amount):
        self.balance += amount
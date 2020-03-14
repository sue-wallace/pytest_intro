# tests: to test the application developed in wallet.py

# test_wallet.py

# is the user trying to spend more cash than they have in their wallet?

import pytest
from wallet import Wallet, InsufficientAmount

# How much is in the wallet?

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

# does adding cash mean that the amount in the wallet increases to the correct amount?

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

# does spending cash mean that the amount in the wallet increases to the correct amount?

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

# Exception rule: if more cash is spent than what is in the wallet

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)
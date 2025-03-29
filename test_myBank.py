import pytest
from myBank import BankAccount


def test_deposit():
    # Arrange
    account = BankAccount(balance=100)


    # Act
    account.deposit(50)


    # Assert
    assert account.balance == 150


def test_withdraw_sufficient_balance():
    # Arrange
    account = BankAccount(balance=100)


    # Act
    account.withdraw(40)


    # Assert
    assert account.balance == 60


def test_withdraw_insufficient_balance():
    # Arrange
    account = BankAccount(balance=100)


    # Act & Assert
    with pytest.raises(ValueError, match="Insufficient funds!"):
        account.withdraw(200)


def test_deposit_negative_amount():
    # Arrange
    account = BankAccount(balance=100)


    # Act & Assert
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(-50)


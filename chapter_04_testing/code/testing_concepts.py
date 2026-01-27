"""
Chapter 4: Testing - Implementation of key concepts

This module demonstrates testing concepts including:
- Basic assertions
- Unit testing with unittest
- Test-driven development
- Testing object-oriented code
"""

# 4.1 Writing Tests - Basic assertions
def demonstrate_assertions():
    """
    Shows basic assertion usage.

    Assertions check that conditions are true.
    If false, they raise AssertionError.
    """
    # Basic assertions
    assert 2 + 2 == 4, "Basic math should work"
    assert len("hello") == 5, "String length should be correct"
    assert True, "This should always pass"
    assert not False, "Negation should work"

    # Function testing with assertions
    result = add_numbers(3, 5)
    assert result == 8, f"add_numbers(3, 5) should be 8, got {result}"

    return "All assertions passed!"


def add_numbers(a, b):
    """Simple function to demonstrate testing."""
    return a + b


# 4.2 Unit Testing with unittest
class Calculator:
    """A simple calculator class for testing demonstrations."""

    def __init__(self):
        self.history = []  # Keep track of operations

    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Subtract two numbers."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        """Get calculation history."""
        return self.history.copy()


# 4.3 Test-Driven Development Example
class Stack:
    """
    A simple stack implementation developed with TDD.

    TDD Process:
    1. Write failing test
    2. Write minimal code to pass
    3. Refactor
    4. Repeat
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """Push item onto stack."""
        self.items.append(item)

    def pop(self):
        """Pop item from stack."""
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return top item without removing."""
        if not self.items:
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return stack size."""
        return len(self.items)


# 4.4 What to Test - Edge cases and error conditions
class StringProcessor:
    """A class for processing strings, with various edge cases."""

    def reverse(self, text):
        """Reverse a string."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text[::-1]

    def count_words(self, text):
        """Count words in text."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return len(text.split())

    def capitalize_words(self, text):
        """Capitalize first letter of each word."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text.title()


# 4.5 Testing and Object-Oriented Design
class BankAccount:
    """
    A bank account class demonstrating testing OOP concepts.

    Tests should focus on:
    - State changes (balance updates)
    - Business rules (no negative balances)
    - Error conditions
    - Method interactions
    """

    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance
        self._transactions = []

    def deposit(self, amount):
        """Deposit money into account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(f"Deposit: +{amount}")
        return self._balance

    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transactions.append(f"Withdrawal: -{amount}")
        return self._balance

    def get_balance(self):
        """Get current balance."""
        return self._balance

    def get_transaction_history(self):
        """Get transaction history."""
        return self._transactions.copy()


if __name__ == "__main__":
    # Demonstrate basic assertions
    print("Testing assertions...")
    print(demonstrate_assertions())

    # Demonstrate calculator
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"History: {calc.get_history()}")

    # Demonstrate stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(f"Stack size: {stack.size()}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")

    # Demonstrate string processor
    processor = StringProcessor()
    print(f"Reverse 'hello': {processor.reverse('hello')}")
    print(f"Word count: {processor.count_words('hello world test')}")

    # Demonstrate bank account
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    print(f"Balance: ${account.get_balance()}")
    print(f"Transactions: {account.get_transaction_history()}")

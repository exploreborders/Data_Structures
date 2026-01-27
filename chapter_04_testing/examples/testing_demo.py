#!/usr/bin/env python3
"""
Examples demonstrating Chapter 4 testing concepts.
Run this script to see testing patterns and TDD in action.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from chapter_04_testing.code.testing_concepts import *

print("=== Chapter 4: Testing Examples ===\n")

print("1. Basic Assertions:")
try:
    result = demonstrate_assertions()
    print(f"   ✓ {result}")
except AssertionError as e:
    print(f"   ✗ Assertion failed: {e}")
print()

print("2. Unit Testing with Calculator:")
calc = Calculator()
print(f"   2 + 3 = {calc.add(2, 3)}")
print(f"   10 - 3 = {calc.subtract(10, 3)}")
print(f"   4 * 5 = {calc.multiply(4, 5)}")
print(f"   10 / 2 = {calc.divide(10, 2)}")

# Test error handling
try:
    calc.divide(10, 0)
except ZeroDivisionError:
    print("   ✓ Division by zero properly raises error")

print(f"   History: {calc.get_history()}")
print()

print("3. Test-Driven Development - Stack Implementation:")
stack = Stack()

# Demonstrate stack operations
print("   Pushing items: 1, 2, 3")
stack.push(1)
stack.push(2)
stack.push(3)
print(f"   Stack size: {stack.size()}")
print(f"   Is empty: {stack.is_empty()}")

print("   Popping items (LIFO):")
while not stack.is_empty():
    print(f"   Pop: {stack.pop()}")
print(f"   Stack size: {stack.size()}")
print()

print("4. Testing Edge Cases - String Processor:")
processor = StringProcessor()

# Normal cases
print(f"   Reverse 'hello': {processor.reverse('hello')}")
print(f"   Word count 'hello world': {processor.count_words('hello world')}")
print(
    f"   Capitalize 'hello world': {processor.capitalize_words('hello world')}")

# Edge cases
print(f"   Reverse empty string: '{processor.reverse('')}'")
print(f"   Word count empty string: {processor.count_words('')}")
print(
    f"   Word count multiple spaces: {processor.count_words('hello   world    test')}"
)

# Error cases
try:
    processor.reverse(123)
except TypeError as e:
    print(f"   ✓ Non-string input properly raises error: {e}")
print()

print("5. Testing Object-Oriented Design - Bank Account:")
account = BankAccount(1000)
print(f"   Initial balance: ${account.get_balance()}")

# Normal operations
account.deposit(500)
print(f"   After deposit of $500: ${account.get_balance()}")

account.withdraw(200)
print(f"   After withdrawal of $200: ${account.get_balance()}")

# Error cases
try:
    account.withdraw(2000)  # Insufficient funds
except ValueError as e:
    print(f"   ✓ Insufficient funds properly prevented: {e}")

try:
    account.deposit(-100)  # Negative deposit
except ValueError as e:
    print(f"   ✓ Negative deposit properly prevented: {e}")

print(f"   Transaction history: {account.get_transaction_history()}")
print()

print("=== Testing Best Practices Demonstrated ===")
print("- Test behavior, not implementation")
print("- Test edge cases and error conditions")
print("- Use descriptive test names")
print("- Keep tests independent and isolated")
print("- Test both success and failure scenarios")
print("- Focus on public interfaces")
print()

print("=== TDD Cycle Example ===")

# Simulate TDD for a simple function
print("TDD: Implementing a function to check if number is even")
print()

# Step 1: Write failing test
print("Step 1 - RED: Write failing test")


def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    print("   Test defined but function doesn't exist yet")


# Step 2: Write minimal code to pass
print("Step 2 - GREEN: Write minimal code")


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


# Step 3: Verify tests pass
print("Step 3: Run tests")
try:
    test_is_even()
    print("   ✓ All tests pass!")
except AssertionError as e:
    print(f"   ✗ Test failed: {e}")

# Step 4: Refactor (if needed)
print("Step 4 - REFACTOR: Code is simple, no changes needed")
print(f"   Final implementation: {is_even.__doc__}")
print(f"   Test with 4: {is_even(4)}")
print(f"   Test with 5: {is_even(5)}")

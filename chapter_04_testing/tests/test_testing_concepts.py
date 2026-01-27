import unittest
import pytest
from chapter_04_testing.code.testing_concepts import (
    add_numbers,
    Calculator,
    Stack,
    StringProcessor,
    BankAccount,
    demonstrate_assertions,
)


# 4.1 Writing Tests - Basic assertions
def test_basic_assertions():
    """Test that demonstrate_assertions works."""
    result = demonstrate_assertions()
    assert result == "All assertions passed!"


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(1.5, 2.5) == 4.0


# 4.2 Unit Testing with unittest
class TestCalculator(unittest.TestCase):
    """Unit tests for the Calculator class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def tearDown(self):
        """Clean up after each test method."""
        pass

    def test_addition(self):
        """Test calculator addition."""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
        self.assertIn("2 + 3 = 5", self.calc.get_history())

    def test_subtraction(self):
        """Test calculator subtraction."""
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)

    def test_multiplication(self):
        """Test calculator multiplication."""
        result = self.calc.multiply(4, 5)
        self.assertEqual(result, 20)

    def test_division(self):
        """Test calculator division."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        """Test division by zero raises error."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_history_tracking(self):
        """Test that history is maintained correctly."""
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0], "1 + 2 = 3")
        self.assertEqual(history[1], "3 * 4 = 12")


# 4.3 Test-Driven Development - Stack tests
class TestStack(unittest.TestCase):
    """TDD-developed tests for Stack class."""

    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        """Test that a new stack is empty."""
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

    def test_push_increases_size(self):
        """Test that push increases stack size."""
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)

    def test_push_pop_roundtrip(self):
        """Test push and pop maintain order (LIFO)."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertTrue(self.stack.is_empty())

    def test_peek_does_not_remove(self):
        """Test that peek returns top item without removing it."""
        self.stack.push(42)
        self.assertEqual(self.stack.peek(), 42)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.pop(), 42)

    def test_pop_empty_stack_raises_error(self):
        """Test that popping empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty_stack_raises_error(self):
        """Test that peeking empty stack raises IndexError."""
        with self.assertRaises(IndexError):
            self.stack.peek()


# 4.4 What to Test - Edge cases and error conditions
class TestStringProcessor(unittest.TestCase):
    """Tests for StringProcessor including edge cases."""

    def setUp(self):
        self.processor = StringProcessor()

    def test_reverse_normal_string(self):
        """Test reversing a normal string."""
        result = self.processor.reverse("hello")
        self.assertEqual(result, "olleh")

    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        result = self.processor.reverse("")
        self.assertEqual(result, "")

    def test_reverse_single_character(self):
        """Test reversing a single character."""
        result = self.processor.reverse("a")
        self.assertEqual(result, "a")

    def test_reverse_unicode(self):
        """Test reversing unicode strings."""
        result = self.processor.reverse("héllo")
        self.assertEqual(result, "olléh")

    def test_reverse_non_string_raises_error(self):
        """Test that non-string input raises TypeError."""
        with self.assertRaises(TypeError):
            self.processor.reverse(123)

    def test_count_words_normal(self):
        """Test counting words in normal text."""
        result = self.processor.count_words("hello world test")
        self.assertEqual(result, 3)

    def test_count_words_empty(self):
        """Test counting words in empty string."""
        result = self.processor.count_words("")
        self.assertEqual(result, 0)

    def test_count_words_multiple_spaces(self):
        """Test handling multiple spaces between words."""
        result = self.processor.count_words("hello   world    test")
        self.assertEqual(result, 3)

    def test_capitalize_words(self):
        """Test capitalizing first letter of each word."""
        result = self.processor.capitalize_words("hello world")
        self.assertEqual(result, "Hello World")


# 4.5 Testing and Object-Oriented Design
class TestBankAccount(unittest.TestCase):
    """Tests for BankAccount demonstrating OOP testing."""

    def setUp(self):
        self.account = BankAccount(100)

    def test_initial_balance(self):
        """Test account starts with correct balance."""
        self.assertEqual(self.account.get_balance(), 100)

    def test_negative_initial_balance_raises_error(self):
        """Test that negative initial balance raises ValueError."""
        with self.assertRaises(ValueError):
            BankAccount(-50)

    def test_deposit_increases_balance(self):
        """Test that deposit increases balance."""
        result = self.account.deposit(50)
        self.assertEqual(result, 150)
        self.assertEqual(self.account.get_balance(), 150)

    def test_deposit_zero_or_negative_raises_error(self):
        """Test that depositing zero or negative amounts raises error."""
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw_decreases_balance(self):
        """Test that withdrawal decreases balance."""
        result = self.account.withdraw(30)
        self.assertEqual(result, 70)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_insufficient_funds_raises_error(self):
        """Test that withdrawing more than balance raises error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(150)

    def test_withdraw_zero_or_negative_raises_error(self):
        """Test that withdrawing zero or negative amounts raises error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(0)
        with self.assertRaises(ValueError):
            self.account.withdraw(-10)

    def test_transaction_history(self):
        """Test that transactions are recorded in history."""
        self.account.deposit(50)
        self.account.withdraw(30)
        history = self.account.get_transaction_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0], "Deposit: +50")
        self.assertEqual(history[1], "Withdrawal: -30")

    def test_balance_unchanged_after_failed_operations(self):
        """Test that balance doesn't change after failed operations."""
        initial_balance = self.account.get_balance()
        try:
            self.account.withdraw(1000)  # Should fail
        except ValueError:
            pass  # Expected
        self.assertEqual(self.account.get_balance(), initial_balance)


# Parameterized tests example
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ],
)
def test_add_numbers_parameterized(a, b, expected):
    """Parameterized test for add_numbers function."""
    assert add_numbers(a, b) == expected


if __name__ == "__main__":
    unittest.main()

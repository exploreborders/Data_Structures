import sys
import os
import unittest

# Add root directory to path so imports work
sys.path.insert(0, os.path.join(os.getcwd(), "..", ".."))

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
    print("✓ test_basic_assertions")


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(1.5, 2.5) == 4.0
    print("✓ test_add_numbers")


# 4.2 Unit Testing with unittest framework style tests
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
        assert result == 5
        assert "2 + 3 = 5" in self.calc.get_history()
        print("✓ TestCalculator.test_addition")

    def test_subtraction(self):
        """Test calculator subtraction."""
        result = self.calc.subtract(10, 3)
        assert result == 7
        print("✓ TestCalculator.test_subtraction")

    def test_multiplication(self):
        """Test calculator multiplication."""
        result = self.calc.multiply(4, 5)
        assert result == 20
        print("✓ TestCalculator.test_multiplication")

    def test_division(self):
        """Test calculator division."""
        result = self.calc.divide(10, 2)
        assert result == 5
        print("✓ TestCalculator.test_division")

    def test_division_by_zero(self):
        """Test division by zero raises error."""
        try:
            self.calc.divide(10, 0)
            assert False, "Should have raised ZeroDivisionError"
        except ZeroDivisionError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"
        print("✓ TestCalculator.test_division_by_zero")

    def test_history_tracking(self):
        """Test that history is maintained correctly."""
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)
        history = self.calc.get_history()
        assert len(history) == 2
        assert history[0] == "1 + 2 = 3"
        assert history[1] == "3 * 4 = 12"
        print("✓ TestCalculator.test_history_tracking")


# 4.3 Test-Driven Development - Stack tests
class TestStack(unittest.TestCase):
    """TDD-developed tests for Stack class."""

    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        """Test that a new stack is empty."""
        assert self.stack.is_empty() == True
        assert self.stack.size() == 0
        print("✓ TestStack.test_new_stack_is_empty")

    def test_push_increases_size(self):
        """Test that push increases stack size."""
        self.stack.push(1)
        assert self.stack.is_empty() == False
        assert self.stack.size() == 1
        print("✓ TestStack.test_push_increases_size")

    def test_push_pop_roundtrip(self):
        """Test push and pop maintain order (LIFO)."""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        assert self.stack.pop() == 3
        assert self.stack.pop() == 2
        assert self.stack.pop() == 1
        assert self.stack.is_empty() == True
        print("✓ TestStack.test_push_pop_roundtrip")

    def test_peek_does_not_remove(self):
        """Test that peek returns top item without removing it."""
        self.stack.push(42)
        assert self.stack.peek() == 42
        assert self.stack.size() == 1
        assert self.stack.pop() == 42
        print("✓ TestStack.test_peek_does_not_remove")

    def test_pop_empty_stack_raises_error(self):
        """Test that popping empty stack raises IndexError."""
        try:
            self.stack.pop()
            assert False, "Should have raised IndexError"
        except IndexError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"
        print("✓ TestStack.test_pop_empty_stack_raises_error")

    def test_peek_empty_stack_raises_error(self):
        """Test that peeking empty stack raises IndexError."""
        try:
            self.stack.peek()
            assert False, "Should have raised IndexError"
        except IndexError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"
        print("✓ TestStack.test_peek_empty_stack_raises_error")


# 4.4 What to Test - Edge cases and error conditions
class TestStringProcessor(unittest.TestCase):
    """Tests for StringProcessor including edge cases."""

    def setUp(self):
        self.processor = StringProcessor()

    def test_reverse_normal_string(self):
        """Test reversing a normal string."""
        result = self.processor.reverse("hello")
        assert result == "olleh"
        print("✓ TestStringProcessor.test_reverse_normal_string")

    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        result = self.processor.reverse("")
        assert result == ""
        print("✓ TestStringProcessor.test_reverse_empty_string")

    def test_reverse_single_character(self):
        """Test reversing a single character."""
        result = self.processor.reverse("a")
        assert result == "a"
        print("✓ TestStringProcessor.test_reverse_single_character")

    def test_reverse_unicode(self):
        """Test reversing unicode strings."""
        result = self.processor.reverse("héllo")
        assert result == "olléh"
        print("✓ TestStringProcessor.test_reverse_unicode")

    def test_reverse_non_string_raises_error(self):
        """Test that non-string input raises TypeError."""
        try:
            self.processor.reverse(123)
            assert False, "Should have raised TypeError"
        except TypeError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"
        print("✓ TestStringProcessor.test_reverse_non_string_raises_error")

    def test_count_words_normal(self):
        """Test counting words in normal text."""
        result = self.processor.count_words("hello world test")
        assert result == 3
        print("✓ TestStringProcessor.test_count_words_normal")

    def test_count_words_empty(self):
        """Test counting words in empty string."""
        result = self.processor.count_words("")
        assert result == 0
        print("✓ TestStringProcessor.test_count_words_empty")

    def test_count_words_multiple_spaces(self):
        """Test handling multiple spaces between words."""
        result = self.processor.count_words("hello   world    test")
        assert result == 3
        print("✓ TestStringProcessor.test_count_words_multiple_spaces")

    def test_capitalize_words(self):
        """Test capitalizing first letter of each word."""
        result = self.processor.capitalize_words("hello world")
        assert result == "Hello World"
        print("✓ TestStringProcessor.test_capitalize_words")


# 4.5 Testing and Object-Oriented Design
class TestBankAccount(unittest.TestCase):
    """Tests for BankAccount demonstrating OOP testing."""

    def setUp(self):
        self.account = BankAccount(100)

    def test_initial_balance(self):
        """Test account starts with correct balance."""
        assert self.account.get_balance() == 100
        print("✓ TestBankAccount.test_initial_balance")

    def test_negative_initial_balance_raises_error(self):
        """Test that negative initial balance raises ValueError."""
        try:
            BankAccount(-50)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"
        print("✓ TestBankAccount.test_negative_initial_balance_raises_error")

    def test_deposit_increases_balance(self):
        """Test that deposit increases balance."""
        result = self.account.deposit(50)
        assert result == 150
        assert self.account.get_balance() == 150
        print("✓ TestBankAccount.test_deposit_increases_balance")

    def test_deposit_zero_or_negative_raises_error(self):
        """Test that depositing zero or negative amounts raises error."""
        try:
            self.account.deposit(0)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"

        try:
            self.account.deposit(-10)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"
        print("✓ TestBankAccount.test_deposit_zero_or_negative_raises_error")

    def test_withdraw_decreases_balance(self):
        """Test that withdrawal decreases balance."""
        result = self.account.withdraw(30)
        assert result == 70
        assert self.account.get_balance() == 70
        print("✓ TestBankAccount.test_withdraw_decreases_balance")

    def test_withdraw_insufficient_funds_raises_error(self):
        """Test that withdrawing more than balance raises error."""
        try:
            self.account.withdraw(150)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"
        print("✓ TestBankAccount.test_withdraw_insufficient_funds_raises_error")

    def test_withdraw_zero_or_negative_raises_error(self):
        """Test that withdrawing zero or negative amounts raises error."""
        try:
            self.account.withdraw(0)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"

        try:
            self.account.withdraw(-10)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass  # Expected
        except Exception as e:
            assert False, f"Wrong exception type: {e}"
        print("✓ TestBankAccount.test_withdraw_zero_or_negative_raises_error")

    def test_transaction_history(self):
        """Test that transactions are recorded in history."""
        self.account.deposit(50)
        self.account.withdraw(30)
        history = self.account.get_transaction_history()
        assert len(history) == 2
        assert history[0] == "Deposit: +50"
        assert history[1] == "Withdrawal: -30"
        print("✓ TestBankAccount.test_transaction_history")

    def test_balance_unchanged_after_failed_operations(self):
        """Test that balance doesn't change after failed operations."""
        initial_balance = self.account.get_balance()
        try:
            self.account.withdraw(1000)  # Should fail
        except ValueError:
            pass  # Expected
        assert self.account.get_balance() == initial_balance
        print("✓ TestBankAccount.test_balance_unchanged_after_failed_operations")


def test_add_numbers_parameterized():
    """Parameterized test for add_numbers function."""
    test_cases = [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ]

    for a, b, expected in test_cases:
        assert add_numbers(a, b) == expected
    print("✓ test_add_numbers_parameterized")


def run_test_class(test_class):
    """Run all test methods in a test class."""
    test_instance = test_class()
    test_methods = [
        method
        for method in dir(test_instance)
        if method.startswith("test_") and callable(getattr(test_instance, method))
    ]

    for test_method in test_methods:
        # Call setUp before each test if it exists
        if hasattr(test_instance, "setUp"):
            test_instance.setUp()

        try:
            getattr(test_instance, test_method)()
        except Exception as e:
            print(f"✗ {test_class.__name__}.{test_method}: {e}")
            return False
        finally:
            # Call tearDown after each test if it exists
            if hasattr(test_instance, "tearDown"):
                test_instance.tearDown()

    return True


def run_all_tests():
    """Run all test functions and test classes."""
    print("Running Chapter 4 Testing Tests...")
    print("=" * 50)

    # Run simple test functions
    simple_tests = [
        test_basic_assertions,
        test_add_numbers,
        test_add_numbers_parameterized,
    ]

    for test_func in simple_tests:
        try:
            test_func()
        except Exception as e:
            print(f"✗ {test_func.__name__}: {e}")
            return False

    # Run test classes
    test_classes = [
        TestCalculator,
        TestStack,
        TestStringProcessor,
        TestBankAccount,
    ]

    for test_class in test_classes:
        if not run_test_class(test_class):
            return False

    print("=" * 50)
    print("All tests passed! ✓")
    return True


if __name__ == "__main__":
    run_all_tests()

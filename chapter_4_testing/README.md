# Chapter 4: Testing

This chapter covers the fundamentals of software testing: writing tests, unit testing with unittest, test-driven development (TDD), what to test, and testing object-oriented design.

## Key Concepts

### Why Testing Matters
- **Correctness**: Tests verify code works as intended
- **Regression Prevention**: Tests catch bugs when code changes
- **Documentation**: Tests show how code should be used
- **Confidence**: Tests give certainty when refactoring

### Writing Tests
- **Assertions**: Check that code behaves correctly
- **Test Cases**: Individual scenarios to verify
- **Edge Cases**: Test boundaries and unusual inputs

### Unit Testing with unittest
- **Test Classes**: Group related tests together
- **setUp/tearDown**: Initialize/cleanup before/after tests
- **Assertions**: Rich set of comparison methods

### Test-Driven Development (TDD)
- **Red-Green-Refactor Cycle**:
  1. Write failing test (Red)
  2. Write minimal code to pass (Green)
  3. Refactor while keeping tests passing
- **Benefits**: Better design, confidence in changes

### What to Test
- **Behavior, not implementation**: Test what code does, not how
- **Public interfaces**: Test methods users will call
- **Edge cases**: Boundaries, errors, unusual inputs
- **Integration**: How components work together

### Testing Object-Oriented Design
- **Class behavior**: Test methods and state changes
- **Inheritance**: Test parent/child relationships
- **Composition**: Test component interactions
- **Encapsulation**: Test through public interfaces

## Examples with Detailed Explanations

### Basic Assertions
```python
# Simple assertion
assert 2 + 2 == 4, "Basic math should work"

# Function testing
def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(-1, 1) == 0
```

### Unit Testing with unittest
```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_division_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(10, 0)
```

### Test-Driven Development Example
```python
# Step 1: Write failing test (RED)
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5  # 0,1,1,2,3,5

# Step 2: Write minimal code (GREEN)
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Step 3: Refactor (optimize with memoization)
def fibonacci(n, memo={}):
    if n in memo: return memo[n]
    if n == 0: return 0
    if n == 1: return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```
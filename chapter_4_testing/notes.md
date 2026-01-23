# Personal Notes for Chapter 4

## Key Concepts Explained

### The Importance of Testing
- **Bugs are inevitable**: All code has bugs; testing finds them before users do
- **Confidence in changes**: Tests let you refactor without fear
- **Living documentation**: Tests show exactly how code should work
- **Design improvement**: Writing tests often reveals design flaws

### Writing Tests: The Basics
- **Assertions**: `assert condition, message` - fails if condition is False
- **Test functions**: Functions that run assertions
- **Test discovery**: Tools like pytest automatically find and run tests
- **Failing fast**: Tests should fail immediately when something is wrong

### Unit Testing with unittest
- **TestCase class**: Base class for grouping related tests
- **setUp()**: Run before each test method - initialize fixtures
- **tearDown()**: Run after each test - cleanup
- **Assertion methods**: self.assertEqual(), assertRaises(), etc.

### Test-Driven Development (TDD)
- **Red-Green-Refactor**: The TDD mantra
  - **Red**: Write test that fails (defines desired behavior)
  - **Green**: Write minimal code to make test pass
  - **Refactor**: Improve code while keeping tests passing
- **Benefits**:
  - Forces thinking about interface first
  - Prevents over-engineering
  - Provides immediate feedback
  - Creates comprehensive test suite

### What to Test: Focus on Value
- **Behavior over implementation**: Test what code does, not internal details
- **Public APIs**: Test methods users actually call
- **Edge cases**: Empty inputs, boundaries, error conditions
- **Integration points**: Where components interact
- **Regression tests**: Bugs that were fixed (to prevent reoccurrence)

### Testing Object-Oriented Code
- **State testing**: Verify object state after operations
- **Behavior testing**: Test method interactions
- **Inheritance testing**: Test overridden methods work correctly
- **Composition testing**: Test component collaborations
- **Mocking**: Isolate units by replacing dependencies

## Key Takeaways
- **Tests are code**: They need maintenance and can have bugs
- **Test coverage**: Measure how much code is exercised by tests
- **Test isolation**: Each test should be independent
- **Test naming**: Clear names like `test_add_positive_numbers`
- **When to test**: Before committing, after changes, before releases

## Common Testing Patterns

### Arrange-Act-Assert (AAA)
```python
def test_something():
    # Arrange: Set up test data
    calc = Calculator()

    # Act: Perform the action being tested
    result = calc.add(2, 3)

    # Assert: Verify the result
    assert result == 5
```

### Testing Exceptions
```python
def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
```

### Parameterized Testing
```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## Exercises/Thoughts
- **Write tests first**: Try TDD on a simple function
- **Test existing code**: Add tests to code you wrote earlier
- **Edge case hunting**: Find edge cases for common functions
- **Refactor with confidence**: Change code design while keeping tests passing

## My Understanding
Testing is not optional - it's essential for reliable software. TDD forces better design, comprehensive testing catches bugs early, and well-written tests serve as documentation. The key is testing behavior, not implementation, and maintaining test quality alongside code quality.
import sys
import os

# Add code directory to path for imports (relative to this test file)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from example import greet, add_numbers


def test_greet():
    assert (
        greet("World") == "Hello, World! Welcome to learning data structures in Python."
    )
    assert (
        greet("Alice") == "Hello, Alice! Welcome to learning data structures in Python."
    )


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

if __name__ == "__main__":
    # Run all test methods
    test_classes = [
        test_greet,
        test_add_numbers,
    ]

    total_passed = 0
    total_failed = 0

    for testClass in test_classes:
        instance = testClass()
        methods = [method for method in dir(instance) if method.startswith("test_")]

        print(f"\nRunning {testClass.__name__} tests...")
        class_passed = 0
        class_failed = 0

        for method_name in methods:
            try:
                method = getattr(instance, method_name)
                method()
                print(f"  ✓ {method_name}")
                class_passed += 1
            except Exception as e:
                print(f"  ✗ {method_name}: {e}")
                class_failed += 1

        print(f"  Results: {class_passed} passed, {class_failed} failed")
        total_passed += class_passed
        total_failed += class_failed

    print(
        f"\n🎉 Final Results: {total_passed} tests passed, {total_failed} tests failed"
    )

    if total_failed > 0:
        print("Some tests failed - check implementation compatibility")
    else:
        print("🎉 All Chapter 01 overview tests passed successfully!")
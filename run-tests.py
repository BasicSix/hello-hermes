#!/usr/bin/env python3
"""
Simple test runner for hello-hermes without pytest dependency
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from hello_hermes.utils import calculate_average, fibonacci, factorial


def run_tests():
    """Run all tests manually"""
    print("🧪 Running hello-hermes unit tests...")
    print("=" * 50)

    tests_passed = 0
    tests_failed = 0

    # Test calculate_average
    print("\n📊 Testing calculate_average:")
    try:
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        print("✅ Basic average calculation")
        tests_passed += 1

        assert calculate_average([]) == 0.0
        print("✅ Empty list returns 0.0")
        tests_passed += 1

        assert calculate_average([5]) == 5.0
        print("✅ Single element list")
        tests_passed += 1

        assert calculate_average([-1, -2, -3, -4, -5]) == -3.0
        print("✅ Negative numbers")
        tests_passed += 1

        assert calculate_average([-2, 0, 2]) == 0.0
        print("✅ Mixed signs")
        tests_passed += 1

    except Exception as e:
        print(f"❌ calculate_average failed: {e}")
        tests_failed += 1

    # Test fibonacci
    print("\n🌀 Testing fibonacci:")
    try:
        assert fibonacci(0) == []
        print("✅ Empty sequence")
        tests_passed += 1

        assert fibonacci(1) == [0]
        print("✅ Single element")
        tests_passed += 1

        assert fibonacci(2) == [0, 1]
        print("✅ Two elements")
        tests_passed += 1

        expected = [0, 1, 1, 2, 3, 5, 8]
        assert fibonacci(7) == expected
        print("✅ Seven elements")
        tests_passed += 1

        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        assert fibonacci(10) == expected
        print("✅ Ten elements")
        tests_passed += 1

    except Exception as e:
        print(f"❌ fibonacci failed: {e}")
        tests_failed += 1

    # Test factorial
    print("\n🔢 Testing factorial:")
    try:
        assert factorial(0) == 1
        print("✅ Factorial of zero")
        tests_passed += 1

        assert factorial(1) == 1
        print("✅ Factorial of one")
        tests_passed += 1

        assert factorial(5) == 120
        print("✅ Factorial of five")
        tests_passed += 1

        assert factorial(10) == 3628800
        print("✅ Factorial of ten")
        tests_passed += 1

        assert factorial(20) == 2432902008176640000
        print("✅ Factorial of twenty")
        tests_passed += 1

        # Test error case
        try:
            factorial(-1)
            print("❌ Should have raised ValueError")
            tests_failed += 1
        except ValueError:
            print("✅ Correctly raises ValueError for negative numbers")
            tests_passed += 1

    except Exception as e:
        print(f"❌ factorial failed: {e}")
        tests_failed += 1

    # Summary
    print("\n" + "=" * 50)
    print(f"📈 Test Results: {tests_passed} passed, {tests_failed} failed")

    if tests_failed == 0:
        print("🎉 All tests passed! hello-hermes is working correctly.")
        return True
    else:
        print("❌ Some tests failed. Please check the implementation.")
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
from Activity_1 import *

run_cases = [
    (5, 6, False),
    (5, 5, False),
    (7, 6, True),
]

submit_cases = run_cases + [
    (10, 3, True),
    (2, 2, False),
    (0, 0, False),
    (10, 5, True),
    (5, 10, False),
]


def test(cadet_1_score, cadet_2_score, expected):
    print("---------------------------------")
    print(f"Inputs: {cadet_1_score}, {cadet_2_score}")
    print(f"Expecting: {expected}")
    result = cadet_1_wins(cadet_1_score, cadet_2_score)
    print(f"Actual: {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()


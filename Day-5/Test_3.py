from Activity_3 import *

run_cases = [
    (["Quantum Spanner"], 0),
    (["Quantum Spanner", "Laser Saw"], 1),
    (["Quantum Spanner", "Laser Saw", "Nutriyum", "Space Wrench"], 3),
]

submit_cases = run_cases + [
    ([], -1),
    (["Single item"], 0),
    (["Solar Shield", "Laser Saw", "Space Drill", "Med Packs", "Quantum Spanner"], 4),
    (["Solar Shield", "Laser Saw", "Space Drill"], 2),
    (["Solar Shield", "Laser Saw"], 1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = get_last_index(input1)
    print(f"Actual: {result}")
    if result == expected_output:
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


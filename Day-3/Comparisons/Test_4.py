from Activity_4 import *

def test(oxygen):
    print(f"Ship Oxygen: {oxygen}")
    print("Checking status...")
    print_status(oxygen)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()


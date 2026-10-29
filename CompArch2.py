''' 
2Q] Write a Python program to perform and verify the results of the following rotate operations on 8-bit binary numbers:
a) Rotate left without carry (ROL) on 11110110 by 2 positions.
b) Rotate left with carry (RCL) on 10000110 by 2 positions.
For each operation, display the original 8-bit binary number, demonstrate the rotation process step by step, and display the final 8-bit binary result. 
For rotate operations with carry, consider the carry flag as an additional bit and clearly indicate its initial and final values. 
Verify the program output against the results obtained through manual calculations.
'''
def rol(bin_str: str, positions: int) -> tuple[str, list[str]]:

    bits = list(bin_str)
    steps = [''.join(bits)]  

    for i in range(positions):
        msb = bits[0]                  
        bits = bits[1:] + [msb]        
        steps.append(''.join(bits))

    return ''.join(bits), steps


def rcl(bin_str: str, positions: int, initial_carry: int = 0) -> tuple[str, int, list[str]]:

    bits = list(bin_str)
    carry = initial_carry
    steps = []

    # Record initial state
    steps.append(f"Carry={carry} | {''.join(bits)}")

    for i in range(positions):
  
        new_carry = int(bits[0])
        bits = bits[1:] + [str(carry)]
        carry = new_carry
        steps.append(f"Carry={carry} | {''.join(bits)}")

    return ''.join(bits), carry, steps


def main():
    print("=" * 70)
    print("8-bit Rotate Operations")
    print("=" * 70)

    # ------------------------------------------------------------------
    # a) ROL 11110110 by 2 positions

    print("\na) Rotate Left without Carry (ROL)")
    print("-" * 50)
    original_a = "11110110"
    positions = 2

    print(f"Original 8-bit number : {original_a}")
    print(f"Operation             : ROL by {positions} positions\n")

    result_a, steps_a = rol(original_a, positions)

    print("Step-by-step process:")
    for i, state in enumerate(steps_a):
        if i == 0:
            print(f"  Initial   : {state}")
        else:
            print(f"  After {i}   : {state}")

    print(f"\nFinal 8-bit result    : {result_a}")

    # Manual verification
    print("\nManual verification:")
    print("  11110110  →  rotate left 1 → 11101101")
    print("  11101101  →  rotate left 1 → 11011011")
    print(f"  Expected : 11011011")
    print(f"  Program  : {result_a}")
    print(f"  Match    : {'YES' if result_a == '11011011' else 'NO'}")

    # ------------------------------------------------------------------
    # b) RCL 10000110 by 2 positions

    print("\n" + "=" * 70)
    print("b) Rotate Left with Carry (RCL)")
    print("-" * 50)
    original_b = "10000110"
    initial_carry = 0          

    print(f"Original 8-bit number : {original_b}")
    print(f"Initial Carry Flag    : {initial_carry}")
    print(f"Operation             : RCL by {positions} positions\n")

    result_b, final_carry, steps_b = rcl(original_b, positions, initial_carry)

    print("Step-by-step process (9-bit view: Carry | data):")
    for i, state in enumerate(steps_b):
        if i == 0:
            print(f"  Initial   : {state}")
        else:
            print(f"  After {i}   : {state}")

    print(f"\nFinal 8-bit result    : {result_b}")
    print(f"Final Carry Flag      : {final_carry}")

    # Manual verification
    print("\nManual verification (starting with CF=0):")
    print("  Initial : CF=0 | 10000110")
    print("  Step 1  : CF becomes 1, data becomes 00001100  →  CF=1 | 00001100")
    print("  Step 2  : CF becomes 0, data becomes 00011001  →  CF=0 | 00011001")
    print(f"  Expected result : 00011001 , Final CF = 0")
    print(f"  Program  result : {result_b} , Final CF = {final_carry}")
    match = (result_b == "00011001" and final_carry == 0)
    print(f"  Match           : {'YES' if match else 'NO'}")

    print("\n" + "=" * 70)
    print("Notes:")
    print("- ROL : bit that leaves MSB position re-enters at LSB (no carry involved).")
    print("- RCL : the carry flag acts as a 9th bit. MSB → CF, old CF → LSB.")
    print("- Initial Carry Flag is assumed 0 (standard convention when not specified).")
    print("=" * 70)


if __name__ == "__main__":
    main()

# Name : Mayur
#  USN : 1NH26AI806-T
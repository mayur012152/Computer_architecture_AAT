'''
1Q] Develop a Python program to perform signed binary arithmetic using the 16-bit 2's complement representation. 
Use the program to verify the results of the following arithmetic expressions:
a)	(35 - (+29))
b)	((-35) - (-12))
For each expression, display the operands in 8-bit 2's complement binary format, perform the binary arithmetic operation, 
and display the final result in both binary and decimal formats. 
Verify the program output against the results obtained through manual binary calculations and identify any arithmetic overflow..
'''

BITS_INTERNAL = 16  
BITS_DISPLAY = 8    


def to_twos_complement(n: int, bits: int) -> str:
    if n < 0:
        n = (1 << bits) + n
    mask = (1 << bits) - 1
    return format(n & mask, f'0{bits}b')


def from_twos_complement(bin_str: str) -> int:
    bits = len(bin_str)
    val = int(bin_str, 2)
    if bin_str[0] == '1':  
        val -= (1 << bits)
    return val


def add_binary(a: str, b: str) -> tuple[str, bool]:

    bits = len(a)
    sum_val = int(a, 2) + int(b, 2)
    
    # Keep only bits bits (modulo 2^bits)
    result = format(sum_val & ((1 << bits) - 1), f'0{bits}b')
    
    # Overflow detection (signed)
    sign_a = a[0]
    sign_b = b[0]
    sign_r = result[0]
    overflow = (sign_a == sign_b) and (sign_r != sign_a)
    return result, overflow


def subtract(a_dec: int, b_dec: int, bits: int = BITS_INTERNAL) -> dict:

    a_bin = to_twos_complement(a_dec, bits)
    b_bin = to_twos_complement(b_dec, bits)

    b_inv = ''.join('1' if c == '0' else '0' for c in b_bin)
    one = '0' * (bits - 1) + '1'
    neg_b, _ = add_binary(b_inv, one) 
    
    result_bin, overflow = add_binary(a_bin, neg_b)
    result_dec = from_twos_complement(result_bin)
    
    return {
        'a_dec': a_dec,
        'b_dec': b_dec,
        'a_bin': a_bin,
        'b_bin': b_bin,
        'neg_b_bin': neg_b,
        'result_bin': result_bin,
        'result_dec': result_dec,
        'overflow': overflow,
        'bits': bits
    }


def display_8bit(n: int) -> str:

    return to_twos_complement(n, BITS_DISPLAY)


def main():
    print("=" * 70)
    print("16-bit 2's Complement Signed Binary Arithmetic")
    print("(Operands shown in 8-bit 2's complement as requested)")
    print("=" * 70)

    expressions = [
        ("a) 35 - (+29)", 35, 29),
        ("b) (-35) - (-12)", -35, -12),
    ]

    for label, a, b in expressions:
        print(f"\n{label}")
        print("-" * 50)
        
        # Display operands in 8-bit
        a8 = display_8bit(a)
        b8 = display_8bit(b)
        print(f"Operand A ({a:4d}) in 8-bit 2's complement: {a8}")
        print(f"Operand B ({b:4d}) in 8-bit 2's complement: {b8}")
        
        # Perform in 16-bit
        res = subtract(a, b, BITS_INTERNAL)
        
        print(f"\nInternal 16-bit representation:")
        print(f"  A:     {res['a_bin']}")
        print(f"  B:     {res['b_bin']}")
        print(f"  -B:    {res['neg_b_bin']}  (2's complement of B)")
        print(f"  A+(-B):{res['result_bin']}")
        
        print(f"\nResult:")
        print(f"  Binary (16-bit): {res['result_bin']}")

        res8 = display_8bit(res['result_dec'])
        print(f"  Binary (8-bit view): {res8}")
        print(f"  Decimal: {res['result_dec']}")
        print(f"  Arithmetic Overflow: {'YES' if res['overflow'] else 'NO'}")
        
        # Manual verification note
        expected = a - b
        print(f"\nManual check: {a} - ({b}) = {expected}")
        if res['result_dec'] == expected and not res['overflow']:
            print("  ✓ Program result matches manual calculation. No overflow.")
        elif res['result_dec'] == expected:
            print("  ✓ Result correct, but overflow flag set (check range).")
        else:
            print("  ✗ Mismatch or overflow occurred.")

    print("\n" + "=" * 70)
    print("Notes:")
    print("- Subtraction performed as A + (2's complement of B).")
    print("- Overflow detected when signs of operands match but result sign differs.")
    print("- For these small values, results fit comfortably in both 8-bit and 16-bit.")
    print("=" * 70)


if __name__ == "__main__":
    main()

# Name : Mayur
#  USN : 1NH26AI806-T
def quick_exp_calc(base: int, exponent: int) -> int:
    '''
    Time Complexity: O(logn)
    Space Complexity: O(1)
    '''
    if exponent == 0:
        ### anything's power of 0 is one
        return 1
    elif exponent % 2 ==0:
        ### if the exponent is an even number, just divide it into half, which is:
        ### m^(n//2) * m^(n//2) = m^n
        return quick_exp_calc(base, exponent//2) * quick_exp_calc(base, exponent//2)
    else:
        ### if the exponent is a odd number, you need to compensate an additional multiplier to the result,
        ### which is: m * m^(n//2) * m^(n//2) = m^n
        return base * quick_exp_calc(base, exponent//2) * quick_exp_calc(base, exponent//2)

if __name__ == "__main__":
    print(quick_exp_calc(5,3))
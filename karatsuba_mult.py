

# x = str(1234)
# y = str(5678)

x = str(3141592653589793238462643383279502884197169399375105820974944592)
y = str(2718281828459045235360287471352662497757247093699959574966967627)

def karatsuba_multi(x, y):
    print(x)
    print(y)

    # base case
    if len(x) == 1 and len(y) == 1:
        return str(int(x)*int(y))
    else:
        n = len(x)
        # n_y = len(y)

        mid_n = n // 2
        # mid_n_y = n_y // 2

        left_half_x = x[:mid_n]
        right_half_x = x[mid_n:]

        left_half_y = y[:mid_n]
        right_half_y = y[mid_n:]
        

        ac = karatsuba_multi(left_half_x, left_half_y)
        ad = karatsuba_multi(left_half_x, right_half_y)
        bc = karatsuba_multi(right_half_x, left_half_y)
        bd = karatsuba_multi(right_half_x, right_half_y)
        
        ad_bc = int(ad) + int(bc)

        # print('ac', ac, 'ad', ad, 'bc', bc, 'bd', bd, 'ad_bc', ad_bc)

        result = int(ac) * 10**n + int(ad_bc)*10**mid_n + int(bd)

        return str(result) 




if __name__ == "__main__":
    
    print(karatsuba_multi(x, y))





















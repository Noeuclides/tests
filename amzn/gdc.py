def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    count = 0 
    gcd = 1
    arr.sort()
    for i in range(num):
        n = arr[i]
        for j in range(num):
            print("n = ",n)
            if arr[j] % n == 0:
                count = count + 1 
        print("COUNT: ", count)
        print("NUM", num)
        print(num==count)
        if count == num:
            print("IN")
            gcd = n 
            print("gcd", gcd)
        count = 0
    print("gcd", gcd)
    return gcd

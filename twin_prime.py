import math

#twin prime : http://mathworld.wolfram.com/TwinPrimes.html
#fast prime number : https://www.rookieslab.com/posts/fastest-way-to-check-if-a-number-is-prime-or-not
def isPrime(n):
    """check if is prime number"""
    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we
    # can skip middle five numbers
    # in below loop
    if n%2 == 0 or n%3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)+1), 6):
        if n%i == 0 or n%(i + 2) == 0:
            return False

    return True

j = 6;
pair_num = 1;
target = 10**5
while j < target:
    if isPrime(j-1) and isPrime(j+1):
        #print("prime is " + str(j-1) + ", " + str(j+1))
        pair_num = pair_num + 1;
    j = j + 6;

print("total " + str(pair_num))
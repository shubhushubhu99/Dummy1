print("Enter the Binary Number: ", end="")

bnum = int(input())

dnum = 0

m = 1

blen = len(str(bnum))

for k in range(blen):

    rem = bnum%10

    dnum = dnum + (rem * m)

    m = m * 2

    bnum = int(bnum/10)

print("\nEquivalent Decimal Value = ", dnum)

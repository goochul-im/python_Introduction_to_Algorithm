# p.947 유클리드 알고리즘

def euclid(a, b):
    if b == 0:
        return a

    else:
        return euclid(b, a % b)


print(euclid(30, 21))

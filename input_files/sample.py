def f1(a, b):
    x = "f2.f2"
    z = 1.2
    p = 1
    if numpy.random.randint(10) > 5:
        x = 1
    else:
        y = [1, 2]
    for i in ['str', 1.2, [1]]:
        if numpy.random.randint(10) > 2:
            z = i
            p += z
        else:
            y = (1, 2)
    z = y + a
    y = a.copy()
    x *= a
    x = a * b

    return z

def f2(i, j):
    x = f1(i, 1)
    y = f1([1], 1)
    x = i * y

    x = y = "s.t.r.".split(".")
    z = x + y
    a = 1
    p = False
    if numpy.random.randint(15) > 1:
        a = p * i
    else:
        z = x
    while numpy.random.randint(1000) > 1:
        a *= j
        if numpy.random.randint(10) > 5:
            p *= z
        else:
            z.append(a)
            p = z.index(j)
    return a

def f3(a, b):
    x = a and b
    y = numpy.random.randint(10)
    if x:
        y += 1.0
    else:
        y += False

    x = "1 test"
    x = x.index("1")
    z = str(x)

    if numpy.random.randint(10) > 5:
        y = [1]

    z = a * y
    x = f2(x, y) * 2
    y = b + x
    z = str(y) + str(z)

    for x in range(3):
        z += b

def f4(a):
    k = ~[1, 2, 3]
    j = "str" + 1
    x = "str"
    y = len(x)
    z = x + y
    i += x
    x = {1, 2}
    y = list(x)
    i = foo()
    i = numpy.foo()
    z = a.copy()
    z *= y
    for i in 1:
        print(i)
    x = f3(a,'a')
    if numpy.random.randint(3) > 2:
        x = z + a
    z = a.pop()
    x += "str"
    return x







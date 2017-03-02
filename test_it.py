def testit():
    yield 1
    yield 2
    yield 3


def testit2():
    n = 0
    while True:
        n += 1
        if n >= 100:break
        yield n

it = testit2()

try:
    while True:
        print(next(it))
except StopIteration as e:
    print("StopIterationが発生したよ",end=" ")
    print(e)
finally:
    print("終わりです")

def testit():
    yield 1
    yield 2
    yield 3

it = testit()

try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration as e:
    print("StopIterationが発生したよ",end=" ")
    print(e)
finally:
    print("finallyに来たよ終わりだよ")

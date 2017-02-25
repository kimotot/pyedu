def sumArgs(*args):
    ''' 可変引数の総和を求める関数
        引数として数値が与えられることを前提にしている
        文字列などの計算不可な項目が存在するかチェックしていない
        :type args: 引数　数値であること
        :rtype: 数値'''


    return sum(args)

if __name__ == "__main__":
    print(sumArgs(1,2,3))
    print(sumArgs(1,2,3,4,5))
    print(sumArgs(1,2,3,4,5,6,7,8,9,10))
    print(sumArgs(10.1,20.22,30.3456))
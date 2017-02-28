# フィボナッチ数列を返却するイテレータクラスのモジュールファイル

class Fibo:
    '''フィボナッチ数列を列挙するイテレータクラス'''

    def __init__(self, max = -1):
        ''' フィボナッチ数を何番目まで生成するか、最大個数（項数）を設定する
            2から始まり、正の整数値とする
            引数が2以下の場合は、強制的に1を設定する
            引数が設定されなかった場合は、max値を-1と設定し、無限に計算を継続するものとする
        '''
        if max < 0:
            self._max = -1
        elif 0 <= max < 2:
            self._max = 1
        else:
            self._max = max

    def __iter__(self):
        '''イテレータとして初期化する'''
        self._fibo_list = []        # 求めたフィボナッチ数をクラス内部で保持するためのリスト
        self._n = 0                 # リストに保持しているフィボナッチ数列の最大項番号 0から数える
        return self

    def __next__(self):
        '''次のフィボナッチ数を計算して返す'''
        while (self._max == -1) or (self._n <= self._max):
            if self._n == 0:
                t = 0
            elif self._n == 1:
                t = 1
            else:
                t = self._fibo_list[self._n - 1] + self._fibo_list[self._n - 2]

            self._fibo_list.append(t)
            self._n += 1
            return t
        else:
            raise StopIteration

    @property
    def length(self):
        return len(self._fibo_list)

# 100以下の素数を列挙する
if __name__ == "__main__":
    it = Fibo(100)
#    print(next(iter(it)))
    for i,n in enumerate(it):
        print(i,n,it.length)

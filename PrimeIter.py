# 素数を列挙するイテレータクラスのモジュールファイル

class PrimeIter:
    '''素数を列挙するイテレータクラス'''

    def __init__(self, max):
        ''' 生成する素数の最大値を設定する
            値の最小値は２
            引数が２以下の数字であったら、強制的に最大値を２に設定する'''
        if max < 2:
            self._max = 2
        else:
            self._max = max

    def __iter__(self):
        '''イテレータとして初期化する'''
        self._n = 1          # 1の次の数字（２）から素数の探索を始める
        self._prime_list = []    # クラス内部で求めた素数を保持するリスト
        return self

    def __next__(self):
        '''nの次の素数を探索して返す'''
        while True:
            self._n += 1
            if self._n > self._max:
                raise StopIteration

            # 今までに見つけた全ての素数で割り切れなければ素数である
            is_prime = True

            for p in self._prime_list:
                if self._n % p == 0:
                    is_prime = False
                    break

            if is_prime:
                self._prime_list.append(self._n)
                return self._n


# 100以下の素数を列挙する
if __name__ == "__main__":
    it = PrimeIter(100)
    print(next(iter(it)))
#    for n in it:
#        print(n,end=" ")

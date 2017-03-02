# フィボナッチ数列数列を発生させるイテレータクラスのモジュールファイル

class Fib:
    '''フィボナッチ数列を列挙するイテレータクラス'''

    def __init__(self, max = -1):
        ''' 生成するフィボナッチ数列の最大項数を設定する
            値は０以上の正の整数値
            引数が0以下の数字であったら、無限に生成する'''
        if max < -1:
            self._max = -1
        else:
            self._max = max

    def __iter__(self):
        '''イテレータとして初期化する'''
        self._n = 0              # フィボナッチ数列を求め始める項番を設定する 最初は0から
        self._fib_list = []      # 求めたフィボナッチ数列をクラス内部で保持するリスト
        return self

    def __next__(self):
        '''nの次の素数を探索して返す'''
        while (self._max == -1) or (self._n <= self._max):
            if self._n <= 1:
                t = self._n
            else:
                t = self._fib_list[self._n - 1] + self._fib_list[self._n - 2]
            
            self._fib_list.append(t)
            self._n += 1
            return t
        else:
            raise StopIteration
    
    @property        #プロパティ属性をつける
    def len(self):
        '''現在求めたフィボナッチ数列の個数を返す関数'''
        return len(self._fib_list)
    
    @len.setter
    def len(self,_):
        print('このプロパティにセッターはありません')

    @len.deleter
    def len(self):
        print('このプロはティを削除できません')
        
# 100以下の素数を列挙する
if __name__ == "__main__":
    it = Fib()
    f = 0
    while f < 10000:
        f = next(iter(it))
        print(f)
    
    print(it.len,f)

#    print(next(iter(it)))
#    for i,n in enumerate(it):
#        print(i,n,it.len)
#    
#    it.len = 100
#    del it.len

'''
deque(デック)は両端キューのことで、スタックとキュー両方の機能を持っている。
popleft()はデックから左端の要素を削除する
pop()は右端の要素を削除して返す。 stackのpopに相当、要素の追加は右側に追加されていくので...
'''


def palindrome(word):
    '回文を判定するプログラム'
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print('a', palindrome('a'))
print('racecar', palindrome('racecar'))
print('""', palindrome(""))
print("halibut", palindrome("halibut"))

'''
実際高速な回文チェッカーが必要なら、逆順の文字列と比較した方が早い。
python にはerverse()がないが、スライスを使うことで逆順の文字列を作れる
'''
def another_palindrome(word):
    return word == word[::-1]

print('\n高速版')
print('a', another_palindrome('a'))
print('racecar', another_palindrome('racecar'))
print('""', another_palindrome(""))
print("halibut", another_palindrome("halibut"))


print('cycle()は無限反復子で、引数から循環的に要素を返す')
import itertools
'''
for item in itertools.cycle([1,2]):
    print(item)
'''

print('\n accumulate()は、要素を一つにまとめた値を計算する。デフォルトは合計値')
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
print(itertools.accumulate([1, 2, 3, 4]))

print('この関数は第二引数に関数を受け付ける。この関数はにこの引数を受け付け、一個の結果を返すものでなければならない')

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
'''
itertoolsモジュールはこれら以外にも多くの関数を定義している。特に、順列、組み合わせの関数は、必要な時には時間の節約になる。
'''
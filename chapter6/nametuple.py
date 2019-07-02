'''
名前付きタプルはタプルのサブクラスでオフセット[offset]だけでなく名前(.name)でも値にアクセスできる
namedtuple関数には
名前
空白区切のフィールド名の文字列
の引数を渡す
'''

from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

print('\n名前付きタプルは辞書からも作れる')
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

'''
**partsはキーワード引数でparts辞書のキーと値を抽出して引数として渡す。次のように書くのと同じである
'''
duck2 = Duck(bill = 'wide orange', tail = 'long')

'''
名前付きタプルはイミュータブルだが、一個以上のフィールドを交換した別の名前付きタプルを返すことはできる。
'''

duck3 = duck2._replace(tail = 'magnificent', bill='crushing')
print(duck3)

print('\n辞書にはフィールドが追加できる')
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)
duck_dict['color'] = 'green'
print(duck_dict)

print('\nが名前付きタプルには追加できない。')
'''
名前付きタプルのメリット
イミュータブルなオブジェクトのように振る舞う
オブジェクトよりも空間的にも、時間的にも効率がいい
ドット記法で属性にアクセスできる
辞書のキーとして使える
'''
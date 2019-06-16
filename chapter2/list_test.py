#python 文法復習 list編

empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekdays)
another_empty_list = list()#list関数で空リストを作ることもできる。

cat_list = list('cat')#文字列を１文字ごとの文字列リストに変換
print(cat_list)

a_tuple = ('ready', 'fire', 'aim')#tapbe imutable
tuple_to_list = list(a_tuple)
print(tuple_to_list)

birthday = '1/6/1952'
birthday = birthday.split('/')
print(birthday)

marxes = ['Groucho', 'Chigo', 'Harpo']
print(marxes[0])
print(marxes[-1])
print(marxes[:])
print(marxes[::2])
print(marxes[:2])
print(marxes[::-1])

list_1 = [1, 2, 3, 4, 5]
list_2 = [2, 4, 6]
list_3 = 100
list_of_list = [list_1, list_2, list_3]
print(list_of_list)
print(list_of_list[1])
print(list_of_list[1][2])

list_of_list[0][2] = 999
print(list_of_list[0])
list_of_list[0] = [1, 2, 3, 4, 5]
print(list_of_list)

marxes.append('Xeppo')
print(marxes)

others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

#appendを使うとothersが1個のリストの要素として追加されてしまう
#marxes.append(others)
#print(marxes)

marxes.insert(3, 'Gummo')
print(marxes[3])
marxes.insert(10, 'Karl')
print(marxes)

#del はpythonの文である。delは代入の逆のようなもので、Pythonオブジェクトから名前を切り離し、その名前がオブジェクトへの最後の参照なら、オブジェクトのメモリを解放する。
del marxes[-1]
print(marxes)
del marxes[2]
print(marxes)
del marxes[-2:]
print(marxes)

marxes.append('Zeppo')
print(marxes)
marxes.remove('Gummo')
print(marxes)


marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())#リストから要素を取り出し、同時にリストからその要素を削除する
print(marxes)
print(marxes.pop(1))

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.append('Chico')
print(marxes.index('Chico'))#1番目のindexを返してる

print('Groucho' in marxes)#少なくとも1箇所に値があればinはTrueを返す

print(marxes.count('Chico'))#リスト内に何個含まれているか

#join()による文字列への変換
separator = ', '
marxes = ['Groucho', 'Chico', 'Harpo']
marxes = separator.join(marxes)#要素の間に, を足して文字列に結合 #joinはsplitの逆
print(marxes)
marxes = marxes.split(separator)
print(marxes)

#sort()はその場でリスト自体をソートする
#sorted()はソートされたリストのコピーを返す
sorted_marxes = sorted(marxes)
print(sorted_marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse = True)
print(numbers)


#＝による代入とcopy()によるコピー
a = [1, 2, 3]
b = a #アドレスの代入であるということ
a[0] = 'surprise'
print(b)
a[0] = 1

#コピーの方法
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'surprise'
print(a)
print(b)
print(c)
print(d)
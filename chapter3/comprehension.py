print('listは一度に一つずつ要素を追加しても作れる')
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

print('\nforとrangeでも作れる')
number_list = list()
for k in range(1,6):
    number_list.append(k)
print(number_list)

print('\nrange()の出力を直接リストにもできる')
number_list = list(range(1,6))
print(number_list)


print('\nリスト内包表記を使ったリストの作成')
number_list = [number for number in range(1, 6)]
print(number_list)

number_list = [number-1 for number in range(1,6)]
print(number_list)

print('\nリスト内包表記には条件式も追加できる')
print('[expression for item in iterable if condition]')
a_list = [number for number in range(1, 6) if number % 2 ==1]
print(a_list)

print('\n内包表記でもforを複数使うことができる、まずは古くのネストされたループを見る')
rows = range(1,4)
cols = range(1,4)
for row in rows:
    for col in cols:
        print(row, col)

print('\n包括表記を使って(row, col)形式のタプルにして, cells変数に代入する')
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

print('\nタプルのアンパックを使ってタプルから値を引き抜く')
for row, col in cells:
    print(row, col)

print('\nリスト内包表記のそれぞれのforにifテストをつけられる')
cells = [(row, col) for row in rows if row % 2 == 0 for col in cols if col %2 ==1]
for cell in cells:
    print(cell)


print('\nジェネレータ内包表記')
#実はタプルには内包表記がない、リスト内包表記のすみかっこを普通のかっこに変えれば、タプル内包表記ができると思われたかもしれない
number_thing = (number for number in range(1, 6))
print(number_thing)
#()ないのものはジェネレータ内包表記であり、とこのようにジェネレータオブジェクトを返してしまう
print('\nジェネレータオブジェクトは直接forループで処理できる')
for number in number_thing:
    print(number)

print('\nジェネレータ包括表記をlist()でラップすればリスト内包表記のように動作させられる')
print('\nジェネレータは一度しか実行できない')
number_thing = (number for number in range(1, 6))
number_list = list(number_thing)
print(number_list)
number_list = list(number_thing)
print(number_list)

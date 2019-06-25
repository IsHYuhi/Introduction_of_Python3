#関数の定義 先頭は英字か_で始める
def do_nothing():
    pass

def make_a_sound():
    print('quack')

def agree():
    return True

#呼び出す時に渡す引数が実引数で、関数内で使われる引数が仮引数である
def echo(anything):
    return anything + ' ' + anything

def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == "bee purple":
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color +"."

do_nothing()
make_a_sound()

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

print(echo('Rumplestiltskin'))
comment = commentary('blue')
print(comment)

print("関数が明示的にreturnを呼び出さなければ呼び出し元は戻り値としてNoneを受け取る")
print(do_nothing())

print("Noneはブール値として評価すると偽になるが、厳密には同じではない")
print("FalseとNoneを区別するためにはis演算子を使う")
if do_nothing() is None:
    print("It's nothing")
else:
    print("It's something")

print("Noneはからの値と存在しない値を区別するために必要である。p.113")


print("\n先頭から順に対応する位置の仮引数にコピーされる位置引数がある")
def menu(wine, entree, dessert = 'pudding'):
    return{'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay', 'chiken', 'cake'))

print("\n一引数の混乱を避けるために対応する仮引数の名前を指定して実引数を指定するキーワード引数がある")
print(menu(entree = 'beef', dessert= 'bagel', wine='bordeaux'))

print("\nまた位置引数とキーワード引数の併用もできる")
print("先に位置引数を指定しなければならない")
print(menu('frontenac', dessert='flan', entree='fish'))

print("\n仮引数にはデフォルト値を指定できる。呼び出し元が対応する実引数を渡さなかった時に使われる")
print(menu('chardonnay', 'chiken'))
print(menu('chardonnay', 'chiken', 'doughnut'))


print("\デフォルト引数の値が計算されるのは、関数が実行された時ではなく定義された時である。リストや辞書などのミュータブルなデータ型をデフォルト引数値として使わない")
print("次の関数は2回目に呼び出された時にresultは前回の呼び出しでセットされた一個の要素が残ってしまう")
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')

print("\n正しくはこう")

def works(arg):
    result = []
    result.append(arg)
    print(result)
works('a')
works('b')

print("\n最初の呼び出しだということを示す別のものを渡すという方法もある")
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')








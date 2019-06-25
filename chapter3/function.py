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

print("\n*による位置引数のタプル化")
#ポインタを連想するかもしれないがpythonにポインタはない。
#この機能は、print()のように可変個の実引数を受け付ける関数を書く時に役立つ
#必須の位置引数がある場合には、位置引数の最後に*argsを書くと、必須引数以外の全ての位置引数を一つにまとめることができる。
#*を使う時タプル仮引数をargsと呼ぶ必要は特にないが、Pythonコミュニティでは一般的な慣習となっている
def print_args(*args):
    print('Positional argument tuple: ', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one: ', required1)
    print('Need this one too: ', required2)
    print('All the rest: ', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

print("\n**によるキーワード引数の辞書化")
#**を使えば、キーワード引数を一個の辞書にまとめることができる。引数の名前は辞書のキー、引数の値は辞書の値になる
#一般的にこの引数を**kwargsと呼ぶことが多い
'''位置引数をまとめる*argsと**kwargsを併用する場合、この二つはこの順序で並べなければならない'''
def print_kwargs(**kwargs):
    print('Keyword arguments: ', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

print('\ndocstring')
#関数本体の先頭に文字列を組み込めば、関数定義にドキュメントをつけることができる
#これを関数のdocstringと呼ぶ

def echo_2(anything):
    'echo_2は、与えられた入力引数を返す'
    return anything

def print_if_true(thing, check):
    '''
    第二引数が真なら、第一引数を表示する
    処理内容:
        1. *第2*引数が真かどうかをチェックする
        2. 真なら*第1*引数を表示する
    '''
    if check:
        print(thing)

print('docstringを表示するためにはhelp()関数を呼び出す、綺麗に成形されたdocstringが返される')

#help(echo_2) #実行するたびに表示されるのでここではコメントアウト
print("整形前の素のままのdocstringを見たい場合には次のように書く")
print(echo_2.__doc__)


print('\npythonでは全てのものがオブジェクトである、もちろん関数も含まれる')

def answer():
    print(42)

def run_something(func):
    func()
print('pythonはかっこがなければ関数を他のオブジェクトと同じように扱う')
run_something(answer)
print(type(run_something))


def add_args(arg1, arg2):
    print(arg1+arg2)
print(type(add_args))
#add_argsのタイプはfunction

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

print("\nこれに*args, **kwargsのテクニックを組み合わせてみる")

def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args) #*をつける

print(run_with_positional_args(sum_args, 1, 2, 3, 4))

print("\n関数内関数")
print('関数を他の関数のなかで定義することができる')
def outer(a, b):
    def inner(c, d):
        return c+d
    return inner(a, b)

print(outer(4, 7))

print("\n関数内関数はループやコードの重複を避けるために役立つ")
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s' " % quote
    return inner(saying)

print(knights('Ni!'))


print("\nクロージャ")
print('クロージャとは、他の関数によって動的に生成される関数で、その関数の外で作られた変数の値を覚えておいたり、変えたりできる')
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s' " % saying
    return inner2
#inner2()はknight2に渡されたsayingの値を知っており、覚えている。
#inner2は動的に作成された関数であり、どのように作成されたかを覚えている。これがすなわちクロージャである。
a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(a())
print(b())

print('\n無名関数:ラムダ関数')
print('ラムダ関数は、一つの文で表現される無名関数である')
def edit_story(words, func):
    for word in words:
        print(func(word))
#この関数を試すには、単語のリストとここの単語に適用される関数が必要である。
stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)

print('\nenliven()関数はとても短いのでラムダに取り替える')
edit_story(stairs, lambda word: word.capitalize() +'!')
#ラムダを使うよりも本物の関数を使った方がコードが明確になることが多いが、ラムダを使わなければ小さな関数を作っていくつも名前を覚えておかなければならなくなる。


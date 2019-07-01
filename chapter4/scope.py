print('プログラムのメイン部分は、グローバル名前空間を定義する')
#global変数
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

print('関数内で一度グローバル変数を取得したあとだと、ローカル変数ではなくグローバル変数と認識され書き換えようとするとエラーが起きる')
print('なので関数内からローカル変数ではなく、グローバル変数の方にアクセスするには、globalキーワードを用いる')
'''
関数内でglobalと書かなければ、pythonはローカル名前空間を使い、animal変数はローカルになる。関数が終わったらローカル変数は消えて無くなる
locals(): ローカル名前空間の内容を示す辞書を返す
globals():グローバル名前空間の内容を示す辞書を返す
'''
def change_and_print_global():
    global animal
    print(animal)
    animal = 'wombat'
    print(animal)

def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))
    print('locals:', locals())

change_local()
print('globals:',globals())
change_and_print_global()


print('\n名前の中の_と__')
'''
先頭と末尾が2個のアンダースコアになっている名前はpythonが使う変数wとして予約されている。自分自身の変数としてこの種のものを使ってはならない
'''

def amazing():
    '''これは素晴らしい関数だ。
    もう一度みる?'''
    print('この関数の名前:', amazing.__name__)
    print('docstring:', amazing.__doc__)#整形前のdocstiringを見たい時、整形後が見たい時はhelp(function)

amazing()
'''
また、globals()から分かるようにメインプログラムには__main__という特別な名前が与えられている。
'''


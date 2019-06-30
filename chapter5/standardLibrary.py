print('setdefault()とdefaultdict()による存在しないキーの処理')

periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
'''
存在しないキーで辞書にアクセスしようとすると、例外が発生する。
辞書のget()関数を使って、キーが存在しない場合はデフォルト値を返すようにすることができる。
setdefault()はキーがなければさらに辞書を追加することができる
'''
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

print('\n既存のキーに別のデフォルト値を代入しようとしても、元の値が返され、辞書は一切変更されない')

helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)

'''
defaultdict()も例外を防ぐという点では似ているが、辞書作成時にあらゆるキーのためのあらかじめデフォルト値を設定するところが異なる。
引数は関数である。
'''
from collections import defaultdict
periodic_table = defaultdict(int)

'''これで、存在しないキーに対する値は整数(int)の0になる'''
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])
print(periodic_table)

'''
defaultdict()に存在しないキーを用いた場合、そのキーが自動で生成される。
そのキーの値は、defaultdict()に渡された型が設定される。
次の例では値が必要になった時にno_idea()が呼び出される
'''

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A']= 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['C'])
print(bestiary)

print()

'''
int(), list(), dict()を使えば、これらの方のからの値を返して存在しないキーのデフォルト値にすることができる
int() : 0
list() : 空のリスト[]
dict(): 空辞書{}
デフォルト値引数を省略すると、新しいキーに与えられるデフォルト値はNoneになる
'''

print('intは独自のカウンタを作るための手段になる')
bestiary = defaultdict(lambda: 'Huh')#無名関数
print(bestiary['E'])

food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

''' もし通常の辞書だったら初期化が必要になる'''
dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] +=1

for food, count in dict_counter.items():
    print(food, count)


print("\nCounter()による要素数の計算")

from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)#Counterで返す

print('most_common()は全ての要素を降順で返す。引数で整数を指定すると最上位から数えてその個数分だけを表示する')
#タプルのリストで返す
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))


print('\nカウンタを結合することもできる')


lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print('lunch:',lunch_counter)
print('breakfast:',breakfast_counter)
print(breakfast_counter + lunch_counter)
print('''朝食では使われているが昼食では使われていないもの -の要素は表示されない''')
print(breakfast_counter - lunch_counter)
print('''昼食では使われているが朝食では使われていないもの''')
print(lunch_counter - breakfast_counter)
print('''共通要素''')
print(lunch_counter & breakfast_counter)
print('''和集合''')
print(lunch_counter | breakfast_counter)

print('\nOrderedDict()によるキー順のソート')
'''
辞書のキーの順序は予測不可能である
'''
quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow',
    'Curly': 'Nyuk nyuk!',
    }
for stooge in quotes:
    print(stooge)

print('\nOrderdDict()は、キーが追加された順序を覚えている')

from collections import OrderedDict
quotes = OrderedDict([('Moe','A wise guy, huh?'), ('Larry', 'Ow'), ('Curly', 'Nyuk nyuk!')])
for stooge in quotes:
    print(stooge)


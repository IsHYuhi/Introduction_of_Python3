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




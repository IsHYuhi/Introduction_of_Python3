#辞書の文法復習 他の言語では連想配列、ハッシュ、ハッシュマップなどと呼ばれている ミュータブル
empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
    }#pythonではリスト、タプル、辞書の最後の要素の後ろにカンマを残しておいていい、また、インデントも見やすいだけで実際には不要
print(bierce)

#dict()を使った変換
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]#list of list
print(dict(lol))

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')] #list of tuple
print(dict(lot))

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])#tuple of list
print(dict(tol))

los = [ 'ab', 'cd', 'ef'] # list of string
print(dict(los))

tos = ('ab', 'cd', 'ef')#tuple of string
print(dict(tos))


#keyによる要素の追加、変更

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }
print(pythons)

pythons['Gilliam'] = 'Gerry'
print(pythons)

pythons['Glliam'] = 'Terry'#同じキーを使って値を置き換えている
print(pythons)

#update()による辞書の結合
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }
print(pythons)

others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)#辞書のキーと値を別の辞書にコピーできる
print(pythons)

first = {'a':1, 'b':2}
second = {'b': 'platypus'}
first.update(second)#キーが重複している場合第二の辞書の値が残る
print(first)

del pythons['Marx']#指定したキーを持つ要素の削除
del pythons['Howard']
print(pythons)


pythons.clear()#clear()による全ての要素の削除
pythons = {} #こっちでもいい
print(pythons)


pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }

print('Chapman' in pythons)#キーがあるかどうか


print(pythons['Cleese'])
print(pythons.get('Cleese'))# キーがあればその値が返される。
print(pythons.get('Marx', 'Not a Python'))#キーがなければオプションが返される
print(pythons.get('Marx'))#オプションがなければNoneが返される。


#keys()による全てのキーの取得
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'smile for the camera',
    }
print(signals.keys())

print(list(signals.keys()))#dict_keyオブジェクトをリストに変換するためにはlist()を呼び出す

#values()による全ての値の取得
print(signals.values())
print(list(signals.values()))

#items()による全てのキー/値ペアの取得
print(signals.items())
print(list(signals.items()))

#リストの場合と同様に辞書に変更を加えると、その辞書を参照している全ての名前に影響が及ぶので別の辞書にコピーしたい場合はcopy()を使う

original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

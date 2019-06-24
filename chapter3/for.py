#イテレータ:イテレーションごとにリスト、辞書などから要素を一つずつ取り出して返すもの

print('シンプルなシーケンス処理')
rabbits = ['Flopsy', 'Mopsy', 'Cttontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current +=1

print('\nイテレータを用いた処理')#javaの拡張forループと似ている、というかほぼ一緒
for rabbit in rabbits:
    print(rabbit)

print('\n文字列をforで処理すると一度に１字ずつ文字が生成される')
word = 'cat'
for letter in word:
    print(letter)


print('\n辞書または辞書のkeys関数をforで処理すると、キーが返される')
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:
    print(card)


print('\n値を出力したいなら、辞書のvalues()関数を使う')
for value in accusation.values():
    print(value)

print('\nkey, valueをタプルで返したい時はitems()を使う')
for item in accusation.items():
    print(item)

print('\nタプルの各要素を個別の変数に代入する')
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)


print('\nbreakによる中止とcontinueによる次のイテレーションの開始が可能')
print('''forは正常に終了したかどうかチェックをするオプションのelseがある
breakが呼び出されなければelseが実行される''')
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is no much of a cheese shop, is it?')

print('zip()を使った複数のシーケンスの反復処理')
print('最も小さいサイズのシーケンスの要素を処理し尽くした時に止まる')
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['triramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ":drink", drink, "- eat", fruit, "- enjoy", dessert)

print('''dictは、タプル、リスト、文字列などの2要素のシーケンスから辞書を作れる
zip()を使えば、複数のシーケンスを辿って、オフセットが共通する要素からタプルを作れる''')
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))#dict(二つの要素を持つタプルたち)からdictを作れる

print('range()による数値シーケンスの生成')
print('range(start, end, step) 必須引数はend, [start, end)')

for x in range(0, 3):
    print(x)

print(list(range(0,3)))

for x in range(2, -1, -1):
    print(x)

print([x for x in range(0, 11, 2)])#内包表記

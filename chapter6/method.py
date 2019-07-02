'''
メソッドのタイプ
メソッドの第一引数がselfであればインスタンスメソッドである。普通書くタイプのメソッド
@classmethodというでコレータを入れるとその次の関数はクラスメソッドになる。
また、メソッドの第一引数は、クラス自体になり、伝統的その引数を 'cls'と呼ぶ
classが予約語で使えないため
'''

class A:
    count =0
    def __init__(self):
        A.count +=1 #ここがselfではなくAなのでクラスそのものの数をカウントしている
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.") #cls.countをA.countに変えても同じである

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

'''
また、第３のタイプのメソッドとして静的メソッドがある
@staticmethodでコレータをつけ引数を取らない。
'''

class CoyoteWeapon:
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

print('\nこのメソッドは、CoyoteWeaponクラスからオブジェクトを作らずに実行できる')
CoyoteWeapon.commercial()

'''
pythonは、ポリモーフィズムの緩やかな実装を持っている。クラスの種類にかかわらず、異なるオブジェクトに対して同じ操作を適用する
これらをダックタイピングと呼ぶ
'''

class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

'''
QuestionとExclamationの初期化の方法は親と変わらないので__init__のオーバーライドはしていない。
自動で親クラスから__init__()メソッドを呼び出す
'''
print('\nダックタイピング')
hunter = Quote('Elmer Fudd', "I'm hunnting wabbits")
print(hunter.who(), 'says:', hunter.says())

hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())

hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())

'''
正直自分はこの動作は当たり前だと思うが。。。
次の例を見るとポリモーフィズムの動作がわかる
'''

class BabblingBrook:
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

'''
要は親であるobjectに入れることができてメソッドが実行できるということ。
継承クラスの違いや、継承していなくても同じメソッドを共通のインターフェースをもつオブジェクトとして扱うことができる。
'''
who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)

print('\n特殊メソッド')
'''
+ や *などの演算子には、特殊メソッドを使うとたどり着く
'''
class Word:
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))
'''
小文字への変換と比較を実行するようにequals()メソッドを定義したが、pythonの組み込み型と同じように
if first == secondと書くことができれば便利だ。ここでequals()を__eq__()に変更する
'''

class Word2:
    def __init__(self, text):
        self.text = text

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):#javaでいうtoString()のようなもの
        return self.text
    def __repr__(self):
        return 'Word("' + self.text + '")'
first2 = Word2('ha')
second2 = Word2('HA')
third2 = Word2('eh')
print(first2 == second2)

'''
これらの演算のための特殊メソッドは他にもあるので役立つ特殊メソッドをまとめたものは入門python3のp175にまとめてある。(そのうちQiitaにでもまとめたい。。。)
'''
print('\n__str__()を定義し忘れると、オブジェクトのデフォルトの文字列バーションが使われる。定義するとしっかりtextが表示される')
print(first)
print(first2)

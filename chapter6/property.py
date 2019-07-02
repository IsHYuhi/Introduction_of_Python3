print('\nプロパティによる属性値の取得、設定')
'''
オブジェクト指向言語の中には外部から直接アクセスできない非公開のオブジェクト属性をサポートしているものがある。
そういった場合はセッターやゲッターが必要になる。
しかし、pythonは全ての属性とメソッドが公開であるので、それらを書く必要はない
が、直接のアクセスが落ち着かないという場合にはpythonらしくプロパティを使おう
'''

class Duck:
    def __init__(self, input_name):
        'ここでの__nameダブルアンダースコアつきのものはマングリングされる。詳しくは後述'
        self.__name = input_name
    def get_name(self):
        print('inside the getter')
        return self.__name
    def set_name(self, input_name):
        print('inside the setter')
        self.__name = input_name
    '''ここの最後の行がなければ通常のゲッターセッターとして機能する
    最後の行は二つのメソッドをnameというプロパティのセッターゲッターとして定義している。
    property()の第一引数はゲッターメソッド、第二引数はセッターメソッドにする'''
    name = property(get_name, set_name)

'''それでも、通常のゲッターメソッドのように直接呼び出すこともできる'''
fowl = Duck('Howard')
print(fowl.name)
print(fowl.get_name())

'nameプロパティに値を代入するとセッターが呼び出される'
fowl.name = 'Daffy'
print(fowl.name)

fowl.set_name('Howard')
print(fowl.name)

print('\nプロパティはでコレータで定義することもできる。')
'''
@property
    ゲッターメソッドの前につける
@property.setter
    セッターメソッドの前につけるデコレータ。
'''

class Duck2:
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = Duck2('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)

'''
上記の例では単一の属性__nameを参照するためにnameプロパティを使ったが、
'''
print('\nプロパティは、計算された値も参照できる。')

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2* self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

print('\nradius属性はいつでも書き換えることができ、deameterはradiusの現在の値から計算される')
c.radius = 7
print(c.diameter)

'''
プロパティのセッターを使用しなければ、外部からプロパティを設定することはできない
これを利用して読み出し専用のプロパティを作ることができる。

また、属性直接アクセスよりも優れている点は、プロパティの定義を書き換えても、クラス定義内のコードを書き換えるだけで済み、呼び出し元には手を付ける必要がないことである。
'''


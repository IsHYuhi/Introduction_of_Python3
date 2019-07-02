'''
属性の先頭に二つのアンダースコア__をつけると、外部からアクセスできなくなる。
実際に属性が非公開になるわけではないが、外部コードが偶然当てたりしないようなものになるように名前をマングリング(ぐちゃぐちゃに変形)する
'''

class Duck():
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

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)
print('そして__name属性にはアクセスできない:ここではコメントアウトしている')
#print(fowl.__name)
'マングリングによって名前が下記のように変わる'
print(fowl._Duck__name)
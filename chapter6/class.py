#継承しない時はclass Person():としない
'''
__init__()はクラス定義からここのオブジェクトを作る時にそれを初期化するメソッドにつけられた特殊名で、self引数は作られたオブジェクト自体を参照する。
必ず第一引数はselfでなければならない。コンストラクタのようなもの？？？
今回は、初期化メソッドにnameというパラメータを追加する
__init__()は同じクラスから作られた他のオブジェクトからこのオブジェクトを区別するために必要な処理をするために使われる
'''
class Person:
    def __init__(self, name):
        self.name = name

hunter = Person('Elmer Fudd')
'''
この渡されたnameは属性としてオブジェクト共に保存され、直接読み書きできる
***Personクラスの内部では,name属性にはself.nameという形でアクセスする。また外部からはhunter.nameのようにクラスのオブジェクトからアクセスする
'''
print('The mighty hunter: ', hunter.name)

print('\n継承')

class Car:
    def exclaim(self):
        print("I'm a Car!")

'継承とオーバーライド'
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")

    def need_a_push(self):
        print("A little help here?")

'''
ここではYugoはCarであるを満たすis-a関係である
__init__()を含むあらゆるメソッドをオーバーライドできる。
'''
give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

'''
先ほどのPersonクラスを使った別の例
'''

print('\nオーバーライド')
class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name+ ", Esquire"

person = Person('Fudd')
doctor = MDPerson("Fudd")
lawyer = JDPerson("Fudd")
print(person.name)
print(doctor.name)
print(lawyer.name)


print('\nメソッドの追加')
give_me_a_yugo.need_a_push()
'汎用的なCarオブジェクト(need_apush()を持たない)オブジェクトは実行できない'
#give_me_a_car.need_a_push() #error

print('superによる親クラスへのアクセス')
'''
superを使わないと継承を使っている意味がなくなってしまう。
メリットとしてはPersonの定義が将来変わっても、super()を使っていれば、EmailPersonがPersonから継承している属性やメソッドは、その変更を反映したものになる。
'''
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name, bob.email)

car = Car()
'下記の二つは同じ動作が得られる'
car.exclaim()
Car.exclaim(car)



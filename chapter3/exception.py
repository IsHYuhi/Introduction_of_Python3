short_list = [1, 2, 3]
position = 5
'''
tryブロックのコードは実行される。そこでエラーが起きると、例外が生成されexceptブロックのコードが実行される。
例外が起きなければ、exceptブロックは実行されない
'''
try:
    short_list[5]
except:
    print('Need a position between 0 and', len(short_list)-1, ' but got', position)

'''
上のように引数なしのexceptを指定すると、あらゆる例外型がキャッチされる。
複数の例外が起きる可能性がある時には、それぞれのために別々のハンドラを用意した方が良い
次のようにname変数に完全は例外オブジェクトを格納できる
except exceptiontype as name
'''

while True:
    value = input('Position [q to quite]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

'''
独自例外の作成
IndexErrorなどはpythonかその標準ライブラリで定義済みのものである。
自分のプログラムの中で発生することのある特殊な状況に対処するために独自の例外型を定義することもできる
'''
'''
ここでは UppercaseExceptionの振る舞いを定義しておらず
例外が生成された時になにを表示するべきかも、親クラスのExceptionに任せている。
'''
# '''
class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
# '''

'''
例外オブジェクト自体にアクセスして、情報を表示することもできる
'''
class OopsException(Exception):
    pass

try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)


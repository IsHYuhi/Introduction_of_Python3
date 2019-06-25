'''
ジェネレータはpythonのシーケンスを作成するオブジェクトである。
range()もジェネレータの一つで一連の整数を生成している。
 ジェネレータは、反復処理のたびに、最後に呼び出された時にどこにいたかを管理し、次の値を返す。
 大きくなる可能性があるシーケンスを作りたいが、ジェネレータ内包表記に収めるにはコードが多すぎる時にはジェネレータ関数を書く
'''
print(sum(range(1,101)))

print('\nジェネレータ関数')
#値をreturn で返す代わりにyield文で返す
def my_range(first = 0, last =10, step = 1):
    number = first
    while number < last:
        yield number
        number += step


print('my_rangeは通常の関数')
print(type(my_range))
ranger = my_range(1, 5)
print('ジェネレータオブジェクトを返す')
print(type(ranger))
for x in ranger:
    print(x)
#generatorは一度使われたら2回目は使えない
for x in ranger:
    print(x)

'''
デコレータは、入力として関数を一つ取り、別の関数を返す関数である。
ソースコードを書き変えずに既存の関数に変更を加えたいことがある。
よく知られているのは、引数として何が渡されたかをみるためのデバッグ文の追加である。
'''
print("\nデコレータ")
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a+b

print(add_ints(3, 5))
cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3, 5))



print('上のように手作業でデコレータの戻り値を代入しなくても、デコレートしたい関数の直前に@decorator_nameを追加すれば変更後の動作が得られる。')
@document_it
def sub_ints(a, b):
    return a-b
print(sub_ints(3, 5))

print('\n関数に対するデコレータは複数持てる。結果を自乗するsquare_it()という別のデコレータを書く')
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result*result
    return new_function

@document_it
@square_it
def add_ints2(a, b):
    return a + b

#逆順
@square_it
@document_it
def add_ints3(a, b):
    return a+b

print(add_ints2(3, 5))
print(add_ints3(3, 5))
print('結果から分かるように関数に近く書かれてる方から先に適応される')



# \で行の継続ができる
alphabet = 'abcdefg' + \
    'hijklmn'
print(alphabet)

bool = True
if bool:
    print('a')#1Tab is 4 space
elif bool:
    print('b')
else:
    print("c")


x=7
print(x==5)
print(x==7)
print(5<x)
print(x<10)

#and, or, notなどのブール演算子は、比較対象の要素よりも優先順位が低い
#混同しないように()を使ってもいい
print('--bool operation test--')
print(5<x and x<10)
print((5<x) and (x<10))
print(5<x and not x>10)

#pythonでは次のようにかける
print('--a<x<b--')
print(5<x<10)

print('Falseになるもの')
print(
'''
bool = False
null = None
n = 0
f = 0.0
s = ' '
list = []
tuple = ()
dic = {}
set = set()
'''
)
print('上記以外はすべてTrue')

count=0
while count <=5:
    print(count , end = "")
    count+=1
print()

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == 'q':
        break
    print(stuff.capitalize())

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 ==0:
        continue
    print(number, 'squad is', number*number)

#elseによるbreakのチェック
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: #breakが呼び出されていない whileループが正常終了したら制御はオプションのelseに渡される
#breakチェッカーと考えるといい
    print('No even number found')



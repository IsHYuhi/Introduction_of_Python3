'''
pythonアプリケーションをもっと大規模なものにするために、モジュールはパッケージと呼ばれる階層構造に組織することができる
例えばsourcesというディレクトリを作り、その中にdaily.pyとweekly.pyの二つのモジュールを作って、両方のモジュールにforecastという関数を作る
'''

from sorces import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
#enumerate()関数は、リストを分解してforループにリストのここの要素を供給する、またここの要素に番号を追加する
for number, outlook in enumerate(weekly.forecast(), 1):#1から番号をつける
    print(number, outlook)


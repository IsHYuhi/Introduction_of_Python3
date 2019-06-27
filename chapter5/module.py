import sys
print('Program arguments:', sys.argv)

'''
import module
他のPythonファイルのファイル名から拡張子の.pyを取り除いたもの
'''

import report #同じディレクトリにおく
'''これはreportモジュールの全体をインポートしているためdescription()のプレフィックスとしてreport.を使わなければならない。
こうすることで他のモジュールにget_description()関数があっても、間違ってそれを呼び出すことはない'''
description = report.get_description()
print("Today's weather:", description)

'''同じ名前の別のモジュールが必要な時や、もっと簡潔な名前を使いたい時は別名を使ってインポートできる '''
import report as wr
description = wr.get_description()
print("Today's weather:", description)

'''必要なものだけをインポートする方法'''
from report import get_description
description = get_description()
print("Today's weather:", description)

from report import get_description as do_it
description = do_it()
print("Today's wheather:",description)

'''
モジュールサーチパス
標準のsysモジュールのpath変数に格納されているディレクトリ名やZIPアーカイブ名のリストを使う
'''
print('sys.pathは次のように定義されている。')
for place in sys.path:
    print(place)
'''使われるのは、最初にマッチしたファイルなので、自分でモジュールを定義し、それが標準ライブラリよりも前のサーチパスに含まれている場合標準ライブラリのrandomにはアクセスできない'''

import sys
print('Program arguments:', sys.argv)

'''
import module
他のPythonファイルのファイル名から拡張子の.pyを取り除いたもの
'''

import report #同じディレクトリに奥
'''これはreportモジュールの全体をインポートしているためdescription()のプレフィックスとしてreport.を使わなければならない。
こうすることで他のモジュールにget_description()関数があっても、間違ってそれを呼び出すことはない'''
description = report.get_description()
print("Today's weather:", description)

'''同じ名前の別のモジュールが必要な時や、もっと簡潔な名前を使いたい時は別名を使ってインポートできる '''
import report as wr
description = wr.get_description()
print("Today's weather:", description)

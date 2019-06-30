print('pprint()による綺麗な表示')

from pprint import pprint
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])
'''
*プログラムの名前をpprint.pyなどにしてしまうとインポートエラーになるので注意
'''
print('print()', quotes)
print('pprint()')
'pprintは要素の位置を揃えようとする'
pprint(quotes)
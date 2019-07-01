#tableの文法復習 tapleはイミュータブル
empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho', #要素が１個のタプルも末尾にカンマをつけて作る
print(one_marx)

marx_tuple = 'Groucho', 'Chico', 'Harpo' #複数の場合はカンマが省略可能
print(marx_tuple)

marx_tuple = ('Groucho', 'Chico', 'Harpo')#かっこはあってもなくてもいいが、囲んだほうがタプルとわかりやすい
print(marx_tuple)

a, b, c = marx_tuple#tupleを使えば一度に複数の変数に代入可能、これをタプルのアンパックということがある
print(a)
print(b)
print(c)

#タプルを使えば一時変数を使わずに一つの文で値を交換できる
password = 'password'
icecream = 'icecream'
password, icecream = icecream, password
print(password)
print(icecream)

#変換関数のtuple()を使うと他のものからタプルを作れる。
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

"""
タプルとリストの比較
タプルは消費スペースが小さい
タプルの要素は、謝って書き換える危険がない。
辞書のキーとして使える
名前付きタプルは、オブジェクトの単純な代用として使える
関数の引数は、タプルとして渡される。
"""
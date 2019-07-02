'''
継承よりもコンポジションや集約の方が理にかなっている場合がある has-a関係
車はドアやタイヤを持っているのような関係
オブジェクトにオブジェクトの属性として与えるイメージ
'''

class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.length = length

class Duck:
    def __init__(self, bill, tail):
        self. bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length)

tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
def get_description():
    '''プロと同じようにランダムな天気を返す
    私たちは関数の中におり、ほかにchoiceという名前のものはないことがわかっているので、randomモジュールから直接choice()をインポートしている
    '''
#randomモジュールからchoice関数をインポートしている
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)

'''
インポートされるコードが複数の場所で使われる場合には、関数の外でインポートするといい。
'''
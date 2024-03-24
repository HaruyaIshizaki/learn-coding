import datetime

# 基本となる関数
# 渡された関数（新たに拡張する機能）の処理の時間を計算する
def timerDecorator(fn):
    def function(arg):
        start = datetime.datetime.now()
        result = fn(arg)
        end = datetime.datetime.now()

        print('time: ' + str(end - start) + ' ms')

        return result

    return function

print(timerDecorator(lambda x: x*2)(2424))

# 新しく追加する機能として、O(n^2)の計算量を持つ関数を定義
def on2func(x):
    finalResult = 1
    for i in range(x):
        result = i
        for j in range(i):
            result += j
        finalResult += result
    return finalResult

# O(n^2)の計算量を持つ関数に対して'timerDecorator'を適用します。そしてその関数を実行します。
print(timerDecorator(on2func)(500))
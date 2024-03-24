def createHigherOrderFn(word, fn):
    def f():
        return fn() + word
    # 関数を出力する
    return f

step0Fn = lambda: "step0: "
step1Fn = createHigherOrderFn("step1: ", step0Fn)
step2Fn = createHigherOrderFn("step2: ", step1Fn)

print(step0Fn())
print(step1Fn())
print(step2Fn())

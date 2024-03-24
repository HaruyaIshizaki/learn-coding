def counterFn():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count

    # この時点では関数を実行しない。関数を返すだけ。
    return increase

# counterFn関数を呼び出し、その結果（increase関数）をcounterという変数に格納します。
counter = counterFn()

# counter変数を通じてcountやincreaseにアクセスできるため、状態が保持される（ステートフル）
print(counter())
print(counter())
print(counter())
print(counter())

# 税金控除後の金額を返すプログラム
federalTaxes = 0.2;

def taxLambda(stateTax, state):
    # 出力するラムダ関数内に共通処理を隠蔽する
    def f(income):
        taxes = federalTaxes + stateTax
        print('computing taxes in: ' + state)
        return int(income - (taxes * income))

    return f

if __name__ == '__main__':
    californiaF = taxLambda(0.0725, 'California')
    texasF = taxLambda(0.0625, 'Taxes')
    hawaiiF = taxLambda(0.04, 'Hawaii')

    income = 40000
    print("Calculating income using lambdas")
    print(californiaF(income))
    # テキサス州の税金計算
    print(texasF(income))
    # ハワイ州の税金計算
    print(hawaiiF(income))

    # このように、異なる所得や税率に対応する関数を一度定義してしまえば、税金計算を再利用して効率的に計算を行うことが可能になります。
    income2 = 500000;
    print("------Calculating more income using lambdas------")
    # カリフォルニア州の税金計算
    print(californiaF(income2))
    # テキサス州の税金計算
    print(texasF(income2))
    # ハワイ州の税金計算
    print(hawaiiF(income2))
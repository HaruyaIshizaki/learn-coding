def createObj():
    privateValue = 'private'

    def setPrivateValue(setValue):
        nonlocal privateValue
        accessAlert()
        privateValue = setValue

    def getPrivateValue():
        return privateValue

    def accessAlert():
        print('data changed')

    # hashMapでキーを通じて複数の関数を返す
    return {
        'setValue': setPrivateValue,
        'getValue': getPrivateValue
    }

if __name__ == '__main__':
    newObj = createObj()
    print(newObj['getValue']())
    newObj['setValue']('newValue')
    print(newObj['getValue']())
class Heap:
    @staticmethod
    # 子ノードのインデックスを返す
    # 親ノードが0なら左の子ノードが1, 右の子ノードが2
    # 1の子ノードの左の子ノードが3, 右の子ノードが4
    def left(i):
        return 2*i + 1

    def right(i):
        return 2*i + 2

    @staticmethod
    def maxHeapify(arr, i):
        l_index = Heap.left(i)
        r_index = Heap.right(i)

        biggest = i
        # 最大ヒープになるようノードの値を比較
        if l_index < len(arr) and arr[l_index] > arr[biggest]:
            biggest = l_index
        if r_index < len(arr) and arr[r_index] > arr[biggest]:
            biggest = r_index

        if biggest == l_index or biggest == r_index:
            tmp = arr[i]
            arr[i] = arr[biggest]
            arr[biggest] = tmp
            Heap.maxHeapify(arr, biggest)

# ヒープの例を示し、maxHeapifyメソッドを使ってそれが最大ヒープになるように調整します。
heap1 = [2,42,11,30,10,7,6,5,9]
# 根ノードが2で、2 < 42のため、最大ヒープではありません。
Heap.maxHeapify(heap1,0)
print(heap1)

heap2 = [56,4,51,10,12,5,12,4,6,5]
# インデックス1が4で、4 < 10のため、最大ヒープではありません。
Heap.maxHeapify(heap2,1)
print(heap2)

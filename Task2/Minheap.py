





def insert(heap, value):
    heap.append(value)
    index = len(heap) - 1
    print(heap)
    while index > 0 and heap[(index - 1) // 2] > heap[index]:
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        index = (index - 1) // 2

def deleteMin(heap, value):
    index = -1
    for i in range(len(heap)):
        if heap[i] == value:
            index = i
            break

    if index == -1:
        return

    heap[index] = heap[-1]
    print("Heap before delete: ",heap)
    heap.pop()

    while True:
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest = index

        if left_child < len(heap) and heap[left_child] < heap[smallest]:
            smallest = left_child
        if right_child < len(heap) and heap[right_child] < heap[smallest]:
            smallest = right_child

        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break

def top(heap):
    if heap:
        return heap[0]
    return -1



if __name__ == "__main__":
    arr = [31, 41, 51, 100]

    print("Initial heap: ", end="")
    for val in arr:
        print(val, end=" ")
    print()
    
    print("Insert ", 13, " ")
    insert(arr, 13)
    print(arr)

    print("Insert ", 16, " ")
    insert(arr, 16)
    print(arr)
    
    deleteMin(arr, 13)
    print("Heap after deleting 13: ", end="")
    print(arr)
    
    print(top(arr))
    
    
    

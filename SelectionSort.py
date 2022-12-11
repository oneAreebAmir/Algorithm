
def SelectionSort(arr):
    lenght = len(arr)
    for i in range(0,lenght-1):
        min = i
        for j in range(i+1,lenght):
            if arr[j] < arr[min]:
                temp = min
                min = j
                j = temp
        if min != i:
            perm = arr[i]
            arr[i] = arr[min]
            arr[min] = perm

    return arr

array = [1,5,2,1,8,3,6,7]
print(SelectionSort(array))
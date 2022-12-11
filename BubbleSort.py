def swap():
    pass

def BubbleSort(arr):
    n = len(arr)
    
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr            

array = [2,1,3,2,3,5,6,5]
print(BubbleSort(array))
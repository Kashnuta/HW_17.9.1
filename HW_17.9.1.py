
def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return(array)

def find(array, num, left, right):
    if left > right:
        return -1
    middle = (right + left) // 2
    if array[middle] == num:
        return middle
    elif num < array[middle]:
        return find(array, num, left, middle - 1)
    else:
        return find(array, num, middle + 1, right)

array = list(map(int, input().split()))
num = int(input())
sort(array)
print(array)
left = 0
right = len(array)
index = find(array, num, left, right)
if index == -1:
    print("Число не в списке")
elif index == (len(array)-1):
    print(index-1, index)
elif index == 0:
    print(index, index+1)
else:
    print(index-1, index+1)
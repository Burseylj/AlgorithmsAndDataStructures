import random
def mergeSort(array):
    size = len(array)
    if size < 2:
        return array
    elif size == 2:
        if array[1] < array[0]:
            return array[::-1]
        else :
            return array
    else:
        arr1 = array[:size/2]
        arr2 = array[size/2:]
        return merge(mergeSort(arr1), mergeSort(arr2))

def merge(arr1,arr2):
    newArr = []
    while (arr1 != [] and arr2 != []):
        head1, head2 = arr1[0], arr2[0]
        if head1 <= head2:
            newArr.append(head1)
            arr1 = arr1[1:]
        else:
            newArr.append(head2)
            arr2 = arr2[1:]
        
    return newArr + arr1 + arr2

def quickSort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    lessArr, moreArr = [],[]
    for x in array[1:]:
        if x <= pivot:
            lessArr.append(x)
        else:
            moreArr.append(x)

    return quickSort(lessArr) + [pivot] + quickSort(moreArr)


def main():
    for i in xrange(100):
        print quickSort(random.sample(range(0,100),10))
main()

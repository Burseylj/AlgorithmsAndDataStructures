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




def main():
    print merge([1,3,5], [0,2,10])
    print merge([1,3,5], [0,2,10,11])

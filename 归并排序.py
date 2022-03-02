'''
归并排序原理：
'''


from typing import List

def merge(arr1:List[int], arr2:List[int]):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result += arr1
    if arr2:
        result += arr2
    return result

def merge_sort(arr:List[int]):
    """
    归并排序
    :param arr: 待排序的List
    :return: 排好序的List
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge(left, right)



def merge1(arr1:list[int], arr2:list[int]):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result += arr1

    if arr2:
        result += arr2

    return result



def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge(left, right)


if __name__ == "__main__":
    print(merge_sort([17, 56, 71, 38, 61, 62, 48, 28, 57, 42]))
import datetime
import random
import time


'''
选择排序：从第一位开始与剩下的数比较，如果剩下的数中有比它更小的，交换位置，再从第二位开始，继续与剩下的数比较，有更小的就交换位置，直互遍历到最后一对
时间复杂度：O(n^2)
空间复杂度：O（1）
稳定性： 不稳定
排序法比较：插入排序 > 选择排序 > 冒泡排序
'''

def run_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        cost = end - start
        print(f"{func.__name__}消耗时长{cost}s")
    return wrapper


@run_time
def selection_sort(arr):
    for i in range(len(arr)):
        #假设一个最小值
        minimum = i

        for j in range(i + 1, len(arr)):
            # 选择最小的值
            if arr[j] < arr[minimum]:
                minimum = j

        # 把最小值和当前值进行交换，也就是把未排序中最小值放到最前面
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr


# @run_time
# def selection_sort(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[i]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr

if __name__ == "__main__":
    list = list()
    for i in range(20000):
        list.append(random.randint(1,1000))
    print(selection_sort(arr=list))             #此长消耗时长 14s

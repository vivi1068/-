import time

from faker.generator import random

source = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]

# for index in range(1 ,len(source)):
#     current_val = source[index]  # 先记下来每次大循环走到的第几个元素的值
#     position = index
#
#     while position > 0 and source[position -1] > current_val:  # 当前元素的左边的紧靠的元素比它大,要把左边的元素一个一个的往右移一位,给当前这个值插入到左边挪一个位置出来
#         source[position] = source[position -1]  # 把左边的一个元素往右移一位
#         position -= 1  # 只一次左移只能把当前元素移动一个位置 ,还得继续左移只到此元素放到排序好的列表的适当位置 为止
#
#     source[position] = current_val  # 已经找到了左边排序好的列表里不小于current_val的元素的位置,把current_val放在这里
#     print(source)


'''
插入排序：玩扑克牌时经常使用插入排序，它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
时间复杂度: O(n^2)
空间复杂度：O（1）
稳定性： 稳定
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

# @run_time
def insertion_sort(arr):
    for i in range(1, len(arr)):
        target = arr[i]        #先记下来每次大循环走到第几个元素的值，称之为目标值
        position = i

        while position > 0 and arr[position - 1] > target:    #如果当前位置大于0，且左边一位数大于目标数
            arr[position] = arr[position - 1]          #就将目标数位置左移一位
            position -= 1                              #索引即跟着自减1，如果目标数符合位置大于0且仍小于左边数，继续循环

        arr[position] = target        #当 position = 0时不符合以上约束条件，跳出循环，说明当前没有比该值更小的了，放在第一位

if __name__ == "__main__":
    insertion_sort(arr=[92, 77, 67, 8, 6, 84, 55, 85, 43, 67])
    # list = list()
    # for i in range(20000):
    #     list.append(random.randint(1, 1000))
    # print(insertion_sort(list))
#   #消耗时长 17s

﻿'''
快速排序： 原理--分而治之
         步骤：
         1、从数组中选择一个元素 P
         2、将所有小于 p 的元素移到P 的左边，所有大于 P 的元素移到P 的右边
         3、被分配到左边或右边的元素，重复以上动作
'''

def partition(start, end, array):
    # why: 这里为什么要 pivot_index = start         而不是直接  pivot_index = 0 ?
    # ans: 因为 partition 函数不知道外部传入进来的start是什么, 所以不能直接写 0 .
    #
    # why: 这里为什么要 pivot = array[pivot_index] 而不是直接  pivot = array[start] ?
    # ans: 因为 start 是一个游标, 它的值会发生变化, 所以在它发生变化之前, 使用 pivot_index 来记录它初始的状态.
    pivot_index = start
    pivot = array[pivot_index]

    # 这个循环试图找出start和end游标交叉的点,
    # 当交叉点出现时意味着: start游标位置的值一定大于 pivot值
    #                   end游标位置的值一定小于 pivot值
    while start < end:

        # 游标start所在位置的值 <= pivot 时, 游标start递增1.
        # 目的: 试图将start右侧邻近的, 并且 <= pivot 的值, 通过游标start递增1的方式记录下来.
        #
        # 代码含义1: start < len(array) 是为了防止后面的 array[start] 取值超出边界.
        # 代码含义2: array[start] <= pivot 表示他们两是一个有效的序列，不需要做任何事，start游标继续右移
        # 代码含义3：array[start] > pivot 表示他们两不是一个有效序列，start游标停止移动,此时跳出当前循环
        while start < len(array) and array[start] <= pivot:
            start += 1

        # 游标end所在位置的值 > pivot 时, 游标end递减1.
        # 目的: 试图将end左侧邻近的, 并且 > pivot 的值, 通过游标end递减1的方式记录下来.
        while array[end] > pivot:
            end -= 1

        # 此时
        # 1. 游标start所在的位置的值 > pivot
        # 2. 游标end所在的位置的值 < pivot
        # 动作: 将start和end位置的值进行互换.
        # 目的: 试图将小于pivot的值归放置在pivot右侧邻近位置, 以便下次循环时可以继续移动start游标和end游标.
        #
        # 代码含义1：start < end 表示当两个游标还没有产生交集时，才可以做位置交换动作
        if start < end:
            array[start], array[end] = array[end], array[start]

    # 将 end游标所在位置的值 与 pivot_index所在位置的值 交换位置.
    # 目的: 交换位置后, end位置左侧的所有元素都小于 pivot, end位置右侧的所有元素都大于 pivot.
    # 重点: pivot所在的位置就是一个排好序的位置, 每次循环其实有效的排序就是pivot.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # 返回 end 游标, 此时 end 就是一个很分割点, 所以这个函数叫做 partition.
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if start >= end:
        return None

    p = partition(start, end, array)

    quick_sort(start, p - 1, array)
    quick_sort(p + 1, end, array)


if __name__ == '__main__':
    # collection = random.sample(range(0, 20), 10)
    collection = [4, 16, 8, 9, 10, 1, 2]
    sorted_collection = sorted([9, 10, 1, 2])
    quick_sort(3, len(collection) - 1, collection)
    assert collection == sorted_collection



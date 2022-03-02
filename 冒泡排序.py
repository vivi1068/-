# coding: utf -8
import random
import time

'''
冒泡排序：冒泡排序步骤遍历列表并比较相邻的元素对。如果元素顺序不对就交换它们。重复遍历列表未排序部分的元素，直到完成列表排序。
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

@run_time
def bubble_sort(our_list):
    # 这个循环是为了让相邻两个数两两相比较后再从头开始比较
    for i in range(len(our_list)):
        # 最后一对比较：j 与j+1的索引分别为n-2,n-1
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap（交换）
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
    return our_list


if __name__ == "__main__":
    list = list()
    for i in range(20000):
        list.append(random.randint(1, 1000))
    print(bubble_sort(list))       #此条消耗时长 51S



# 非递归版本
def quick_sort1(nums):
    def partition(list1,l,r):
        flag = list1[l]  # 先记录flag
        while l<r: # 每次交换一个 原本右小左大的变成右大左小
            while l<r and list1[r]>=flag:
                r-=1
            list1[l] = list1[r]  # 原本右侧小数调整到左侧
            while l<r and list1[l]<=flag:
                l+=1
            list1[r] = list1[l]  # 原本左侧大数调整到右侧
        list1[l] = flag  # 还原记录的flag
        return l

    if len(nums)<2:
        return nums
    stack = []
    stack.append([0, len(nums)-1])
    while stack:
        [left, right] = stack.pop()
        index = partition(nums, left, right)
        if left < index-1:
            stack.append([left, index-1])
        if right > index+1:
            stack.append([index+1, right])
    return nums

# 递归版本
def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    flag = arr[0]
    left = [x for x in arr if x < flag]
    middle = [x for x in arr if x == flag]
    right = [x for x in arr if x > flag]
    return quick_sort2(left) + middle + quick_sort2(right)

if __name__ == "__main__":
    nums = [21,3,4,15,4,3,123,436,12]
    print(quick_sort2(nums))
    print(quick_sort1(nums))

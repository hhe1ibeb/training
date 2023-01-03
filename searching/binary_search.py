def binary_search(arr, low, high, x):
    mid = (low + high) // 2
    if high >= low:
        if arr[mid] == x:
            return mid+1
        else:
            if arr[mid] > x:
                return binary_search(arr, low, mid-1, x)
            else:
                return binary_search(arr, mid+1, high, x)
    return 0


n, k = map(int, input().split())
nums = list(map(int, input().split()))
tar = list(map(int, input().split()))
for i in range(k):
    result = binary_search(nums, 0, len(nums)-1, tar[i])
    print(result)

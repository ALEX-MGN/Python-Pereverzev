def find_insert_position(arr, x):
    if(len(arr) == 0):
        return 0
    else:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        return left

print(find_insert_position([1, 2, 3, 5, 7, 9],10))
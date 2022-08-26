class Sorting:
    def merge(self, left_arr, right_arr):
        left_index = 0
        right_index = 0
        temp = []
        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] <= right_arr[right_index]:
                temp.append(left_arr[left_index])
                left_index += 1
            else:
                temp.append(right_arr[right_index])
                right_index += 1
        while left_index < len(left_arr):
            temp.append(left_arr[left_index])
            left_index += 1
        while right_index < len(right_arr):
            temp.append(right_arr[right_index])
            right_index += 1
        return temp

    def mergesort(self, arr, start, end):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:end]
        left_sorted = self.mergesort(left_arr, start, mid)
        right_sorted = self.mergesort(right_arr, mid, end)
        return self.merge(left_sorted, right_sorted)

    def countingsort(self, arr):
        max_element = max(arr)
        min_element = min(arr)
        n = len(arr)
        output_arr = [0 for _ in range(n)]
        range_of_arr = max_element - min_element + 1  # added one as 0 also included ...
        count_arr = [0 for _ in range(range_of_arr)]

        for i in range(n):
            count_arr[arr[i] - min_element] += 1
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]

        for i in range(n - 1, -1, -1):
            x = arr[i] - min_element
            print(x)
            output_arr[count_arr[x] - 1] = arr[i]
            count_arr[x] -= 1

        for i in range(n):
            arr[i] = output_arr[i]
        return arr

    def cSort(self, arr, exp):
        n = len(arr)
        output_arr = [0] * n
        count_arr = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            position = index % 10
            # print(index, position, exp)
            count_arr[position] += 1
        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output_arr[count_arr[index % 10] - 1] = arr[i]
            count_arr[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output_arr[i]

    def radixSort(self, arr):
        max1 = max(arr)
        exp = 1
        while max1 / exp > 1:
            self.cSort(arr, exp)
            exp *= 10
        return arr


import random

list_obj = [random.randrange(-10, 10) for i in range(8)]
n = len(list_obj)
# print("Given array: ", list_obj)

sort = Sorting()
x = sort.radixSort([802, 200, 100, 900])
print(x)

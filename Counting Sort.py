
def counting_sort(arr):

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

   
    count = [0] * range_of_elements

    for num in arr:
        count[num - min_val] += 1

    
    sorted_arr = []
    for i in range(range_of_elements):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr



arr = [4, 2, 2, 8, 3, 3, 1]
print("Unsorted array:", arr)

sorted_arr = counting_sort(arr)

print("Sorted array:", sorted_arr)

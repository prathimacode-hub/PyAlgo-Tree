# To heapify
def heapify(array, num, x):
    # Find the largest among root, left child and right child
    max = x
    left = 2 * x + 1
    right = 2 * x + 2

    if left < num and array[x] < array[left]:
        max = left

    if right < num and array[max] < array[right]:
        max = right

    # If root is not largest, swap and continue heapifying
    if max != x:
        array[x], array[max] = array[max], array[x]
        heapify(array, num, max)


# To insert an element
def insert(nums, next):
    s = len(nums)
    if s == 0:
        nums.append(next)
    else:
        nums.append(next)
        for i in range((s // 2) - 1, -1, -1):
            heapify(nums, s, i)


# To delete an element
def delete(nums, n):
    s = len(nums)
    i = 0
    for i in range(0, s):
        if n == nums[i]:
            break

    nums[i], nums[s - 1] = nums[s - 1], nums[i]

    nums.remove(s - 1)

    for i in range((len(nums) // 2) - 1, -1, -1):
        heapify(nums, len(nums), i)


array = []

insert(array, 1)
insert(array, 4)
insert(array, 2)
insert(array, 7)
insert(array, 8)
insert(array, 5)
insert(array, 6)

print("Max-Heap array: " + str(array))

delete(array, 6)
print("After deletion: " + str(array))

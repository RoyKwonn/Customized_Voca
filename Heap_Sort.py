# arr이라는 리스트, 전체 개수, 자식노드 중 큰거
# To heapify subtree rooted at index i.
# n is size of heap
def heapify(data, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and data[i][2] > data[l][2]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and data[largest][2] > data[r][2]:
        largest = r

        # Change root, if needed
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # swap

        # Heapify the root.
        heapify(data, n, largest)


def heapSort(data):
    n = len(data)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    # n부터 -1_2_까지 -1_3_만큼 숫자간격을 좁혀서
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]  # swap
        heapify(data, i, 0)

    return data

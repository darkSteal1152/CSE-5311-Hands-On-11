class DynamicArray:
    def __init__(self):
        self._capacity = 2
        self._size = 0
        self._array = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return [None] * capacity

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = value
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Pop from empty array")
        value = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return value

    def get(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    def set(self, index, value):
        if not 0 <= index < self._size:
            raise IndexError("Index out of bounds")
        self._array[index] = value

    def __len__(self):
        return self._size

    def capacity(self):
        return self._capacity

    def __str__(self):
        return "[" + ", ".join(str(self._array[i]) for i in range(self._size)) + "]"


arr = DynamicArray()
arr.append(10)
print(arr)
print("Capacity:", arr.capacity())
print("Size:", len(arr))
arr.append(15)
print(arr)
print("Capacity:", arr.capacity())
print("Size:", len(arr))
arr.append(12)
print(arr)
print("Capacity:", arr.capacity())
print("Size:", len(arr))
arr.append(3)
print(arr)
print("Capacity:", arr.capacity())
print("Size:", len(arr))
arr.append(4)
print(arr)
print("Capacity:", arr.capacity())
print("Size:", len(arr))
arr.append(13)
print(arr)
print("Capacity:", arr.capacity())
print("Size:", len(arr))
arr.append(1)
print(arr)
print("Capacity:", arr.capacity())
print("Size:", len(arr))

arr.pop()
print(arr)

print("Element at index 1:", arr.get(1))
print("Capacity:", arr.capacity())
print("Size:", len(arr))

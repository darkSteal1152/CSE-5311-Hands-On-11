import matplotlib.pyplot as plt

class DynamicArray:
    def __init__(self):
        self._capacity = 1           # Initial capacity
        self._size = 0               # Current number of elements
        self._array = [None] * self._capacity
        self._total_cost = 0         # Total cost of all operations
        self._operations = 0         # Number of insertions (for amortized analysis)
        self._costs = []             # List to store the cost of each insertion
        self._amortized_costs = []   # List to store amortized cost after each insertion

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def insert(self, value):
        cost = 1

        if self._size == self._capacity:
            new_capacity = 2 * self._capacity
            resize_cost = self._size
            cost += resize_cost
            self._resize(new_capacity)

        self._array[self._size] = value
        self._size += 1

        self._total_cost += cost
        self._operations += 1

        self._costs.append(cost)
        self._amortized_costs.append(self._total_cost / self._operations)

    def average_cost(self):
        return self._total_cost / self._operations if self._operations > 0 else 0


n = 100
array = DynamicArray()

for i in range(1, n + 1):
    array.insert(i)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(range(1, n + 1), array._costs, marker='o', linestyle='-', color='b', label="Individual Insertion Cost")
plt.xlabel("Insertion Operation")
plt.ylabel("Cost")
plt.title("Individual Insertion Cost")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(range(1, n + 1), array._amortized_costs, marker='o', linestyle='-', color='r', label="Amortized Cost")
plt.xlabel("Insertion Operation")
plt.ylabel("Amortized Cost")
plt.title("Amortized Cost per Insertion")
plt.legend()

plt.tight_layout()
plt.show()

import os


class UnsortedArray:
    def __init__(self, arr: [list] = []) -> None:
        self.arr: [list] = arr
        self.length = len(arr)

    def insert(self, value):
        self.arr.append(value)
        self.length = self.length + 1

    def search(self, value: int) -> int:
        for i in range(self.length):
            if self.arr[i] == value:
                return i
        return -1

    @staticmethod
    def display():
        ar = UnsortedArray([i for i in range(1, 10)])
        ar.insert(21)
        print('Inserted list is: ', end=" ")
        for i in range(ar.length):
            print(ar.arr[i], end=' ')
        print()
        index = ar.search(3)
        if index != -1:
            print('Index number is: {}'.format(index))
        else:
            print('Value not found')
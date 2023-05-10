import os


class RotationArray:
    def __init__(self, arr: [list] = []) -> None:
        self.arr: [list] = arr
        self.length = len(arr)

    def leftRotate(self, d: int) -> None:
        if self.length:
            for i in range(d):
                last: int = self.arr.pop(0)
                self.arr.append(last)
            self.display('left')

    def rightRotate(self, d: int) -> None:
        if self.length:
            for i in range(d):
                first: int = self.arr.pop()
                self.arr.insert(0, first)
            self.display('right')

    def display(self, action: str = ''):
        print("The {} rotated list is: ".format(action), end=" ")
        for i in range(self.length):
            print(self.arr[i], end=" ")
        print()

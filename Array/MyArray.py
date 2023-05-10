from Array.RotationArray import RotationArray
from Array.UnsortedArray import UnsortedArray


class MyArray:

    @staticmethod
    def do() -> None:
        MyArray.leftRotation()
        MyArray.rightRotation()

        UnsortedArray.display()

    @staticmethod
    def leftRotation() -> None:
        arr: [list] = [i for i in range(1, 11)]
        ra = RotationArray(arr)
        ra.leftRotate(3)

    @staticmethod
    def rightRotation() -> None:
        arr: [list] = [i for i in range(1, 11)]
        ra = RotationArray(arr)
        ra.rightRotate(5)

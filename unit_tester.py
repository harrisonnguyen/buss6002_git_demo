from __future__ import print_function
from square import square
from cube import cube
from sum import sum

def main():
    if square(50) != 50**2:
        print("Square function does not work")

    if cube(50) != 50**3:
        print("Cube function does not work")

    numbers = [1,2,3,4,5]
    if sum(numbers) != 15:
        print("Sum function does not work")

if __name__ == "__main__":
    main()
from __future__ import print_function
from square import square
from cube import cube
from sum import sum
import argparse

def main(args):
    a = 1
    b = 6
    c = 9
    x = args.x
    print("Lets compute the polynomial of %d*x^3 + %d*x^2 + %d*x" %(a,b,c))
    result = sum([a*cube(x), b*square(x), c*x])
    print("The result is %d" %result)
    true_result = a*x**3 + b*x**2 + c*x
    if true_result == result:
        print("Success class complete!")
    else:
        print("Woops. Try again")
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--x', dest='x', type=int,
                    help='a value of x for the polynomial')
    args = parser.parse_args()
    main(args)
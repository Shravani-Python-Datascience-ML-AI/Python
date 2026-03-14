
"""
  ..............parallel Programming.........

   in this application only single process gets executed on one core of our cpu
   to use power of multicore processor we use pooling in python

"""

import os
import multiprocessing

def Square(No):
    return (No*No)

def main():
    Data = [1,2,3,4,5]
    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Square, Data)

    print("Result afer square operatiuon is ",Result)

if __name__ == "__main__":
    main()








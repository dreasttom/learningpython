#!/usr/bin/python
## The purpose of this code is just to demonstrate multi-threading
## it simply prints out square and cube of a series of numbers


import time
import threading


def Print_Square(numbers):
  try:
    print("Print squares")
    for n in numbers:
      time.sleep(0.2)
      print("Square", n*n)

  except:
    print ("Error in Print_Square")


def Print_Cube(numbers):
  try:
    print("Print cubes")
    for n in numbers:
      time.sleep(0.2)
      print("Cube", n*n*n)
  except:
    print ("Error in Print_Cube")

def Main():
	arr = [2,3,4,5]
	t = time.time()
	Print_Square(arr)
	Print_Cube(arr)
	thread1=threading.Thread(Target=Print_Square, args=(arr,))
	thread2=threading.Thread(Target=Print_Cube, args=(arr,))
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()
	print("Program took", time.time()-t)


if __name__ == '__main__':
	Main()



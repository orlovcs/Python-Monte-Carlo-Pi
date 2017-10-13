
import random


def monte():
  square_size = int(input("What should the size of the square be?: "))
  r = square_size / 2
  left_bottom = [0,0]
  left_top = [0,square_size]
  right_bottom = [square_size,0]
  right_top = [square_size,square_size]
 
 
  print(left_top[0],left_top[1],
  "------",right_top[0],right_top[1])
  
  
  for i in range(0,5):
    print("|            |")

  print(left_bottom[0],left_bottom[1],
  "------",right_bottom[0],right_bottom[1])
  
  print("r is equal to ",r)
  print("The area of the square is ", 4*(r**2))
  iterations = int(input("Enter the amount of iterations: "))
  in_circle = 0
  for i in range(1,iterations):
    x = random.randrange(0,r)
    y = random.randrange(0,r)
    if ((x**2)+(y**2))<(r**2):
      in_circle = in_circle + 1
  pi = ((4 * in_circle) / iterations)
  print("Pi is: ", pi)
    

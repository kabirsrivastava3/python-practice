#fibonacci using recursion

def fibonacciSeries(limit):
  if limit == 1:
    return 0
  elif limit == 2:
    return 1
  
  value = fibonacciSeries(limit-1)+fibonacciSeries(limit-2)
 
  return value

print("Enter the last term required: ")
limit = int(input())
for index in range(1,limit+1):
    print(fibonacciSeries(index),end = ', ')
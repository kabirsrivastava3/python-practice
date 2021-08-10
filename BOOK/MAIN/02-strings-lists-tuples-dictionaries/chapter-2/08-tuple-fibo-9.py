#print the first 9 terms of Fibonacci series
#Time Complexity = O(N)

fiboSeries= (0,1,1)

for index in range(6):
    fiboSeries = fiboSeries + (fiboSeries[index+1] + fiboSeries[index+2],)

print("9 terms of Fibonacci series are: ",fiboSeries)
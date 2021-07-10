#print the first 9 terms of Fibonacci series
#Time Complexity = O(N)

fiboSeries= (0,1,1)

for i in range(6):
    fiboSeries = fiboSeries + (fiboSeries[i+1] + fiboSeries[i+2],)

print("9 terms of Fibonacci series are: ",fiboSeries)
# Bubble Sort-keys of a dictionary as a list
#Time Complexity = O(N*N)

def bubbleSort(k):
    for i in range(1,len(k)):
        for j in range(len(k)-i):
            if k[j] > k[j+1]:
                k[j],k[j+1] = k[j+1],k[j]
    return k

dictNumber = {"a":1, "c":3, "f":6, "e":5, "d":4, "b":2}
k = list(dict.keys())
print(bubbleSort(k))


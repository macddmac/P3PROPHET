#print ("input 3 integers you want to see in order")

#a = int(input())
#b = int(input())
#c = int(input())
#arr = [a, b, c]

def RohanBubbleSort1(arr):
    n = len(arr)


    for i in range(n):


        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#RohanBubbleSort1(arr)

#print ("The array in numerical order is:")
#for i in range(len(arr)):
#print ("%d" %arr[i])

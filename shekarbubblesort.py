class Bubblesort:
    def __init__(self, arr):
        arr1 = arr.split()
        arr2=[]
        for x in arr1:
            arr2.append(int(x))
        self._oarr = arr2
        self._sarr = arr2.copy()
        self.bubbleSort()

    def bubbleSort(self):
        n = len(self._sarr)
        for i in range(n-1):
            for f in range(0, n-i-1):
                if self._sarr[f] > self._sarr[f+1] :
                    self._sarr[f], self._sarr[f+1] = self._sarr[f+1], self._sarr[f]

    @property
    def sarr(self):
        return self._sarr

    @property
    def oarr(self):
        return self._oarr

if __name__ == "__main__":
    #arrinput=input("enter a list of numbers \n")
    arrinput = "3 5 8 2"
    bs = Bubblesort(arrinput)
    print("Unsorted array is:", bs.oarr )
    print("Sorted array is:", bs.sarr)

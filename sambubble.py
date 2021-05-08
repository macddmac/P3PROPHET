class Numbersort:
    def __init__(self, arr):
        arr1 = arr.split()
        arr2=[]
        for x in arr1:
            arr2.append(int(x))
        self.colin = arr2.copy()
        self.order()

    def order(self):
        n = len(self.colin)
        for i in range(n-1):
            for f in range(0, n-i-1):
                if self.colin[f] > self.colin[f+1] :
                    self.colin[f], self.colin[f+1] = self.colin[f+1], self.colin[f]

    @property
    def szeto(self):
        return self.colin

if __name__ == "__main__":
    #arrinput=input("enter a list of numbers \n")
    arrinput = "3 5 8 2"
    bs = Numbersort(arrinput)
    print("Sorted array is:", bs.szeto)
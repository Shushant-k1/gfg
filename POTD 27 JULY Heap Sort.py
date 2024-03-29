class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        large, l, r = i, 2*i+1, 2*i+2
        if l<n and arr[large]<arr[l]:large=l
        if r<n and arr[large]<arr[r]:large=r
        
        if large!=i:
            arr[large], arr[i] = arr[i], arr[large]
            self.heapify(arr, n, large)
    
    #Function to build a Heap from array.
    def buildHeap(self, arr, n):
        for i in range(n, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)

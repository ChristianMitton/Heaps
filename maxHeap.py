# This is the correct formula for parent, left child and right child:
# 
#   parent = (k - 1) // 2
#   leftChild = (k * 2) + 1
#   rightChild = (k * 2) + 2
#
# Various incorrect versions pop up from a quick google search

class MaxHeap:
    def __init__(self, array):
        self.heap = []
        self.inputArray = array
        self.buildHeap()

    def buildHeap(self):
        for num in self.inputArray:            
            self.heap.append(num)                        
            self.siftUp()                                       

    def remove(self):                
        heap = self.heap    

        self.swap(0, -1)        
        val = heap.pop(-1)

        self.siftDown()                        
        return val

    def siftUp(self):
        heap = self.heap
        k = len(heap)-1        
        parentIdx = (k-1)//2        
        while parentIdx >= 0:
            if heap[parentIdx] < heap[k]:
                self.swap(parentIdx, k)
                k = parentIdx
                parentIdx = (k-1)//2
            else:
                break

    def siftDown(self):
        heap = self.heap
        k = 0
        leftChildIdx = (k * 2) + 1
        while leftChildIdx < len(heap):            
            rightChildIdx = leftChildIdx + 1
            # if there is no right child
            if rightChildIdx >= len(heap):                
                biggestChildIdx = leftChildIdx                
            # otherwise, get the smallest child
            else:                  
                biggestChildIdx = leftChildIdx if heap[leftChildIdx] >= heap[rightChildIdx] else rightChildIdx                                
                        
            if heap[k] < heap[biggestChildIdx]:                
                self.swap(k, biggestChildIdx)
                k = biggestChildIdx
                leftChildIdx = (k * 2) + 1
            else:
                break            
                    
    def swap(self, a, b):
        heap = self.heap
        heap[a], heap[b] = heap[b], heap[a]        

array = [1,4,6,8,3,7,9,9,2,-1]

maxHeap = MaxHeap(array)
print(f'Heap: {maxHeap.heap}')

r = maxHeap.remove()
print(f'Biggest Number: {r}')
# print(maxHeap.heap)

r = maxHeap.remove()
print(f'Biggest Number: {r}')
# print(maxHeap.heap)

r = maxHeap.remove()
print(f'Biggest Number: {r}')
# print(maxHeap.heap)

r = maxHeap.remove()
print(f'Biggest Number: {r}')
# print(maxHeap.heap)

r = maxHeap.remove()
print(f'Biggest Number: {r}')
# print(maxHeap.heap)

r = maxHeap.remove()
print(f'Biggest Number: {r}')
# print(maxHeap.heap)

r = maxHeap.remove()
print(f'Biggest Number: {r}')
# print(maxHeap.heap)
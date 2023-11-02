from Flight import Flight

class Heap:

    def __init__(self) :
        self.heap = list()

    class Entry:
        key: int
        value: Flight


        def __init__(self, key, value):
            self.key = key
            self.value = value

    def parent(self, j): return int((j-1)/2)
    def left(self, j): return 2*j+1
    def right(self, j): return 2*j+2
    def hasLeft(self, j): return self.left(j) < len(self.heap)
    def hasRight(self, j): return self.right(j) < len(self.heap)



    def swap(self , i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def upHeap(self, j):

        while j > 0:
            p = self.parent(j)

            if self.heap[j].key >= self.heap[p].key : break
            self.swap(j, p)
            j = p

    def downHeap(self, j):

        while self.hasLeft(j) :
            left_index = self.left(j)
            small_child_index = left_index

            if self.hasRight(j) :
                right_index = self.right(j)
                if self.heap[left_index].key > self.heap[right_index].key:
                    small_child_index = right_index

            if self.heap[small_child_index].key >= self.heap[j].key: break
            self.swap(j, small_child_index)
            j = small_child_index


    def remove_min(self):

        if len(self.heap) == 0:
            return None
        answer = self.heap[0]

        self.swap(0, len(self.heap)-1)
        self.heap.pop()
        self.downHeap(0)

        return answer


    def inster(self , key, value: Flight):
        newest = self.Entry(key, value)
        self.heap.append(newest)
        self.upHeap(len(self.heap)-1)

        return newest











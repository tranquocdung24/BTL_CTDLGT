class List:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.data = [None] * self.capacity

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.data[idx]

    def autoResize(self):
        if(self.size == self.capacity):
            self.capacity *= 2
            moi = [None] * self.capacity
            for i in range(self.size):
                moi[i] = self.data[i]
            self.data = moi

    def push_back(self, new_data):
        self.autoResize()
        self.data[self.size] = new_data
        self.size += 1

    def remove(self, idx):
        if not 0 <= idx < self.size:
            return
        for i in range(idx, self.size-1):
            self.data[i] = self.data[i+1]
        self.data[self.size-1] = None
        self.size -= 1

    def partition(self, l, r, cmp):
        pivot = self.data[r]
        i = l - 1

        for j in range(l, r):
            if cmp(self.data[j], pivot):
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
        self.data[i + 1], self.data[r] = self.data[r], self.data[i + 1]
        return i + 1

    def QuickSort1(self, l, r, cmp):
        if(l <= r):
            pos = self.partition(l, r, cmp)
            self.QuickSort1(l,pos-1,cmp)
            self.QuickSort1(pos + 1, r, cmp)

    def QuickSort(self, cmp):
        if (self.size > 1):
            self.QuickSort1(0, self.size-1, cmp)






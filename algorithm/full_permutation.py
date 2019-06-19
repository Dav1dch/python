class arr:
    def __init__(self, low, high):
        self.permutate_arr = [i for i in range(low, high + 1)]
        self.bool_arr = [False] * (high + 1 - low)
        self.size = high + 1 - low
        self.vector = []


    def sort(self, level):
        for i in range(0, self.size):
            if (self.bool_arr[i] == False):
                self.bool_arr[i] = True
                self.vector.append(self.permutate_arr[i])
                if (level != self.size - 1):
                    self.sort(level + 1)
                else:
                    print(self.vector)
                self.bool_arr[i] = False
                self.vector.pop()


if __name__ == "__main__":
    # low = (int)(input("please input low\n"))
    # high = (int)(input("please input high\n"))
    sort_arr = arr(1, 11)
    sort_arr.sort(0)
    pass

class SetsService:
    def __init__(self, data_array):
        self.__data__ = data_array
        self.__amount__ = []
        self.__number__ = []
        self.sets = []
        self.total_sets = 1
        self.sets_data = {}
        self.set_data = []

    def __total_sets__(self):
        try:
            [self.__amount__.append(self.__data__[x][0]) for x in range(len(self.__data__))]
            for x in range(len(self.__amount__)):
                self.total_sets = self.total_sets * (self.__data__[x][1] ** self.__data__[x][0])
            for i in range(self.total_sets):
                set_data = []
                temp = i
                for j in range(len(self.__data__)):
                    number = self.__data__[j][1]
                    amount = self.__data__[j][0]
                    set_data_completed = []
                    for _ in range(amount):
                        set_data_completed.append((temp % number) + 1)
                        temp = temp // number
                    set_data.extend(set_data_completed)
                self.sets.append(set_data)
            return self.sets
        except IndexError:
            print("unu")

    def __data_sets__(self):
        try:
            sets = self.__total_sets__()
            [self.__number__.append(self.__data__[x][1]) for x in range(len(self.__data__))]
            for i in list(range(1, self.__number__.__getitem__(0) + 1)):
                for j in range(len(sets)):
                    if sets[j][0] == i:
                        self.set_data.append(sets[j])
                        set_data_copy = self.set_data.copy()
                        self.sets_data[i] = set_data_copy
                    if j == len(sets) - 1:
                        self.set_data.clear()
            return self.sets_data
        except IndexError:
            print("unu")

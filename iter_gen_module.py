class FlatIterator:
    def __init__(self, list_of_list):
        self.lst = list_of_list
        self.cursor = -1
        self.list_len = len(self.lst)

    def __iter__(self):
        self.cursor += 1
        self.list_cursor = 0
        return self

    def __next__(self):
        if self.list_cursor == len(self.lst[self.cursor]):
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.list_cursor += 1
        return self.lst[self.cursor][self.list_cursor - 1]

def flat_generator(list_of_lists):
    for list in list_of_lists:
        for item in list:
            yield item



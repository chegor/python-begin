class Buffer:
    def __init__(self):
        self.tmpList = []

    def add(self, *a):
        for item in a:
            self.tmpList.append(item)
            if (len(self.tmpList)) == 5:
                print (sum(self.tmpList))
                del self.tmpList[:5]

    def get_current_part(self):
        return self.tmpList
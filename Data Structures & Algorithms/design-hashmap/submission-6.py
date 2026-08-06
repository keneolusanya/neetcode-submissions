class MyHashMap:

    def __init__(self):
        self.m = [None] * 10000000

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

    def get(self, key: int) -> int:
        if self.m[key] != None:
            return self.m[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.m[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# set of numbers
# array for indexes for library
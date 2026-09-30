class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # alice -> [(one, 10), (two, 20), (three, 30)] 25
        # find the place where to insert the timestamp. return value to left if present else ""
        if not self.store[key]:
            return ""

        values = self.store[key]
        res = ""

        l, r = 0, len(values) - 1 # 0, 2
        while l <= r:
            mid = l + (r - l) // 2 # 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif timestamp > values[mid][1]:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


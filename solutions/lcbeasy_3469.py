def maxHeightOfTriangle(red: int, blue: int) -> int:
    def h(first, second):
        cnt = [first, second]
        r = 1
        while True:
            if cnt[(r - 1) % 2] < r:
                return r - 1
            cnt[(r - 1) % 2] -= r
            r += 1
    return max(h(red, blue), h(blue, red))

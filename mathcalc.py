class Math:
    def __init__(self, multiplier):
        self._series = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self._times = []
        for n in self._series:
            self._times.append(n * multiplier)

    @property
    def times(self):
        return self._times

    @property
    def series(self):
        return self._series


if __name__ == "__main__":
    G = Math(9)
    print(G.series)
    print(G.times)

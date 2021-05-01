#gets imports
import random

"""creates list of weightlifting exercises"""
exerciselist = ["curls", "bench press", "tricep extension", "skull crushers", "lateral raises", "shoulder press", "decline press", "cable flies"]

"""creates class to start function"""
class Exercise:

    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 8:
            raise ValueError("Series must be between 0 and 8")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.exercise_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building book series list, this id called from __init__"""
    def exercise_series(self):
        limit = self._series
        f = [(random.sample((exerciselist), k= self._series))]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= self._series

    """Method/Function to set data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters with decorator to allow notation access"""
    @property
    def series(self):
        return self._series
    @property
    def list(self):
        return self._list
    @property
    def number(self):
        return self._list[self._dictID - 1]
    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]

if __name__ == "__main__":
    """Value for testing"""
    a = 2
    """Constructor of Class object"""
    Exercise = Exercise(a/a)
    print(f"Do these weightlifting exercises = {exerciselist.list}")



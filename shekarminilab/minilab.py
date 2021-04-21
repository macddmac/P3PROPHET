import random


workoutlist = ["Standing Forward Bend", "Kneeling Hip Flexor Stretch", "Leg Press", "Barbell Squats", "Jump Squat", "Hack Squat", "Romanian Deadlift", "Standing Calf Raises", "Leg Extensions", "Lying Leg Curls", "Dumbbell Step Ups", "Reverse Lunge", "Walking Lunge"]

class Workouts:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 14:
            raise ValueError("Series must be between 0 and 14")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.workout_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building book series list, this id called from __init__"""
    def workout_series(self):
        limit = self._series
        f = [(random.sample((workoutlist), k= self._series))]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= self._series

    """Method/Function to set data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1


    """Getters with decorator to allow . notation access"""
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
    '''Value for testing'''
    a = 2
    '''Constructor of Class object'''
    Workouts = Workouts(a/a)
    print(f"Here are some book recomendations = {Workouts.list}")



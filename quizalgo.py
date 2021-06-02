class Quiz:
    def __init__(self, user_i):
        self._uk = []

        self._new = []
        if user_i == "yes":
            correct = True
        else:
            correct = False
        if correct:
            self._new.append("Correct")
        else:
            self._new.append("Incorrect")

    @property
    def times(self):
        return self._new

    @property
    def series(self):
        return self._uk


if __name__ == "__main__":
    quiz = Quiz
    print(quiz.uk)
    print(quiz.new)

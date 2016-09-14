class Data:

    def __init__(self, time, gender, height):
        self.time = time
        self.gender = gender
        self.height = height

    def __str__(self):
        return self.time + " " + self.gender + " " + self.height
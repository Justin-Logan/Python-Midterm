class Race:
    def __init__(self, num_horses):
        self.horses = [f"Horse {i+1}" for i in range(num_horses)]

    def shuffle(self):
        from random import shuffle

        shuffle(self.horses)
        return self.horses

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        pass

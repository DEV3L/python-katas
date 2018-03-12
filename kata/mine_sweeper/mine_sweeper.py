class MineSweeper:
    def __init__(self, mine_field: str):
        self.mine_field = mine_field

    @property
    def columns(self):
        size = self.mine_field.split('\n')[0]
        return int(size.split(' ')[0])

    @property
    def field(self):
        return self.mine_field

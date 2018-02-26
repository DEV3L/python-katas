class BuildStatus:

    def __init__(self, *, branch_name: str, number: int, status: str, time: str):
        self.branch_name = branch_name
        self.number = number
        self.status = status
        self.time = time

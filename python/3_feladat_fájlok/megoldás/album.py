class Album:
    def __init__(self, data: str):
        splittedData: list = data.strip().split(";")
        self.artist: str = splittedData[0]
        self.album: str = splittedData[1]
        self.date: str = int(splittedData[2])
        self.genre: str = splittedData[3]
        self.sales: str = int(splittedData[4])
        self.price: float = round((self.sales*1000000) * 20.57, 2)
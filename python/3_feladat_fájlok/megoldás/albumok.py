# 1. feladat ----------------------------------------------------
from album import Album

listOfAlbum: list[Album] = []

# 2. feladat ----------------------------------------------------
def readFromFile(fileName: str):
    with open(fileName, 'r', encoding="UTF-8") as f:
        f.readline()
        for line in f.readlines():
            newAlbum: Album = Album(line)
            listOfAlbum.append(newAlbum)

# 4. feladat ----------------------------------------------------
def saleOver(comSale: int):
    overNum: int = 0
    for al in listOfAlbum:
        if al.sales > comSale:
            overNum += 1
    return overNum

# 6. feladat ----------------------------------------------------
def searchByGenre(genre: str):
    searchList: list[Album] = []
    for al in listOfAlbum:
        if al.genre.capitalize().find(genre.capitalize()) != -1:
            searchList.append(al)
    return searchList

# 7. feladat ----------------------------------------------------
def getAlbumStat():
    stat: dict[str, int] = {}
    for al in listOfAlbum:
        if al.artist not in stat.keys():
            stat[al.artist] = 1
        else:
            stat[al.artist] += 1
    return stat

# 8. feladat ----------------------------------------------------
def getSaleProfit():
    stat: dict[str, int] = {}
    for al in listOfAlbum:
        if al.artist not in stat.keys():
            stat[al.artist] = al.price
        else:
            stat[al.artist] += al.price
    return stat

# 9. feladat ----------------------------------------------------
def writeToFile(newFileName: str, profits: dict[str, int]):
    with open(newFileName, 'w', encoding="UTF-8") as f:
        for i in range(0, 3):
                artist = max(profits, key=profits.get)
                profit = profits.pop(artist)
                f.write(f"{i+1}. helyezet: {artist} - {int(profit*357.64):,} FT\n")
        

def main():
    readFromFile("albumok.csv")
    lenghtOfList: int = len(listOfAlbum)
    print(f"3. feladat: A listában {lenghtOfList} album szerepel.")
    overNum: int = saleOver(42)
    print(f"4. feladat: Összesen {overNum} album haladata meg a 42 milliós eladási számot.")
    searchedGenre: str = input("5. feldat: Adjon meg egy műfajt: ")
    print("6. feladat: Műfaj keresés:")
    searchAlbums: list[Album] = searchByGenre(searchedGenre)
    if len(searchAlbums) == 0:
        print("Nincs ilyen műfajú album az állományban!")
    else:
        for al in searchAlbums:
            print(f"\t{al.artist} - {al.album}")
    stats: dict[str, int] = getAlbumStat()
    print("7. feladat: Toplistás albumok")
    for name, albumNum in sorted(stats.items()):
        if albumNum > 1:
            print(f"\t{name} - {albumNum} toplistás album")
    profits: dict[str, int] = getSaleProfit()
    writeToFile("topthree.txt", profits)

if __name__ == "__main__":
    main()
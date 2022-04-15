from glicko2 import *

def main():

    na = Player("me", 1500, 350, .06)
    fh = Player("fishhook",1500,350,.06)
    carty = Player("carty",1500,350,.06)
    merk = Player("merk",1500,350,.06)
    na.update_player([1500,1500,1500],[350,350,350],[0,1,0])
    print(na.rating)
    print(na.rd)
    print(na.vol)

if __name__ == "__main__":
    main()
from itertools import islice
def snakes():
    fruit = "5,5 8,17 5,2 17,14 2,4 17,6 17,17 1,1 2,3 4,9 13,2 12,15 18,15 12,1 17,5 2,14 7,3 17,6 7,13 6,5 5,17 17,12 16,7 15,15 14,14 10,8 15,5 12,12 9,18 7,16 1,3 16,13 12,11 13,6 11,1 5,4 15,8 6,3 5,14 5,3 5,1 17,12 10,14 13,14 18,14 6,14 7,1 15,16 13,4 18,3 9,1 3,13".split(" ")
    for i in range(len(fruit)):
        fruit[i] = fruit[i].split(",")
        fruit[i][0], fruit[i][1] = int(fruit[i][0]), int(fruit[i][1])
    n = 0 #Which fruit number we are on

    moves = "RRRRRRRRRRDDDDDDDDDDUUUUULLLLLLDDDDDDDDDDDDRRRRRRUUUUUUUUUUULLLLLLUUUURRDDRDRDDRDRDRDRDDDDRRRRRRUULLLLLLDLDLDLUUUUUUUULLLLLLLLUUURRRRDDDRRRRRRRRRRRRUUULLDDDRRDDDDDDDDDDLLLLLLLLLLLUUUUUUUUUUUUUUUULLLLLDDDRURRDDDDDDLLDRRRRRRUUUUUUURURRRRRRDDDDDDDDDDDDDLLLLLDRRRRRRRRUUUUUULLLLLLLUUUUUUUUURRRDDDDDDLLLDDRRRRUUUUURRDDDDDDLLLLLLLLLLLLLLLDDDDRRRRUUURUUUUUUUUURRRRRDDDDRRRRRDDDDDDLLLLLLDLLLLLUUUUUUUUURRDDDDDDDDDDDDDLLLLUUUUURRRUUURRDDDDLLDRRRRRRRRRRUUUUUUULLLDDDRDDDLLLDDRRRRRRUUUUUUUUUUUUULLLLDDDDDDDDDDDDDDLLLLUUUUUUUUUUURRRRRRRDDDDDDDLLLLLLDDDDDLDLLLUUUUUULLLLLLLUUUUUUUUURRRRRRRRRDDDDDDDDDDRRRRRRRRUULLLLLLUUUUURRRUUUUULLLLDDLDLLLLLDDDDRRRRRRRRRRRRRUUUUUUUULLLLLLLLLLLDDDDLLLDDDDDDDDDDRRRRRRRRRRRRRRRUUUUUUUUUULLLLLLLLLULLLLLLLUURRRRRRRRRRRRRRRRRDDDDDDDDDDDLLLLLLLLLDDDDLLLLLLLLDRRRRRRRRRUUURRRRRRRRDDDDLLLLLLLLLLLLLLLLLLUUUURRRRRRRULLLLLLLUUUUUUUUUUUURRRRRRRRDDDDDRDDDDDDDDDDDRRRRRDRRRRUULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRUULLLLLLLLLLLLLLLLDDDDDDDD"

    height = 20
    width = 20

    score = 0
    length = 1
    x =[0]
    y = [0]
    print(fruit)

    for i in moves:
        
        print(x[0], y[0], fruit[n][0], fruit[n][1])
        if (x[0] == fruit[n][0]) and (y[0] == fruit[n][1]):
            length += 1
            x.append(x[-1])
            y.append(y[-1])
            n += 1
            score += 100
            print("fruit")

            for o in range(length-2, 0, -1):
                x[o] = x[o-1]
                y[o] = y[o-1]
        else:
            for o in range(length-1, 0, -1):

                x[o] = x[o-1]
                y[o] = y[o-1]
 
        print(i)
        if i == "D":
            y[0] += 1
        if i == "U":
            y[0] -= 1
        if i == "L":
            x[0] -= 1
        if i == "R":
            x[0] += 1

        print(x, "\n", y)

        for o in range(1, length):
            if (x[0] == x[o]) and (y[0] == y[o]):                
                print("Self Collision")
                return score
        if (x[0] >= width) or (x[0] < 0) or (y[0] < 0) or (y[0] >= height):
            print("Side collision")
            break
        
        print("Score:", score, "\n")
        score += 1

print(snakes())

# https://adventofcode.com/2020/day/1


def load_data(filename):
    global lines
    with open(filename, "r") as input_data:
        lines = input_data.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()


def myHelperFunction():
    global lines
    pass

def problemOne():
    global lines
    
    for a in lines:
        for b in lines:
                x = int(a)
                y = int(b)
                if 2020 == x + y:
                    print(x,y,x+y,x*y)
                    return x*y


    pass

def problemTwo():
    global lines

    for a in lines:
        for b in lines:
            for c in lines:
                x = int(a)
                y = int(b)
                z = int(c)
                if 2020 == x + y + z:
                    print(x,y,z,x+y+z,x*y*z)
                    return x*y*z

    pass

if __name__ == "__main__":
    load_data("day1-input.txt")
    # problemOne()
    # problemTwo()
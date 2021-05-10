import math


def run():
    my_dictroot = {i: round(math.sqrt(i), 2) for i in range(1, 1001)}
    print(my_dictroot)


if __name__ == "__main__":
    run()
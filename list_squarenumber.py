def run():
    square_list = []
    for i in range(1, 101):
        if i%3!=0:
            square_list.append(i**2)
    
    print(square_list)


if __name__ == "__main__":
    run()
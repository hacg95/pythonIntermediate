def run():
    my_list = [2, "Love", True, 3.14]
    my_dict = {"firsname": "Harold", "lastname": "Carrillo"}

    super_list = [
        {"firsname": "Harold", "lastname": "Carrillo"},
        {"firsname": "Karen", "lastname": "Alviarez"},
        {"firsname": "Fabián", "lastname": "Becerra"}
    ]

    super_dict = {
        "integer_nums": [-2, 5, 8, 14, 22],
        "floating_nums": [-1.4, -2.7, 0.9, 1.5, 4.6]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for i in super_list:
        print(i)


if __name__ == "__main__":
    run()
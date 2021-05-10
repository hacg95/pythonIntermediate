def run():
    # Filter function
    my_list1 = [1,2,3,4,5,6,7,8,9]
    odd = list(filter(lambda x: x%2 != 0, my_list1))
    print(odd)

    # Map function
    my_list2 = [1,2,3,4,5]
    square = list(map(lambda x: x**2, my_list2))
    print(square)

    # Reduce function
    from functools import reduce 
    my_list3 = [2,2,2,2,2]
    all_multiplied = reduce(lambda a,b: a*b, my_list3)
    print(all_multiplied)


if __name__ == "__main__":
    run()
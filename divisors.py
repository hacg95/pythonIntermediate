def divisors(num):
    divisor = [i for i in range(1, num+1) if num%i==0]
    return divisor


def run():
    try:
        num = int(input("Insert a number: "))
        try:
            if num<0:
                raise ValueError("Negative numbers not allowed")
            return print(divisors(num))
        except ValueError as ve:
            print(ve)
            return False
    except ValueError:
        print("You have to insert a number")


if __name__ == "__main__":
    run()
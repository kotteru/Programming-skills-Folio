def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"


def main():
    num = int(input("Enter a number: "))
    message = check_even_odd(num)
    print(message)


if __name__ == "__main__":
    main()

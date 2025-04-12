def main():

    try:
        a = int(input("Enter a number: "))
        print(a)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("I am inside Finally.")
        # Finally block will always execute, even if function returns or raises an exception.

main()
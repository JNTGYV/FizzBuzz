def fizzBuzz(minNum, MaxNum):
    for num in range(1, 101):
        result = ""
        if num % 3 == 0:
            result += "Fizz"
        if num % 5 == 0:
            result += "Buzz"
    
        print(result or num)



def main():
    fizzBuzz(1,101)


if __name__ == "__main__":
    main()
>>>>>>> Stashed changes

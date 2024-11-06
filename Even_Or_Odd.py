#Austin Lindstrom
#Program - Determines if a number is Even or Odd

print('Please enter any number')
num = int(input())


def main(num):
    if num % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    print (result)
    return result

main(num)
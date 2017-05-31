#!/usr/bin/python
import sys
import random

def main():
    range_max_text = "Enter testing range maximum (minimum is 0):"
    operation_text = "\nChoose excercises operation:\n 1 - Sum\n 2 - Multiplicate\n 3 - Substract\n 4 - Divide\nOr any other number to exit."
    excercises_text = "\nEnter number of excercises with this operation:"
    range_max = enter_int(range_max_text)
    is_running = False
    operation = enter_int(operation_text)
    if 1 <= operation <= 4:
        is_running = True

    while is_running:
        excercises = enter_int(excercises_text)
        improve = True
        while improve:
            improve = testing(range_max, operation, excercises)
        operation = enter_int(operation_text)
        if not 1 <= operation <= 4:
            is_running = False

    print ("\nGood bye!")

def testing(rng, operation, tests):
    attempt = 0
    correct = 0
    while attempt != tests:
        if test_func[operation](rng):
            correct += 1
        attempt += 1
    print ("Your score is {} from {} ({}%)".format(correct, tests, correct/tests*100))
    print ("Press \"Y\" if you want to improve your results.")
    q = input()
    if q.lower() == "y":
        return True
    return False

def sum_test(maximum):
    elem = list([random.randint(0, maximum) for i in range(2)])
    answer = enter_int("{} + {} = ... ?".format(elem[0], elem[1]))
    if answer == elem[0] + elem[1]:
        print("Correct\n")
        return True
    else:
        print("Wrong. Correct answer is %i\n" %(elem[0] + elem[1]))
        return False

def mult_test(maximum):
    elem = list([random.randint(0, maximum) for i in range(2)])
    answer = enter_int("{} * {} = ... ?".format(elem[0], elem[1]))
    if answer == elem[0] * elem[1]:
        print("Correct\n")
        return True
    else:
        print("Wrong. Correct answer is %i\n" %(elem[0] * elem[1]))
        return False

def sub_test(maximum):
    elem = list([random.randint(0, maximum) for i in range(2)])
    elem.append(elem[0] + elem[1])
    answer = enter_int("{} - {} = ... ?".format(elem[2], elem[0]))
    if answer == elem[2] - elem[0]:
        print("Correct\n")
        return True
    else:
        print("Wrong. Correct answer is %i\n" %(elem[2] - elem[0]))
        return False

def div_test(maximum):
    elem = list([random.randint(0, maximum) for i in range(2)])
    #To prevent zero division
    while elem[0] == 0:
        elem[0] = random.randint(0, maximum)
    elem.append(elem[0] * elem[1])
    answer = enter_int("{} / {} = ... ?".format(elem[2], elem[0]))
    if answer == elem[2] // elem[0]:
        print("Correct\n")
        return True
    else:
        print("Wrong. Correct answer is %i\n" %(elem[2] // elem[0]))
        return False

def enter_int(text):
    count = 0
    while count != wrong_enter_attempts:
        try:
            print (text)
            var = int(input())
            if var < 0:
                raise ValueError
        except ValueError:
            print ("Sorry, enter a valid number please (%i more attempts)\n" %(wrong_enter_attempts-count-1))
            count += 1
        else:
            break
    else:
        print ("No number was entered. Program terminated.")
        sys.exit()
    return var

test_func = {
    1 : sum_test,
    2 : mult_test,
    3 : sub_test,
    4 : div_test
}
wrong_enter_attempts = 3

if __name__ == "__main__":
    main()
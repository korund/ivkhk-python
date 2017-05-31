import datetime

def main():
    print ("Personal code tester\nAuthor: Konstantinov Rudolf")
    while True:
        code = enter_id()
        if is_end(code):
            break
        
        print ("Correct personal code\n")
        code_list = [int(sym) for sym in code]
        gender = code_list[0] % 2
        bd_year = (start_century + (code_list[0]-1) // 2) * 100 + code_list[1] * 10 + code_list[2]
        bd_month = code_list[3] * 10 + code_list[4]
        bd_day = code_list[5] * 10 + code_list[6]
        birthdate = datetime.date(bd_year, bd_month, bd_day)
        age = int((datetime.date.today() - birthdate).days / days_per_year)
        print ("Personal info")
        print ("Gender: ", end="")
        if gender == 0:
            print ("Female")
        else:
            print ("Male")
        print ("Birthdate: {}.{}.{}".format(bd_day, bd_month, bd_year))
        if datetime.date.today().month == bd_month and datetime.date.today().day == bd_day:
            print ("Happy birthday!")
        print ("Age: ", age)

def enter_id():
    while True:
        print ("\n" + "-"*50)
        print ("Enter your personal code (11 digits) or \"Q\" to exit:")
        code = input()
        if is_end(code) or is_valid(code):
            return code
        else:
            print("Sorry, enter a valid code please\n")

def is_valid(code):
    #should be 11 digits
    if len(code) != 11:
        return False
        
    #check, if all symbols are digits and count a checksum
    try:
        checksum = [0, 0]
        for i, item in enumerate(code):
            current = int(item)
            checksum[0] += current*weight_array[0][i]
            checksum[1] += current*weight_array[1][i]
    except ValueError:
        return False
        
    #check last digit
    if checksum[0] % 11 < 10:
        if int(code[-1]) != checksum[0] % 11:
            return False
    elif checksum[1] % 11 < 10:
        if int(code[-1]) != checksum[1] % 11:
            return False
    elif int(code[-1]) != 0:
            return False
    return True
    
def is_end(code):
    if code.lower() == "q":
        return True
    return False
    
start_century = 18
days_per_year = 365.242374
#11 elements. The last one is checknumber mask
weight_array = [[1,2,3,4,5,6,7,8,9,1,0],\
                [3,4,5,6,7,8,9,1,2,3,0]]
#test ID's
c1 = "39307080077"
c2 = "38602090338"
c3 = "39312070005"
c4 = "39312080001"
c5 = "39312090001"
c6 = "39312100006"

if __name__ == "__main__":
    main()
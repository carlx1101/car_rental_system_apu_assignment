
# Group Member 
# YIP KAR FAI  
# TP060711 
# NG LI SHENG   
# TP060612
import datetime
from datetime import datetime, timedelta


# Function to allow registered customer to recover their account
def accountRecovery():
    print("Welcome to Car Rental Management System (Account Recovery)\n".center(100))
    # userInput phone number
    searchContact = input("Please enter phone number:")
    # Open file to read data
    with open('userDatabase.txt', 'r') as data:
        # Read every lines of the file into a list
        temp = data.readlines()
        # Check data in file from 0 index to last index
        data.seek(0)
        # Loop through line of list
        for line in temp:
            # Check if searchcontact leave empty
            if searchContact == "":
                print("please enter something")
            # Check if searchContact in list 
            if searchContact in line:
                print("-"*106)
                print("This is your account credentials".center(100))
                print("-"*106)
                print(line)
            else:
                print("Please enter correct phone number")


# Function to delete account of registered customer
def disableUserAccount():
    # userInput password
    password = input("Please enter password  : ")
    databse = 'userDatabase.txt'
    # Open file to read data
    with open(databse, 'r+') as data:
        # Read every lines of the file into a list
        temp = data.readlines()
        # search data in file from 0 index to last index
        data.seek(0)
        # Loop through line of list
        for line in temp:
            # Check if not password in list
            if not password in line:
                # Write line into files
                data.write(line)
        
        data.truncate()
    print("Account has been disbale") 


# Function for unregistered user to register 
def userRegister():
        print("Sign up")
        #userInput username, password, emailaddress, and contactNumber
        username = str(input("Please enter Username: "))
        password = input("Please enter Password: ")
        emailAddress = input("Please enter Email: ")
        contactNumber = input("Please enter contact: ")

        #Open file to append data of userInput
        open('userDatabase.txt', 'a').close()

        #Open file to read data
        with open("userDatabase.txt","r") as userAccountData:
            #Read every lines of the file into a list
            lines = userAccountData.readlines()
            #Loop through line of list
            for line in lines:
                #Strip spaces across line and split space between line
                rec = line.strip("\n").split(" ")
                #Check if username or password equal to the record of the file
                if "Username:"+username == rec[0] or "Password:"+password == rec[1]:
                    print("account existed")
                    return main()
                #Check if username or password are leaving empty
                elif username  == "" or password == "":
                    print("username and password cannot be empty")
                    return main()
                
        # Open file to append and write userAccountData into it
        with open("userDatabase.txt","a+") as userAccountData:
            userAccountData.write(f"Username:{username} Password:{password} EmailAddress:{emailAddress} Contact:{contactNumber}\n") 
            print("Account succesfully Registered")
        return main()
                    





# Function to check our license info
def license():
    github_Link = "https://github.com/carlx1101/car_rental_system_apu"
    while True:
        print("Thank you for Supporting Our System")
        print("License: "+"MIT License")
        print("Github Repo: "+github_Link)
        #userInput option(number)
        userDecision = int(input("Press 1 to exit:"))
        if userDecision == 1:  
            print("  _______ _                 _     __     __       ")
            print(" |__   __| |               | |    \ \   / /       ")
            print("    | |  | |__   __ _ _ __ | | __  \ \_/ /__ ")
            print("    | |  | '_ \ / _` | '_ \| |/ /   \   / _ \| | | |")
            print("    | |  | | | | (_| | | | |   <     | | (_) | |_| |")
            print("    |_|  |_| |_|\__,_|_| |_|_|\_\    |_|\___/ \__,_|")

            return main()
        else:
            continue


# Function for Registered customer Login
def userLogin():
    authentication = True
    while authentication:
        print("Login")
        # userInput username and password
        username = str(input("Please enter Username: "))
        password = input("Please enter Password: ")
        # Check Username and Password is Same As the List
        with open("userDatabase.txt","r") as userAccountData:
            #Read every lines of the file into a list
            lines = userAccountData.readlines()
            #loop through line of list
            for line in lines:
                # Strip spaces across line and split space between line
                rec = line.strip("\n").split(" ")
                # Check if username and password are equal to the record
                if "Username:"+username == rec[0] and "Password:"+password == rec[1]:
                    authentication = False
        #Check if authentication is False
        if authentication == False:
            print(f"Login succesfully! Welcome {username}")
            return userMenu() 
        else:
            print("Invalid Username and Password")
            return main() 


# Function for admin to add cars to be rented out 
def addCars():
    carStatus = "available"
    # userInput number of cars
    numberOfCars = int(input("Please enter number of cars you wish to add:"))
    # Looping through userInput for car numbers
    for count in range(numberOfCars):
        # userInput carid, modelname, vehicletype, and priceperday
        carID = input("Please enter car ID:")
        modelName = input("Please enter car model name:")
        vehicleType = input("Please enter vehicle type:")
        pricePerDay = input("Please enter price per day:")

        print("-"*106)
        print("Car have succesfully added!")
        print("carID:", carID) 
        print("ModelName:", modelName) 
        print("vehicleType:", vehicleType) 
        print("PricePerDay:", pricePerDay)
        print("Status:", carStatus)
        print("-"*106)

        # Open file to append data into it
        with open('carsDatabase.txt', 'a') as cars:
                cars.write(f"CarID:{carID} ModelName:{modelName} VehicleType:{vehicleType} Price:{str(pricePerDay)} Status:{carStatus}\n")


# Function for admin to modify car detail
def modifyCarDetails():
    # Loop through function
    try:
        while True:
            carList= []
            carNotRentOut()
            # Open file to read data
            with open("carsDatabase.txt","r") as carFile:
                # userInput carid
                carID = input("Please enter car ID you wish to modify:")
                modify = 0
                # Loop through line of file
                for line in carFile:
                    # Strip spaces across line and split space between line
                    record = line.strip().split(" ")
                    # Check if userInput carID equal to record
                    if "CarID:"+carID == record[0]:
                        print("1.",record[0])
                        print("2.",record[1])
                        print("3.",record[2])
                        print("4.",record[3])
                        # userInput Option
                        inputNum = int(input("Please Enter A Record Number to Modify: "))
                        print("-"*100)
                        print("Dear Admin, Please Modify [EXACTLY BASED ON FORMAT BELOW]:)")
                        print(record[inputNum-1])
                        print("-"*100)
                        print("CarID: (New Values)")
                        print("ModelName:(New Values)")
                        print("VehicleType:(New Values)")
                        print("Price:(New Values)")
                        print("-"*100)
                        # Check if userInput inputNum is equal to 1
                        if inputNum-1 == 0:
                            # userInput new carid
                            new = input("Please Enter New CarID:")
                            stringOne = "CarID:"
                            # To concatenate CarID:(New CarID)
                            record[inputNum-1] =  str(stringOne + new)
                        # Check if userInput inputNum is equal to 2
                        if inputNum-1 == 1:
                            # userInput new modelname
                            new = input("Please Enter New ModelName:")
                            stringTwo = "ModelName:"
                            # To concatenate ModelName:(New ModelName)
                            record[inputNum-1] =  str(stringTwo + new)
                        # Check if userInput inputNum is equal to 3  
                        if inputNum-1 == 2:
                            #userInput new vehicletype
                            new = input("Please Enter New VehicleType:")
                            stringThree = "VehicleType:"
                            # To concatenate VehicleType:(New VehicleType)
                            record[inputNum-1] =  str(stringThree + new)
                        # Check if userInput inputNum is equal to 4
                        if inputNum-1 == 3:
                            # userInput new price
                            new = input("Please Enter New Price:")
                            stringFour = "Price:"
                            # To concatenate Price:(New Price)
                            record[inputNum-1] =  str(stringFour + new)
                        modify = 1
                    # Append record to carList
                        print(record) 
                    carList.append(record)
            # Check if modify is false
            if modify == 0:
                print("The value not exist")
            else:
                # Open file to write carFile data into it
                with open("carsDatabase.txt","w") as carFile:
                    i = 0
                    # Loop through length of carList which is smaller than i
                    while (i < len(carList)):
                        # Join carList[i] with spaces between line in newRecord
                        newRecord = " ".join(carList[i])
                        # Write newRecord in file with spaces across line
                        carFile.write(newRecord+"\n")
                        i += 1

            # userInput Option (y/n)
            remodify = input("Dear Admin, do you wish to remodify? YES ENTER (y), NO ENTER (n):")
            # Check if userInput is n/N
            if remodify == "n" or remodify == "N":
                break
    except IndexError:
        print("please only select above field number")
        return adminMenu()        


# Function for registered customer to modify their account
def modifyUser():
    try:
        # Loop through function
        while True:
            userList= []
            # Open file to read data
            with open("userDatabase.txt","r") as userFile:
                # userInput password
                password = input("Please enter your password: ")
                modify = 0
                # Loop through line of file
                for line in userFile:
                    # Strip spaces across line and split space between line
                    record = line.strip().split(" ")
                    # Check if userInput password is equal to record
                    if "Password:"+password == record[1]:
                        print("1.",record[0])
                        print("2.",record[1])
                        print("3.",record[2])
                        print("4.",record[3])
                        # userInput option
                        inputNum = int(input("Please Enter A Record Number to Modify: "))
                        print(record[inputNum-1])
                        print("Dear Customer, Please Modify [EXACTLY BASED ON FORMAT BELOW]:)")
                        print("-"*100)
                        print("Username:(New Value)")
                        print("Password:(New Value)")
                        print("EmailAddress:(New Value)")
                        print("Contact:(New Value)")
                        print("-"*100)
                        # Check if userInput inputNum is 1
                        if inputNum-1 == 0:
                            # userInput new username
                            new = input("Please Enter New Username:")
                            stringOne = "Username:"
                            # To concatenate Username:(New Username)
                            record[inputNum-1] =  str(stringOne + new)
                        # Check if userInput inputNum is 2
                        if inputNum-1 == 1:
                            #userInput new password
                            new = input("Please Enter New Password:")
                            stringTwo = "Password:"
                            # To concatenate Password:(New Password)
                            record[inputNum-1] =  str(stringTwo + new)
                        # Check if userInput inputNum is 3 
                        if inputNum-1 == 2:
                            #userInput new emailaddress
                            new = input("Please Enter New EmailAddress:")
                            stringThree = "EmailAddress:"
                            # To concatenate EmailAddress:(New EmailAddress)
                            record[inputNum-1] =  str(stringThree + new)
                        # Check if userInput inputNum is 4
                        if inputNum-1 == 3:
                            # userInput new contact
                            new = input("Please Enter New Contact:")
                            stringFour = "Contact:"
                            # To concatenate Contact:(New Contact)
                            record[inputNum-1] =  str(stringFour + new) 
                        modify = 1
                        print(record)
                    # Append all record in userList
                    userList.append(record)
            # Check if modify is false
            if modify == 0:
                print("Dear User, You Have Enter Wrong Password")
            else:
                # Open file to write userFile data into it
                with open("userDatabase.txt","w") as userFile:
                    i = 0
                    # Loop through length of userList which is smaller than i
                    while (i < len(userList)):
                        # Join userList[i] with spaces between line in newRecord
                        newRecord = " ".join(userList[i])
                        # Write newRecord in file with spaces across line
                        userFile.write(newRecord+"\n")
                        i += 1
            # userInput Option (y/n)
            remodify = input("Dear User, do you wish to remodify? YES ENTER (y), NO ENTER (n):")
            # Check if userInput is n/N
            if remodify == "n" or remodify == "N":
                break

    except IndexError:
        print("please only select above field number")
        return userMenu()   

# Function for registered customer to book car
def bookCar(): 
    carNotRentOut()
    # userInput carid
    chooseCar = input("Please enter carID you wish to book: ")
    # Open file to read carAccountData into it
    with open("carsDatabase.txt","r") as carAccountData:
        # Read every lines of the file into a list
        lines = carAccountData.readlines()
        # Remove Price: in all line of the file
        lines = [line.replace('Price:', '') for line in lines]
        # Loop through line of list
        for line in lines:
            # Strip spaces across line and split space between line
            record = line.strip("\n").split(" ")
            # Check if userInput carID is equal to the record
            if "CarID:"+chooseCar == record[0]:
                print("This is the details of your selections:")
                print(record[0])
                print(record[1])
                print(record[2])
                print("Price:",record[3])
                print(record[4])
                print("-"*100)
                print("Welcome to Car Rental Management System (Registered Customer)\n".center(100))
                print("Please fill your information below")
                # userInput bookname, idnumber, inputDate, and week        
                bookName = input("Please enter your name:")
                idNumber = input("Please enter your IC number:")
                inputDate = input("Please enter a date for renting the car (in format YYYY-MM-DD HH:MM): ")
                rentDate = datetime.strptime(inputDate, "%Y-%m-%d %H:%M")
                # userInput total week to rent car 
                week = int(input("Please enter the total weeks you want to rent the car: "))
                returnDate = rentDate + timedelta(weeks = week)
                day = week * 7
 
                print("-"*100)
                print("Welcome to Car Rental Management System (Registered Customer)\n".center(100))
                print("This is Your Payment Receipt")
                print("-"*100)
                print(record[0])
                print(record[1])
                print(record[2])
                totalPrice = int(record[3]) * int(day)
                print("TotalPrice:",totalPrice)
                str(record[3])
                print("-"*100)
                print("This is your total car rent duration:")
                print("-"*100)
                print("Total Week Rent:", week, "week")
                print("Total Day Rent:", day, "day")
                print("Your Rent Date and Time:", rentDate)
                print("Your Return Date and Time:", returnDate)
                print("Payment Has Been Made! Thank you!")
                print("-"*106)
                # Open file to append data into it
                with open('transactionsDatabase.txt', 'a') as transaction:
                        transaction.write(f"BookerName:{bookName} ICNumber:{idNumber} {record[0]} {record[1]} {record[2]} RentDate:{str(rentDate)} ReturnDate:{str(returnDate)} TotalPrice:{str(totalPrice)}\n")
 
    carList= []
    with open("carsDatabase.txt","r") as carFile:
        # Loop through line of file
        for line in carFile:
            # Strip spaces across line and split space between line
            record = line.strip().split(" ")
            # Check if userInput carID is in record
            if "CarID:"+chooseCar == record[0]:
                # If Yes change available status to unavailable
                record[4] = "Status:unavailable"
            # Append record into carList
            carList.append(record)
    # Open file to write carFile data into it
    with open("carsDatabase.txt","w") as carFile:
        i = 0
        # Loop thorugh length of carList which is smaller i
        while (i < len(carList)):
            # Join carList[i] with spaces between line in newRecord
            newRecord = " ".join(carList[i])
            # Write newRecord in file with spaces across line
            carFile.write(newRecord+"\n")
            i += 1


# Function for admin to return unavailable car
def returnRentedCar():
    carRentOut()
    #userInput carid
    chooseCar = input("Please enter carID you wish to return: ")
    # Open file to read data
    with open("carsDatabase.txt","r") as carAccountData:
        # Read every lines of the file into a list
        lines = carAccountData.readlines()
        # Loop through line of list
        for line in lines:
            # Strip spaces across line and split space between line
            record = line.strip("\n").split(" ")
            # Check if userInput carID is in record
            if "CarID:"+chooseCar == record[0]:
                print("This is your returned carID:")
                print(record[0])
                print(record[1])
                print(record[2])
                print(record[3])
                print("You have successfully return the car")
 
    carList= []
    # Open file to read data
    with open("carsDatabase.txt","r") as carFile:
        # Loop through line of file
        for line in carFile:
            # Strip spaces across line and split spaces between line
            record = line.strip().split(" ")
            # Check if userInput carId is in record
            if "CarID:"+chooseCar == record[0]:
                # If Yes change unavailable status to available
                record[4] = "Status:available"
            # Append record into carList
            carList.append(record)
    # Open file to write carFile data into it
    with open("carsDatabase.txt","w") as carFile:
        i = 0
        # Loop thorugh length of carList which is smaller i
        while (i < len(carList)):
            # Join carList[i] with spaces between line in newRecord
            newRecord = " ".join(carList[i])
            # Write newRecord in file with spaces across line
            carFile.write(newRecord+"\n")
            i += 1


# Function for displaying available car for rent
def carNotRentOut():
    print("-"*106)
    print("Available Cars For Rent".center(100))
    print("-"*106)
    lines = []
    # Open file to read data
    with open('carsDatabase.txt', 'r') as carAccountData:
        # Read every lines of the file into a list
        lines = carAccountData.readlines()
    i = 0
    # Loop through line of list
    for line in lines:
        # Check if Status:available in the list
        if "Status:available" in line:
            i += 1
            print(f"{i}.car = {line}")
    print("-"*106)


# Function for displaying all rented car
def carRentOut():
    print("-"*106)
    print("Rented Out Cars".center(100))
    print("-"*106)
    lines = []
    # Open file to read data
    with open('carsDatabase.txt', 'r') as carAccountData:
        # Read every lines of the file into a list
        lines = carAccountData.readlines()
    i = 0
    # Loop through line of list
    for line in lines:
        # Check if Status:unavailable in the list
        if "Status:unavailable" in line:
            i += 1
            print(f"{i}.car = {line}")
    print("-"*106)


# Function for displaying customer booking and payment
def cusBookAndPay():
    print("-"*106)
    print("Customer Booking and Payment".center(100))
    print("-"*106)
    lines = []
    # Open file to read data
    with open('transactionsDatabase.txt', 'r') as carAccountData:
        # Read every lines of the file into a list
        lines = carAccountData.readlines()
    i = 0
    # Loop through line of list
    for line in lines:
        i += 1
        print(f"{i}.Booking = {line}")
    print("-"*106)


# Function for admin to search specific customer booking
def searchCusBook():
    print("-"*106)
    print("Search Customer Booking".center(100))
    print("-"*106)
    # userInput customer name
    search = input("Please enter customer name to check booking history: ")
    print("-"*106)
    print(f"Booking history of {search} customer".center(100))
    print("-"*106)
    # Open file to read data
    with open('transactionsDatabase.txt', 'r') as data:
        # Read every lines of the file into a list
        lines = data.readlines()
        # Loop through line of list
        for line in lines:
            # Strip spaces across line and split space between line
            record = line.strip("\n").split(" ")
            # Check if bookerName userInput is equal to the list
            if "BookerName:"+search == record[0]:
                print(record[0],"\t",record[1],"\t",record[2],"\t",record[3],"\t",record[4])


# Function for admin to search specific customer payment
def searchCusPay():
    print("-"*106)
    print("Search Customer Payment".center(100))
    print("-"*106)
    # userInput customer name
    search = input("Please enter customer name to check payment history: ")
    print("-"*106)
    print(f"Payment history of {search} customer".center(100))
    print("-"*106)
    # Open file to read data
    with open('transactionsDatabase.txt', 'r') as data:
        # Read every lines of the file into a list
        lines = data.readlines()
        # Loop through line of list
        i = 1
        for line in lines:
            # Strip spaces across line and split space between line
            record = line.strip("\n").split(" ")
            # Check if bookerName userInput is equal to the list
            if "BookerName:"+search == record[0]:
                print(i,".\t",record[0],"\t",record[1],"\t",record[9])
                print("\t",record[5],"\t","RentTime:",record[6],"\t",record[7],"\t","ReturnTime:",record[8],"\n")
                i += 1


# Function for registered customer to check personal booking history
def history():
    print("-"*106)
    print("Search Rent History".center(100))
    print("-"*106)
    #userInput ic number
    search= input("Please enter IC:")
    print("-"*106)
    print("Your personal booking history".center(100))
    print("-"*106)
    with open('transactionsDatabase.txt', 'r') as data:
        # Read every lines of the file into a list
        lines = data.readlines()
        # Loop through line of list
        i = 1
        for line in lines:
            # Strip spaces across line and split space between line
            record = line.strip("\n").split(" ")
            # Check if ICNumber userInput is equal to the list
            if "ICNumber:"+search == record[1]:
                print(i,".\t",record[3],"\t",record[4],"\t",record[9])
                print("\t",record[5],"\t","RentTime:",record[6],"\t",record[7],"\t","ReturnTime:",record[8],"\n")
                i += 1
 

# Function for access userMenu page
def userMenu():
    while True:
        print("-"*106)
        print("Welcome to Car Rental Management System (Registered Customer/ User Menu)\n".center(100))
        print("Please select an option:")
        print("1.Modify Personal Details.")
        print("2.View Personal Rental History.")
        print("3.View Detail of Cars to be Rented Out.")
        print("4.Select and Book a car for a specific duration.")
        print("5.Disable user account.")
        print("6.Log Out")
        # userInput Option
        userDecision = int(input("Please enter your option: "))
        if userDecision == 1:
            modifyUser()
            continue
        elif userDecision == 2:
            history()
            continue
        elif userDecision == 3:
            carNotRentOut()
            continue
        elif userDecision == 4:
            bookCar()
            continue
        elif userDecision == 5:
            disableUserAccount()
            return main()
        elif userDecision == 6:
            return main()
        else:
            print("Please select option again")


# Function for access adminMenu page
def adminMenu():
    while True:
        print("-"*106)
        print("Welcome to Car Rental Management System (Administrator/ Menu)\n".center(100))
        print("Please select an option: ")
        print("1. Add Cars to be rented out ")
        print("2. Modify car details")
        print("3. Display all records")
        print("4. Search Specific record of")
        print("5. Return a Rented Car. ")
        print("6. Exit Administration Mode ")
        print("-"*50)
        # userInput Option
        userDecision = int(input("Please enter your option: "))
        if userDecision == 1:
            print("-"*106)
            print("Welcome to Car Rental Management System (Administrator/Add Cars)\n".center(100))
            addCars()
            continue
        elif userDecision == 2:
            print("-"*106)
            print("Welcome to Car Rental Management System (Administrator/Modify Cars)\n".center(100))
            modifyCarDetails()
            continue
        elif userDecision == 3:
            print("-"*106)
            print("Welcome to Car Rental Management System (Administrator/Display Cars Record)\n".center(100))
            print("1.Cars Rented Out")
            print("2.Cars available for Rent")
            print("3.Customer Bookings and Payments Details")
            print("4.Exit to Admin")
            userDecision = int(input("Please enter your option: "))
            if userDecision == 1:
                carRentOut()
                continue
            elif userDecision == 2:
                carNotRentOut()
                continue
            elif userDecision == 3:
                cusBookAndPay()
                continue 
            elif userDecision == 4:
                continue
            else:
                print("Please select option again")
        elif userDecision == 4:
            print("-"*106)
            print("Welcome to Car Rental Management System (Administrator/Search Cars)\n".center(100))
            print("1.Customer Booking")
            print("2.Customer Payment")
            print("3.Exit to Admin")
            print("-"*106)
            userDecision = int(input("Please enter your option: "))
            if userDecision == 1:
                searchCusBook()
                continue
            elif userDecision == 2:
                searchCusPay()
                continue
            elif userDecision == 3:
                continue
            else:
                print("Please select option again")
        elif userDecision == 5:
            print("-"*106)
            print("Welcome to Car Rental Management System (Administrator/Return Rented Car)\n".center(100))
            print("-"*106)
            returnRentedCar()
            continue
    
        elif userDecision == 6:
            return main() 

# Main Function
def main():
    #default username and password
    defaultUsername = "admin"
    defaultPassword = "admin"
    checkLogin = True
    # Loop through function   
    while checkLogin :
        try:
            print("-"*106)
            print ("\033[1;34;40m Welcome to Car Rental Management System\n".center(100))
            print("   _____             _____            _        _    _____           _            ")
            print("  / ____|           |  __ \          | |      | |  / ____|         | |                ")
            print(" | |     __ _ _ __  | |__) |___ _ __ | |_ __ _| | | (___  _   _ ___| |_ ___ _ __ ___  ")
            print(" | |    / _` | '__| |  _  // _ \ '_ \| __/ _` | |  \___ \| | | / __| __/ _ \ '_ ` _ \ ")
            print(" | |___| (_| | |    | | \ \  __/ | | | || (_| | |  ____) | |_| \__ \ ||  __/ | | | | |")
            print("  \_____\__,_|_|    |_|  \_\___|_| |_|\__\__,_|_| |_____/ \__, |___/\__\___|_| |_| |_|")
            print("                                                           __/ |              ")
            print("                                                          |___/                       ")
 
            print("Please select an option: ")
            print( "1. Registered Customer ")
            print( "2. Unregistered Customer ")
            print( "3. Admin")
            print( "4. Guest")
            print( "5. Account Recovery")
            print( "6. Support Us "+"\u2764\ufe0f")
            print( "7. Exit")
            # userInput Option
            userDecision = int(input("Please enter your option: "))
            if userDecision == 1:
                print("-"*106)
                print("Welcome to Car Rental Management System (Registered Customer/User Login)\n".center(100))
                print("-"*106)
                userLogin()
                checkLogin = False
 
            elif userDecision == 2: 
                print("-"*106)
                print("Welcome to Car Rental Management System (Unregistered Customer/User Registration)\n".center(100))
                print("-"*106)
                print("Please fill the form below:")
                userRegister()
 
 
            elif userDecision == 3:
                print("-"*106)
                print("Welcome to Car Rental Management System (Administrator)\n".center(100))
                # userInput username and password
                username = str(input("Please enter Username: "))
                password = input("Please enter Password: ")
                # Check if username and password are same with defaultUsername and defaultPassword
                if username == defaultUsername and password == defaultPassword:
                    print("Loging into Admin ........")
                    print("Login Successfully! You are now login as Administrator Mode ! ")
                    adminMenu()
                else: 
                    print("Invalid Username and Password")
                    continue
 
            elif userDecision == 4:
                print("-"*106)
                print("Welcome to Car Rental Management System (Guest Mode)\n".center(100))
                print("-"*106)
                print("1. View all cars available for rent. ")
                print("2. New customer Register to Access other Details")
                print("3. Exit Guest Mode")
                print("-"*106)
                # userInput option
                userDecision = int(input("Please enter your option: "))
                if userDecision == 1:
                    carNotRentOut()
                elif userDecision == 2:
                    userRegister()  
                elif userDecision == 3:
                    continue
            elif userDecision == 5:
                accountRecovery()
                continue
            elif userDecision == 6:
                license()
            elif userDecision == 7:
                print("-"*106) 
                print("Thank you for using our services!")
                print("Exiting...")
                print("-"*106)
                exit()
        # Check if value error
        except ValueError:
            print("Please only select the option above, retrying ...")
 
 
main()
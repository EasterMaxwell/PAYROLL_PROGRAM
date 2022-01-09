
# To import the date module
import datetime
# To import the time module
import time
# To import the random module
import random

more_details = ('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMORE INFORMATION'
                '\nKnown as : Apex Technologies'
                'Popular Products : Apex Banking Software'
                'Created : 1992'
                'Annual Revenue : $5 billion (including appreciating assets)'
                'Market Base : Finance Software & Technology')

company_faq = ('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCOMPANY INFORMATION'
              '\nApex Technology is a company with the major goal or mission of bringing high - standard' 
              'Tech to homes around the world, irrespective of the standard or literacy of the users.' 
              'Our Mantra has always been the same ; "Make tech software and easily available". And ' 
              'so far, we have been able to complete half our mission. Our Employees are the backbone ' 
              'of our production and execution. without them, our mission would simply turn into a night' 
              'mare. Our employees work hard every single second to stay at the top of the Tech market and' 
              'the Software industry. Currently we have ', random.randint(40000, 50000), 'Employees across'
              'the world and we would be glad if you would volunteer to contribute to our teams effort!')

# Employee options
option_1 = 'A. CREATE EMPLOYEE ACCOUNT'
option_2 = 'B. COLLECT PAY'
option_3 = 'C. PAY FOR INSURANCE'
option_4 = 'D. FIX/CHANGE WORK RATE'
option_5 = 'E. CHANGE CURRENT DEPARTMENT'

# Employer options
option_6 = 'A. COLLECT DEPARTMENT INFORMATION'
option_7 = 'B. REVENUE ACCOUNTING'
option_8 = 'C. PAY EXPENSES'
option_9 = 'D. CHECK TAX RATE'
option_0 = 'E. COMPANY FAQ'

# Departments within the organization
department_1 = '1. Sales Department'
department_2 = '2. Advertisement Department'
department_3 = '3. Marketing Department'
department_4 = '4. Manufacturing Department'
department_5 = '5. Resources Department'
department_6 = '6. Transportation Department'
department_7 = '7. Managing Department'

time.sleep(2)
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\tWELCOME TO MY PAYROLL PROJECT!')

# General Employee pin
employee_pin = 237659
# General Employer pin
employer_pin = 872334

# Random net worth of our employee
employee_net_worth = 100000

company_balance = 1000000000

# A variable to check if any input statement is empty
null = ''

time.sleep(2)
print('Employee pin : ', employee_pin)
time.sleep(2)
print('Employer pin : ', employer_pin)

# Prompting the user to enter employee mode, if he/she is an employee
# Prompting the user to also enter employer mode, if he/she is an employer
time.sleep(2)
user_mode = input('\nPress x to activate employee mode : '
                  '\nPress o to activate employer mode : '
                  '\nEnter Option : ')

# To check if the input field is x
if user_mode == 'x':
    time.sleep(1)
    print('\nActivating Employee Mode...')
    time.sleep(3)
    print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEMPLOYEE MODE')

    time.sleep(2)
    print(option_1)
    time.sleep(1)
    print(option_2)
    time.sleep(1)
    print(option_3)
    time.sleep(1)
    print(option_4)
    time.sleep(1)
    print(option_5)
    time.sleep(2)

    # employee input option
    employee_option_input = input('\nEnter Option : ')
    # To create employee account
    if employee_option_input == 'A':
        time.sleep(2)
        name_input = input('\nEnter Your name : ')
        time.sleep(1)
        age_input = int(input('Enter Your age : '))
        time.sleep(1)
        # if the age_input is not up to 18, print an error
        while age_input < 18:
            time.sleep(2)
            print('detecting error...')
            time.sleep(3)
            print('Error message : You are too Young To Work in this company!')
            exit()
        # if the age input is greater than 70, print an error
        while age_input > 70:
            time.sleep(2)
            print('detecting error...')
            time.sleep(3)
            print('You are too Old to Work for this company!')
            exit()

        occupation_input = input('Enter Occupation : ')
        time.sleep(1)
        department_input = input('Enter department of service : ')
        time.sleep(1)
        birth_input = input('Enter date of birth : ')

        # After each input field above is filled, create the employee account
        time.sleep(2)
        print('\nCreating account...')
        time.sleep(6)
        print('Account Creation successful!')
        time.sleep(2)
        print('Account details stored successfully!')

        time.sleep(2)
        # To validate his/her account, the employee must enter the general employee pin
        # as referenced at the start of the program.
        validation_input = int(input('\nEnter Employee Pin to Validate Your Account : '))
        time.sleep(2)

        # to check if the validation_input correlates with the employee pin
        if validation_input == employee_pin:
            time.sleep(2)
            print('\nValidating account...')
            time.sleep(5)
            print('Validation successful!')
            time.sleep(2)
            print('Process completed!')
            time.sleep(2)
            print('\nPreparing Account Details...')
            time.sleep(5)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tACCOUNT DETAILS')
            time.sleep(2)
            print('Employee Name : ', name_input)
            time.sleep(1)
            print('Employee Age : ', age_input)
            time.sleep(1)
            print('Employee Occupation : ', occupation_input)
            time.sleep(1)
            print('Employee Department : ', department_input)
            time.sleep(1)
            print('Employee date of Birth : ', birth_input)
            time.sleep(1)
            print('Date of creation : ', datetime.datetime.now())

            # exit input, to exit program after account has been created
            exit_input = input('\nPress x to exit : ')

            if exit_input == 'x':
                time.sleep(2)
                print('\nexiting program...')
                time.sleep(3)
                print('Program terminated!')
                exit()
            elif exit_input == null:
                time.sleep(2)
                print('Input bar empty!')
                time.sleep(1)
                print('\nexiting by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()
            else:
                time.sleep(2)
                print('\nInvalid input!')
                time.sleep(1)
                print('exiting program...')
                time.sleep(3)
                print('Program terminated!')

        # Check if validation pin is incorrect
        while validation_input != employee_pin:
            time.sleep(2)
            print('\nValidating account...')
            time.sleep(5)
            print('Sorry, the pin is incorrect')
            time.sleep(2)
            print('Your account has been deleted!')
            exit()

        # if validation input field is empty
        while validation_input == null:
            time.sleep(2)
            print('\nError Message : Input bar empty!')
            time.sleep(2)
            print('Notice : Your account will be deleted')
            time.sleep(2)
            print('Tip : restart program and enter the "employee pin" ')
            exit()

    # Employee pay session
    elif employee_option_input == 'B':
        time.sleep(2)
        print('\t\t\t\t\t\t\t\t\t\t\t\t\tDEPARTMENTS')
        time.sleep(1)

        print(department_1)
        time.sleep(1)
        print(department_2)
        time.sleep(1)
        print(department_3)
        time.sleep(1)
        print(department_4)
        time.sleep(1)
        print(department_5)
        time.sleep(1)
        print(department_6)
        time.sleep(1)
        print(department_7)

        # Input field to enter the employee personal information
        time.sleep(2)
        pay_name_input = input('\nEnter Your Name : ')
        time.sleep(1)
        pay_depart_input = input('Enter Your Department of service : ')
        time.sleep(1)
        pay_occ_input = input('Enter Your Occupation : ')
        time.sleep(1)
        pay_hr_input = int(input('Enter Your Work (Hours) : '))
        time.sleep(1)
        pay_bank_input = input('Enter Your Bank : ')
        time.sleep(2)

        # After each field above is entered, calculate the pay
        print('\nCalculating pay...')
        time.sleep(5)
        print('Transacting amount...')
        time.sleep(3)
        print('Transaction successful!')
        time.sleep(1)

        # To check if the pay department input is from the sales department
        while pay_depart_input == 'Sales Department':
            time.sleep(2)
            print('\nYour Account has been credited with $', pay_hr_input * 30 * 15)
            time.sleep(2)
            print('\nPreparing transaction details...')
            time.sleep(5)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tTRANSACTION DETAILS')
            time.sleep(1)
            print('Employee Name : ', pay_name_input)
            time.sleep(1)
            print('Employee department of service : ', pay_depart_input)
            time.sleep(1)
            print('Employee Occupation : ', pay_occ_input)
            time.sleep(1)
            print('Employee Work rate : ', pay_hr_input)
            time.sleep(1)
            print('Employee Bank Id : ', pay_bank_input)
            time.sleep(1)
            print('Transaction id : ', random.randint(1, 10000000))
            exit()

        # if the department input is from the Advertisement department
        while pay_depart_input == 'Advertisement Department':
            time.sleep(2)
            print('\nYour Account has been credited with $', pay_hr_input * 30 * 13)
            time.sleep(2)
            print('\nPreparing transaction details...')
            time.sleep(5)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tTRANSACTION DETAILS')
            time.sleep(1)
            print('Employee Name : ', pay_name_input)
            time.sleep(1)
            print('Employee department of service : ', pay_depart_input)
            time.sleep(1)
            print('Employee Occupation : ', pay_occ_input)
            time.sleep(1)
            print('Employee Work rate : ', pay_hr_input)
            time.sleep(1)
            print('Employee Bank Id : ', pay_bank_input)
            time.sleep(1)
            print('Transaction id : ', random.randint(1, 10000000))
            exit()

        # if the department input is from the Marketing department
        while pay_depart_input == 'Marketing Department':
            time.sleep(2)
            print('\nYour Account has been credited with $', pay_hr_input * 30 * 20)
            time.sleep(2)
            print('\nPreparing transaction details...')
            time.sleep(5)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tTRANSACTION DETAILS')
            time.sleep(1)
            print('Employee Name : ', pay_name_input)
            time.sleep(1)
            print('Employee department of service : ', pay_depart_input)
            time.sleep(1)
            print('Employee Occupation : ', pay_occ_input)
            time.sleep(1)
            print('Employee Work rate : ', pay_hr_input)
            time.sleep(1)
            print('Employee Bank Id : ', pay_bank_input)
            time.sleep(1)
            print('Transaction id : ', random.randint(1, 10000000))
            exit()

        # if the department input is from the Manufacturing department
        while pay_depart_input == 'Manufacturing Department':
            time.sleep(2)
            print('\nYour Account has been credited with $', pay_hr_input * 30 * 22)
            time.sleep(2)
            print('\nPreparing transaction details...')
            time.sleep(5)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tTRANSACTION DETAILS')
            time.sleep(1)
            print('Employee Name : ', pay_name_input)
            time.sleep(1)
            print('Employee department of service : ', pay_depart_input)
            time.sleep(1)
            print('Employee Occupation : ', pay_occ_input)
            time.sleep(1)
            print('Employee Work rate : ', pay_hr_input)
            time.sleep(1)
            print('Employee Bank Id : ', pay_bank_input)
            time.sleep(1)
            print('Transaction id : ', random.randint(1, 10000000))
            exit()

            # if the department input is from the resources department

        while pay_depart_input == 'Resources Department':
            time.sleep(2)
            print('\nYour Account has been credited with $', pay_hr_input * 30 * 25)
            time.sleep(2)
            print('\nPreparing transaction details...')
            time.sleep(5)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tTRANSACTION DETAILS')
            time.sleep(1)
            print('Employee Name : ', pay_name_input)
            time.sleep(1)
            print('Employee department of service : ', pay_depart_input)
            time.sleep(1)
            print('Employee Occupation : ', pay_occ_input)
            time.sleep(1)
            print('Employee Work rate : ', pay_hr_input)
            time.sleep(1)
            print('Employee Bank Id : ', pay_bank_input)
            time.sleep(1)
            print('Transaction id : ', random.randint(1, 10000000))
            exit()

        # if the department input if from the Transportation department
        while pay_depart_input == 'Transportation Department':
            time.sleep(2)
            print('\nYour Account has been credited with $', pay_hr_input * 30 * 10)
            time.sleep(2)
            print('\nPreparing transaction details...')
            time.sleep(5)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tTRANSACTION DETAILS')
            time.sleep(1)
            print('Employee Name : ', pay_name_input)
            time.sleep(1)
            print('Employee department of service : ', pay_depart_input)
            time.sleep(1)
            print('Employee Occupation : ', pay_occ_input)
            time.sleep(1)
            print('Employee Work rate : ', pay_hr_input)
            time.sleep(1)
            print('Employee Bank Id : ', pay_bank_input)
            time.sleep(1)
            print('Transaction id : ', random.randint(1, 10000000))
            exit()

            # if the department input is from the Managing Department

        while pay_depart_input == 'Managing Department':
            time.sleep(2)
            print('\nYour Account has been credited with $', pay_hr_input * 30 * 35)
            time.sleep(2)
            print('\nPreparing transaction details...')
            time.sleep(5)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tTRANSACTION DETAILS')
            time.sleep(1)
            print('Employee Name : ', pay_name_input)
            time.sleep(1)
            print('Employee department of service : ', pay_depart_input)
            time.sleep(1)
            print('Employee Occupation : ', pay_occ_input)
            time.sleep(1)
            print('Employee Work rate : ', pay_hr_input)
            time.sleep(1)
            print('Employee Bank Id : ', pay_bank_input)
            time.sleep(1)
            print('Transaction id : ', random.randint(1, 10000000), 'xb - ref')
            exit()

    elif employee_option_input == 'C':
        time.sleep(2)
        print('Note : This is a very important part of the workforce of our company, We appreciate You!')
        time.sleep(2)
        i_name_input = input('\nEnter Your Name : ')
        time.sleep(1)
        i_period_input = input('Enter Your Insurance period : ')
        time.sleep(1)
        i_pin_input = int(input('Enter Your bank pin : '))
        time.sleep(1)
        i_choice_input = input('Premium or Normal : ')
        time.sleep(2)

        if i_choice_input == 'Premium':
            time.sleep(2)
            print('\nBooking insurance...')
            time.sleep(5)
            print('Insurance booking successful!')
            time.sleep(2)
            print('\nYour Total fee is : ', 15000 * 2)
            time.sleep(2)

            premium_payment = input('\nPress 0 to pay : ')

            if premium_payment == '0':
                time.sleep(2)
                print('\nTransacting Amount')
                time.sleep(5)
                print('Amount Transferred successfully!')
                time.sleep(2)
                print('\nPreparing Insurance Booking details...')
                time.sleep(3)
                print('\nName : ', i_name_input)
                time.sleep(1)
                print('Insurance Period : ', i_period_input)
                time.sleep(1)
                print('Bank Pin : ', i_pin_input)
                time.sleep(1)
                print('Insurance Type : ', i_choice_input)
                time.sleep(1)
                print('Transaction id : ', random.randint(1, 90000000), 'xb - ref')
                time.sleep(2)
                print('\nAccount Balance : ', employee_net_worth - 15000 * 2)
                exit()

            elif premium_payment == null:
                time.sleep(2)
                print('\nError Message : input bar empty!')
                time.sleep(2)
                print('Payment Process Denied!')
                time.sleep(1)
                print('exiting...')
                time.sleep(3)
                print('Program terminated')
                exit()

            else:
                time.sleep(2)
                print('\nInvalid Input!')
                time.sleep(1)
                print('terminating program...')
                time.sleep(3)
                print('Program terminated by default.')

        elif i_choice_input == 'Normal':
            time.sleep(2)
            print('\nBooking Insurance...')
            time.sleep(5)
            print('Insurance booking successful!')
            time.sleep(2)
            print('\nYour Total fee is : ', 5000 * 2)
            time.sleep(2)

            normal_payment = input('\nPress 0 to pay : ')

            if normal_payment == '0':
                time.sleep(2)
                print('\nTransacting Amount')
                time.sleep(5)
                print('Amount Transferred successfully!')
                time.sleep(2)
                print('\nPreparing Insurance Booking details...')
                time.sleep(3)
                print('\nName : ', i_name_input)
                time.sleep(1)
                print('Insurance Period : ', i_period_input)
                time.sleep(1)
                print('Bank Pin : ', i_pin_input)
                time.sleep(1)
                print('Insurance Type : ', i_choice_input)
                time.sleep(1)
                print('Transaction id : ', random.randint(1, 90000000), 'xb - ref')
                time.sleep(2)
                print('\n\033[1;36mAccount Balance : ', employee_net_worth - 5000 * 2)
                exit()

            elif normal_payment == null:
                time.sleep(2)
                print('\nError Message : input bar empty!')
                time.sleep(2)
                print('Payment Process Denied!')
                time.sleep(1)
                print('exiting...')
                time.sleep(3)
                print('Program terminated')
                exit()

            else:
                time.sleep(2)
                print('\nInvalid Input!')
                time.sleep(1)
                print('exiting...')
                time.sleep(3)
                print('Program terminated by default.')
                exit()

    elif employee_option_input == 'D':
        time.sleep(1)
        w_rate_input = input('\nEnter current work rate : ')
        time.sleep(1)
        w_name_input = input('Enter Your Name : ')
        time.sleep(1)
        w_depart_input = input('Enter Your Department of Service : ')
        time.sleep(1)
        new_rate_input = input('Enter New Work Rate : ')

        time.sleep(2)
        print('\nProcessing...')
        time.sleep(5)
        print('Done!')
        time.sleep(2)
        print('\nYour work rate has been change from', w_rate_input, 'to', new_rate_input)

        if new_rate_input > w_rate_input:
            time.sleep(2)
            print('That is an increase in Work rate!, Your pay will also increase.')
            time.sleep(2)

            w_exit = input('\nPress x to exit')

            if w_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif w_exit != null:
                time.sleep(1)
                print('\ninput bar empty!')
                time.sleep(1)
                print('Program terminating by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            else:
                time.sleep(1)
                print('\ninvalid input!')
                time.sleep(1)
                print('exiting...')
                time.sleep(2)
                print('Program terminated!')
                exit()

        elif new_rate_input < w_rate_input:
            time.sleep(2)
            print('That is a decrease in Work rate!, Your pay will also decrease.')

            n_exit = input('\nPress x to exit')

            if n_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif n_exit != null:
                time.sleep(1)
                print('\ninput bar empty!')
                time.sleep(1)
                print('exiting...')
                time.sleep(3)
                print('Program terminating by default...')
                exit()

            else:
                time.sleep(1)
                print('\ninvalid input!')
                time.sleep(1)
                print('exiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

    elif employee_option_input == 'E':
        time.sleep(2)
        print('Seems you are getting promoted!')
        time.sleep(2)
        c_name_input = input('\nEnter Your Name : ')
        c_depart_input = input('Enter Your Previous department : ')
        current_depart = input('Enter Current Department : ')
        c_occ_input = input('Enter Your occupation : ')

        time.sleep(2)
        print('\nSwitching employee department...')
        time.sleep(5)
        print('Successful!')
        time.sleep(2)
        print('\nDear', c_name_input, 'You have been transferred from', c_depart_input, 'to', current_depart)

        c_exit = input('\nPress x to exit : ')

        if c_exit == 'x':
            print('\nexiting...')
            time.sleep(3)
            print('Program terminated!')
            exit()

        elif c_exit == null:
            print('\nInput bar empty!')
            time.sleep(1)
            print('Program exiting by default...')
            time.sleep(3)
            print('Program terminated!')
            exit()

        else:
            print('\nInvalid input!')
            time.sleep(1)
            print('exiting...')
            time.sleep(3)
            print('done')
            exit()

    elif employee_option_input == null:
        time.sleep(1)
        print('\nInput bar empty!')
        time.sleep(1)
        print('restart program!')
        time.sleep(1)
        print('exiting...')
        time.sleep(3)
        print('done!')
        exit()

    else:
        time.sleep(1)
        print('\nInvalid input!')
        time.sleep(1)
        print('exiting...')
        time.sleep(3)
        print('Program terminated!')
        exit()

if user_mode == 'o':
    time.sleep(1)
    print('\nActivating Employer Mode...')
    time.sleep(3)
    print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tEMPLOYER MODE')

    time.sleep(1)
    print(option_6)
    time.sleep(1)
    print(option_7)
    time.sleep(1)
    print(option_8)
    time.sleep(1)
    print(option_9)
    time.sleep(2)

    employer_input = input('\nEnter option : ')
    # Collect department information
    if employer_input == 'A':
        time.sleep(1)
        emp_depart_input = input('\nEnter Department : ')

        if emp_depart_input == 'Sales Department':
            time.sleep(2)
            print('\nPreparing information...')
            time.sleep(6)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tSales Department Information')
            time.sleep(1)
            print('Number of Employees : ', random.randint(500, 2000))
            time.sleep(1)
            print('Revenue per Year : ', random.randint(100000, 500000), 'dollars')
            time.sleep(1)
            print('Revenue per Month : ', random.randint(30000, 50000), 'dollars')
            time.sleep(1)
            print('Expenses per Year : ', random.randint(4000, 5000), 'dollars')
            time.sleep(1)
            print('Expenses per Month : ', random.randint(400, 1000), 'dollars')
            time.sleep(1)
            print('Performance Rate : ', random.randint(50, 100), '%')
            time.sleep(2)

            s_exit = input('\nPress x to exit : ')

            if s_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif s_exit == null:
                time.sleep(1)
                print('Input bar empty')
                time.sleep(1)
                print('exiting by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            else:
                time.sleep(1)
                print('Invalid input')
                time.sleep(2)
                print('Program terminating by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

        elif emp_depart_input == 'Advertisement Department':
            time.sleep(2)
            print('\nPreparing information...')
            time.sleep(6)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tAdvertisement Department Information')
            time.sleep(1)
            print('Number of Employees : ', random.randint(100, 500))
            time.sleep(1)
            print('Revenue per Year : ', random.randint(50000, 100000), 'dollars')
            time.sleep(1)
            print('Revenue per Month : ', random.randint(20000, 40000), 'dollars')
            time.sleep(1)
            print('Expenses per Year : ', random.randint(1000, 10000), 'dollars')
            time.sleep(1)
            print('Expenses per Month : ', random.randint(1000, 5000), 'dollars')
            time.sleep(1)
            print('Performance Rate : ', random.randint(1, 80), '%')
            time.sleep(2)

            a_exit = input('\nPress x to exit : ')

            if a_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif a_exit == null:
                time.sleep(1)
                print('Input bar empty')
                time.sleep(1)
                print('exiting by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

        elif emp_depart_input == 'Marketing Department':
            time.sleep(2)
            print('\nPreparing information...')
            time.sleep(6)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tMarketing Department Information')
            time.sleep(1)
            print('Number of Employees : ', random.randint(1, 2000))
            time.sleep(1)
            print('Revenue per Year : ', random.randint(500000, 3000000), 'dollars')
            time.sleep(1)
            print('Revenue per Month : ', random.randint(30000, 55000), 'dollars')
            time.sleep(1)
            print('Expenses per Year : ', random.randint(10000, 20000), 'dollars')
            time.sleep(1)
            print('Expenses per Month : ', random.randint(9000, 15000), 'dollars')
            time.sleep(1)
            print('Performance Rate : ', random.randint(1, 100), '%')
            time.sleep(2)

            m_exit = input('\nPress x to exit : ')

            if m_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif m_exit == null:
                time.sleep(1)
                print('Input bar empty')
                time.sleep(1)
                print('exiting by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            else:
                time.sleep(1)
                print('Invalid input')
                time.sleep(2)
                print('Program terminating by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

        elif emp_depart_input == 'Manufacturing Department':
            time.sleep(2)
            print('\nPreparing information...')
            time.sleep(6)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tManufacturing Department Information')
            time.sleep(1)
            print('Number of Employees : ', random.randint(1500, 2000))
            time.sleep(1)
            print('Revenue per Year : ', random.randint(50000, 300000), 'dollars')
            time.sleep(1)
            print('Revenue per Month : ', random.randint(3000, 55000), 'dollars')
            time.sleep(1)
            print('Expenses per Year : ', random.randint(5000, 15000), 'dollars')
            time.sleep(1)
            print('Expenses per Month : ', random.randint(1000, 5000), 'dollars')
            time.sleep(1)
            print('Performance Rate : ', random.randint(1, 90), '%')
            time.sleep(2)

            md_exit = input('\nPress x to exit : ')

            if md_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif md_exit == null:
                time.sleep(1)
                print('Input bar empty')
                time.sleep(1)
                print('exiting by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            else:
                time.sleep(1)
                print('Invalid input')
                time.sleep(2)
                print('Program terminating by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()


        elif emp_depart_input == 'Resources Department':
            time.sleep(2)
            print('\nPreparing information...')
            time.sleep(6)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tResources Department Information')
            time.sleep(1)
            print('Number of Employees : ', random.randint(500, 1000))
            time.sleep(1)
            print('Revenue per Year : ', random.randint(200000, 250000), 'dollars')
            time.sleep(1)
            print('Revenue per Month : ', random.randint(30000, 40000), 'dollars')
            time.sleep(1)
            print('Expenses per Year : ', random.randint(15000, 15000), 'dollars')
            time.sleep(1)
            print('Expenses per Month : ', random.randint(5000, 10000), 'dollars')
            time.sleep(1)
            print('Performance Rate : ', random.randint(1, 88), '%')
            time.sleep(2)

            r_exit = input('\nPress x to exit : ')

            if r_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif r_exit == null:
                time.sleep(1)
                print('Input bar empty')
                time.sleep(1)
                print('exiting by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            else:
                time.sleep(1)
                print('Invalid input')
                time.sleep(2)
                print('Program terminating by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()


        elif emp_depart_input == 'Transportation Department':
            time.sleep(2)
            print('\nPreparing information...')
            time.sleep(6)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\033\nTransportation Department Information')
            time.sleep(1)
            print('Number of Employees : ', random.randint(1500, 2000))
            time.sleep(1)
            print('Revenue per Year : ', random.randint(55000, 70000), 'dollars')
            time.sleep(1)
            print('Revenue per Month : ', random.randint(300, 5000), 'dollars')
            time.sleep(1)
            print('Expenses per Year : ', random.randint(1000, 5000), 'dollars')
            time.sleep(1)
            print('Expenses per Month : ', random.randint(500, 2000), 'dollars')
            time.sleep(1)
            print('Performance Rate : ', random.randint(1, 85), '%')
            time.sleep(2)

            t_exit = input('\nPress x to exit : ')

            if t_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif t_exit == null:
                time.sleep(1)
                print('Input bar empty')
                time.sleep(1)
                print('exiting by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            else:
                time.sleep(1)
                print('Invalid input')
                time.sleep(2)
                print('Program terminating by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()


        elif emp_depart_input == 'Managing Department':
            time.sleep(2)
            print('\nPreparing information...')
            time.sleep(6)
            print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tManaging Department Information')
            time.sleep(1)
            print('Number of Employees : ', random.randint(1, 2000))
            time.sleep(1)
            print('Revenue per Year : ', random.randint(2000000, 5000000), 'dollars')
            time.sleep(1)
            print('Revenue per Month : ', random.randint(150000, 200000), 'dollars')
            time.sleep(1)
            print('Expenses per Year : ', random.randint(40000, 100000), 'dollars')
            time.sleep(1)
            print('Expenses per Month : ', random.randint(9000, 40000), 'dollars')
            time.sleep(1)
            print('Performance Rate : ', random.randint(1, 100), '%')
            time.sleep(2)

            man_exit = input('\nPress x to exit : ')

            if man_exit == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif man_exit == null:
                time.sleep(1)
                print('\nInput bar empty')
                time.sleep(1)
                print('exiting by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            else:
                time.sleep(1)
                print('\nInvalid input')
                time.sleep(2)
                print('Program terminating by default...')
                time.sleep(3)
                print('Program terminated!')
                exit()

        elif emp_depart_input == null:
            time.sleep(1)
            print('\nInput bar empty')
            time.sleep(1)
            print('exiting by default...')
            time.sleep(3)
            print('Program terminated!')
            exit()

        else:
            time.sleep(1)
            print('\nInvalid input')
            time.sleep(2)
            print('Program terminating by default...')
            time.sleep(3)
            print('Program terminated!')
            exit()

    elif employer_input == 'B':
        time.sleep(1)
        print('Note : You can only calculate the annual revenue.')
        time.sleep(1)
        print('\nPreparing revenue of each department...')
        time.sleep(5)
        sd_revenue = random.randint(150000, 500000)
        ad_revenue = random.randint(100000, 250000)
        mrk_revenue = random.randint(500000, 3000000)
        md_revenue = random.randint(70000, 100000)
        td_revenue = random.randint(50000, 70000)
        rd_revenue = random.randint(100000, 200000)
        man_revenue = random.randint(2000000, 5000000)

        print('\n\t\t\t\t\t\t\t\t\t\t\t\t\tRevenue Of Each Department')
        time.sleep(2)
        print('Sales Department Revenue : ', sd_revenue, 'dollars')
        time.sleep(1)
        print('Advertisement Department Revenue : ', ad_revenue, 'dollars')
        time.sleep(1)
        print('Marketing Department Revenue : ', mrk_revenue, 'dollars')
        time.sleep(1)
        print('Manufacturing Department Revenue : ', md_revenue, 'dollars')
        time.sleep(1)
        print('Transportation Department Revenue : ', td_revenue, 'dollars')
        time.sleep(1)
        print('Resources Department Revenue : ', rd_revenue, 'dollars')
        time.sleep(1)
        print('Managing Department Revenue : ', man_revenue, 'dollars')

        time.sleep(2)
        addition_input = input('\nPress 0 to add all revenue : ')

        if addition_input == 'x':
            time.sleep(1)
            print('\nProcessing...')
            time.sleep(5)
            print('Done!')
            time.sleep(1)
            print('\nTotal Annual Revenue : ', sd_revenue + ad_revenue + mrk_revenue +
                  md_revenue + td_revenue + rd_revenue + man_revenue, 'dollars')
            time.sleep(2)
            print("\nCompany's Current Balance : ", company_balance + sd_revenue + ad_revenue + mrk_revenue
                  + td_revenue + md_revenue + rd_revenue + man_revenue)


            time.sleep(2)
            add_exit_input = input('\nPress x to exit : ')

            if add_exit_input == 'x':
                time.sleep(1)
                print('\nexiting...')
                time.sleep(3)
                print('Program terminated!')
                exit()

            elif add_exit_input == null:
                time.sleep(1)
                print('\nInput bar empty!')
                time.sleep(1)
                print('Program terminating by default...')
                time.sleep(3)
                print('program terminated!')

            else:
                time.sleep(1)
                print('\nInvalid input!')
                time.sleep(1)
                print('exiting program...')
                time.sleep(3)
                print('program terminated!')
                exit()

        elif addition_input == null:
            time.sleep(1)
            print('\nError Message : input bar empty!')
            time.sleep(1)
            print('restart program to add up revenue')
            time.sleep(1)
            print('exiting...')
            time.sleep(3)
            exit()

        else:
            time.sleep(1)
            print('\nInvalid input!')
            time.sleep(1)
            print('You have to restart program to add revenue!')
            time.sleep(1)
            print('exiting...')
            time.sleep(3)
            exit()

    elif employer_input == 'C':
        time.sleep(1)
        print('Note : You can only calculate Annual Expenses.')
        time.sleep(1)
        print('\nCalculating Total Annual Expenses...')
        time.sleep(5)
        print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;4mExpenses Of Each Department')
        time.sleep(1)
        sd_expense = random.randint(1500, 15000)
        ad_expense = random.randint(1000, 17000)
        mrk_expense = random.randint(5000, 10000)
        md_expense = random.randint(7000, 20000)
        td_expense = random.randint(50000, 70000)
        rd_expense = random.randint(10000, 20000)
        man_expense = random.randint(20000, 50000)

        print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;4mRevenue Of Each Department')
        time.sleep(2)
        print('Sales Department Expenses : ', sd_expense, 'dollars')
        time.sleep(1)
        print('Advertisement Department Expenses : ', ad_expense, 'dollars')
        time.sleep(1)
        print('Marketing Department Expenses : ', mrk_expense, 'dollars')
        time.sleep(1)
        print('Manufacturing Department Expenses : ', md_expense, 'dollars')
        time.sleep(1)
        print('Transportation Department Expenses : ', td_expense, 'dollars')
        time.sleep(1)
        print('Resources Department Expenses : ', rd_expense, 'dollars')
        time.sleep(1)
        print('Managing Department Expenses : ', man_expense, 'dollars')

        time.sleep(2)
        print('\nTotal Expenses : ', sd_expense + ad_expense + mrk_expense + td_expense
              + md_expense + rd_expense + man_expense)
        time.sleep(2)
        print("\nCompany's Current Balance : ", company_balance - sd_expense + ad_expense + mrk_expense
              + td_expense + md_expense + rd_expense + man_expense)

    elif employer_input == 'D':
        time.sleep(1)
        print('Checking tax rate...')
        time.sleep(5)
        print('Process completed!')
        time.sleep(2)

        tax_rate = company_balance - random.randint(1000000, 2000000)

        print('\nTax rate : ', tax_rate, 'dollars')

        pay_input = input('\nEnter 0 to pay tax : ')

        if pay_input == '0':
            time.sleep(1)
            print('\nProcessing payment...')
            time.sleep(4)
            print('Payment completed!')
            time.sleep(1)
            print('\nCurrent Account Balance : ', company_balance - tax_rate, 'dollars')
            time.sleep(1)
            print('Transaction id : ', random.randint(1, 2000000), 'xnb - ref')

        elif pay_input == null:
            time.sleep(1)
            print('\nError : input bar empty!')
            time.sleep(1)
            print('terminating program by default...')
            time.sleep(3)
            print('program terminated!')
            exit()

        else:
            time.sleep(1)
            print('\nError : Invalid input')
            time.sleep(1)
            print('exiting')
            time.sleep(3)
            print('program terminated!')
            exit()

    elif employer_input == 'E':
        time.sleep(1)
        print('\nProcessing requesting...')
        time.sleep(5)
        print('Done!')
        time.sleep(2)
        print('\n', company_faq)
        time.sleep(3)
        print('\n', more_details)
        exit()

    elif employer_input == 'E':
        time.sleep(1)
        faq_input = input('\nPress o to continue : ')

        if faq_input == 'o':
            time.sleep(2)
            print('\nFetching information...')
            time.sleep(5)
            print('successful!')

            print(company_faq)
            time.sleep(3)
            print(more_details)
            time.sleep(2)
            exit()

        elif faq_input == null:
            time.sleep(1)
            print('\nError message : Input bar empty!')
            time.sleep(1)
            print('exiting...')
            time.sleep(3)
            print('program terminated!')
            exit()

        else:
            time.sleep(1)
            print('\nInvalid input!')
            time.sleep(1)
            print('exiting...')
            time.sleep(3)
            print('program terminated!')
            exit()



    elif employer_input == null:
        time.sleep(2)
        print('\nInput bar empty!')
        time.sleep(1)
        print('exiting by default...')
        time.sleep(3)
        print('Program terminated!')
        exit()

    else:
        time.sleep(2)
        print('\nInvalid Input!')
        time.sleep(1)
        print('exiting...')
        time.sleep(3)
        print('Program terminated!')
        exit()

elif user_mode == null:
    time.sleep(2)
    print('\nError : input bar empty!')
    time.sleep(2)
    print('Restart program.')
    exit()







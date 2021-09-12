# Anh Do (Student ID #001511153)
from Classes import Format
import simulation
from readData import convert_time
import os


# USER INTERFACE--------------------------------------------------------------------------------------------------------
def program_start():
    """Start program user interface"""
    welcome = Format.BOLD + Format.YELLOW + ' WGUPS Routing Program ' + Format.END
    print(welcome.center(105, "*"))
    instruction = '''
    Select one of the following options:
       1. Package delivery status
       2. Total mileage traveled by all trucks
       3. Truck routes simulation
       4. Open screenshots
       5. Exit
    '''
    print(instruction)


print('Optimizing routes...')
simulation.run(False)  # Run simulation without printing
print('Optimization completed!')
program_start()
while True:
    option = int(input('>>> OPTION: '))

    if option == 1:  # Package delivery status
        option_txt = Format.UNDERLINE + 'PACKAGE DELIVERY STATUS' + Format.END
        print(option_txt)
        while True:
            try:
                time = input('- Enter time in "HH:MM" format: ')
                time = convert_time(time)
                break
            except ValueError:  # catch time format error
                print('ERROR: Invalid time format')
                continue

        pkg = int(input('''- Select package(s):
           0. All packages
        1-40. Specific package
    >>> PACKAGE SELECTION: '''))
        simulation.package_status(pkg, time)
        print(' END PROGRAM '.center(91, '='))
        print('Program restarts...')
        program_start()

    elif option == 2:  # Truck total mileage
        option_txt = Format.UNDERLINE + 'TRUCK TOTAL MILEAGE' + Format.END
        print(option_txt)
        simulation.truck_mileage()
        print(' END PROGRAM '.center(91, '='))
        print('Program restarts...')
        program_start()

    elif option == 3:  # Truck routes simulation
        option_txt = Format.UNDERLINE + 'TRUCK ROUTES SIMULATION' + Format.END
        print(option_txt)

        simulation.run(True)
        print(' END PROGRAM '.center(91, '='))
        print('Program restarts...')
        program_start()

    elif option == 4:  # Open screenshots
        print('Opening screenshots...')

        os.startfile('.\Screenshots\Package Status 0900.png')
        os.startfile('.\Screenshots\Package Status 1000.png')
        os.startfile('.\Screenshots\Package Status 1230.png')

        print(' END PROGRAM '.center(91, '='))
        print('Program restarts...')
        program_start()

    elif option == 5:  # Exit program
        print('\n\nClosing program...')
        exit()

    else:  # Invalid input
        print('Invalid input. Please select option 1-5.')








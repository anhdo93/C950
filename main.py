# Anh Do (Student ID #001511153)
from Classes import Format
import simulation

'''
    INTERFACE REQUIREMENTS:
    1. Status/Info of any package at any time
    2. Total mileage traveled by all trucks
    3. Status of all packages at a time between:
        a. 08:35 am  - 09:25 am
        b. 09:35 am  - 10:25 am
        c. 12:03 pm  - 01:12 pm
'''

# USER INTERFACE--------------------------------------------------------------------------------------------------------
welcome = Format.BOLD + Format.YELLOW + ' WGUPS Routing Program ' + Format.END
print(welcome.center(60, "-"))
option = int(input('''
Select one of the following options:
   1. Package delivery status
   2. Total mileage traveled by all trucks 
   3. Truck routes simulation
   4. Open screenshots 
 >>> OPTION: '''))

if option == 1:
    option_txt = Format.UNDERLINE + 'PACKAGE DELIVERY STATUS' + Format.END
    print(option_txt)
    time = input('- Enter time in "HH:MM" format: ')
    pkg = int(input('''- Select package(s):
       0. All packages
    1-40. Specific package
>>> PACKAGE SELECTION: '''))
    simulation.package_status(pkg)

elif option == 2:
    option_txt = Format.UNDERLINE + 'TRUCK TOTAL MILEAGE' + Format.END
    print(option_txt)
    simulation.run('23:59', False)
    simulation.truck_mileage()

elif option == 3:
    option_txt = Format.UNDERLINE + 'TRUCK ROUTES SIMULATION' + Format.END
    print(option_txt)
    simulation.run('23:59', True)

else:
    pass








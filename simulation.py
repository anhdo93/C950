from functions import *
import optimize
from datetime import timedelta
import sys, os


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


# PACKAGES DELIVERY-----------------------------------------------------------------------------------------------------
def run(time_string, printRoute):
    time = convert_time(time_string)
    if not printRoute:
        blockPrint()
    total_mileage = 0
    for t in truck:
        if t == 3:
            start_time[t] = min(start_time[1], start_time[2])  # Truck 3 starts when either truck 1 or 2 arrives at hub

        current_location = 0
        package_index = 0

        print('--------- TRUCK {} ----------'.format(t))
        print('Truck {} Route: '.format(t), end='')
        print(*route_for_truck[t], sep=' --> ')
        print('Truck {} Packages: {}'.format(t, packages_on_truck[t]))

        for destination in route_for_truck[t]:
            for pkg in packages_on_truck[t]:
                # Find package with wrong address to update
                found_error = False
                current_package = get_package(pkg)
                if (current_package.location_id == destination) and ('Wrong address' in get_package(pkg).notes):
                    error_package = current_package
                    if error_package.status != Status.DELIVERED:
                        found_error = True
                        if start_time[t] < update_time:  # wait until update time to correct address
                            start_time[t] = update_time
                        error_package.address = '410 S State St'
                        error_package.city = 'Salt Lake City'
                        error_package.state = 'UT'
                        error_package.zip = '84111'
                        error_package.notes = 'Fixed address'
                        error_package.location_id = locationHashTable.get(error_package.address).id
                # Deliver package to destination
                if (current_package.location_id == destination) or found_error:
                    current_package.status = Status.EN_ROUTE
                    next_location = get_package(pkg).location_id
                    delivery_time = start_time[t] + timedelta(hours=distance[current_location][next_location]/speed)
                    mileage[t] += distance[current_location][next_location]
                    if delivery_time > current_package.deadline:  # Check if package can arrive on time
                        current_package.status = Status.LATE
                    else:
                        current_package.status = Status.DELIVERED
                    if current_package.id != 0:
                        package_index += 1
                    else:
                        package_index = 0
                    print('{}-{:2} Package {:3}: {:>3} -> {:>3} [{:>4} miles ] Start: {}  Delivered: {} {:>19}  (Deadline {:>6})'
                          .format(t, package_index, current_package.id, current_location, next_location, distance[current_location][next_location],
                                  start_time[t].strftime('%H:%M'), delivery_time.strftime('%H:%M'),
                                  current_package.status, current_package.deadline.strftime('%H:%M')))
                    current_location = next_location
                    start_time[t] = delivery_time

        print('Truck {} traveled {:.1f} miles'.format(t, mileage[t]))
        total_mileage += mileage[t]

    print('TOTAL MILEAGE: {} miles'.format(total_mileage))
    enablePrint()


def truck_mileage():
    total_miles = 0
    for t in truck:
        print('Truck {} traveled {:.1f} miles'.format(t, mileage[t]))
        total_miles += mileage[t]
    print('TOTAL MILEAGE: {} miles'.format(total_miles))


def package_status(pkg):
    if pkg == 0:
        pass
    else:
        pass

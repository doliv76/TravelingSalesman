# C950 Performance Assessment
# Donald Oliver ID: 001259807

from data_transfer import load_address_data, load_distance_data, load_package_data
from chaining_hash_table import ChainingHashTable
from utility import deliver_packages, greedy_route, prep_route, calc_return_time,\
    lookup_package, lookup_time
from datetime import *

# time1, time2: truck1, truck2 hub departure times
time1 = time(8, 0, 0)
time2 = time(9, 5, 0)


# list to hold the routes for each truck prior to truck route computation
node_list = []
# package chaining hash table
pack_table = ChainingHashTable()
# address dictionary
addr_dict = {}
# distance table
distance_table = []

total_distance = 0.0

# truck routes
truck1_route = []
truck2_route = []
truck3_route = []

# Hard-Coded routes sorted in non-descending order
package_list1 = [5, 10, 11, 13, 14, 15, 16, 19, 20, 21, 22, 26, 29, 30, 34, 39]
package_list2 = [1, 3, 4, 6, 8, 12, 18, 25, 28, 31, 32, 35, 36, 37, 38, 40]
package_list3 = [2, 7, 9, 17, 23, 24, 27, 33]

# populate pack_table from csv
load_package_data('packages.csv', pack_table)
# populate addr_dict from csv with address strings as keys
load_address_data('addresses.csv', addr_dict)

# populate distance_table from csv
load_distance_data('distances.csv', distance_table)

addr_invert = dict(zip(addr_dict.values(), addr_dict.keys()))
# Start of CLI
print("          WGUPS DAILY LOCAL DELIVERIES SYSTEM: WDLDS")
switch = input("          (ENTER 'continue' TO RUN THE DAILY LOCAL DELIVERIES SIMULATION...)\n")

# flag to prevent the core algorithm from being run more than once for the data set
simulation_flag = 0


# CLI Control Loop; Exit program when 'exit' is entered by user
while switch != 'exit':
    # Home screen control loop
    while switch == 'home_screen' or switch == 'return':
        print("\n\n          WDLDS HOME SCREEN\n")
        print("          TOTAL DISTANCE TRAVELED LAST SIMULATION: %s\n" % str(total_distance))
        print("          TO LOOK UP A DELIVERED PACKAGE BY ID, ENTER 'package search'")
        print("          TO LOOK UP PACKAGE DELIVERY STATUSES AT A SPECIFIC TIME, ENTER 'time search'")
        print("          IF TOTAL DISTANCE TRAVELED IS 0, ENTER 'continue' TO RUN SIMULATION")
        print("          TO EXIT WDLDS, ENTER 'exit'")
        switch = input()
        break

    # Route Preparation, Package Delivery, Run Dynamic Core Algorithm
    while switch == 'continue':
        # Simulation flag is to prevent the reference errors that result from
        # Running the Core Algorithm more than once
        if simulation_flag != 1:
            # Run Greedy Algorithm to Build Route for Truck 1
            # Run Package Delivery for Truck 1
            print("Delivering truck 1: ")
            node_list = prep_route(package_list1, pack_table, addr_dict, node_list)
            truck1_distance = float(format(greedy_route(node_list, distance_table, truck1_route), '.2f'))
            truck1_time = calc_return_time(truck1_distance, time1)
            deliver_packages(time1, package_list1, pack_table, addr_invert, distance_table, truck1_route)
            print("Truck 1 Distance: %s" % str(truck1_distance))
            print("Truck 1 Time: %s" % str(truck1_time))

            # Run Greedy Algorithm to Build Route for Truck 2
            # Run Package Delivery for Truck 2
            print("\nDelivering truck 2: ")
            node_list = prep_route(package_list2, pack_table, addr_dict, node_list)
            truck2_distance = float(format(greedy_route(node_list, distance_table, truck2_route), '.2f'))
            truck2_time = calc_return_time(truck2_distance, time2)
            deliver_packages(time2, package_list2, pack_table, addr_invert, distance_table, truck2_route)
            print("Truck 2 Distance: %s" % str(truck2_distance))
            print("Truck 2 Time: %s" % str(truck2_time))

            # Run Greedy Algorithm to Build Route for Truck 3
            # Run Package Delivery for Truck 3
            print("\nDelivering truck 3: ")
            node_list = prep_route(package_list3, pack_table, addr_dict, node_list)
            truck3_distance = float(format(greedy_route(node_list, distance_table, truck3_route), '.2f'))
            truck3_time = calc_return_time(truck3_distance, truck1_time)
            deliver_packages(truck1_time, package_list3, pack_table, addr_invert, distance_table, truck3_route)
            print("Truck 3 Distance: %s" % str(truck3_distance))
            print("Truck 3 Time: %s" % str(truck3_time))

            total_distance = format(truck1_distance + truck2_distance + truck3_distance, '.2f')
            print("Total distance driven: %s" % str(total_distance))
            switch = 'home_screen'
            simulation_flag = 1
            break

        # If Core Algorithm has already been run, display message and return to main menu
        else:
            print("          SIMULATION FOR THIS DATA SET HAS ALREADY BEEN PERFORMED...")
            switch = input("          ENTER 'return' TO RETURN TO MAIN MENU")
            break

    # package id search control loop
    while switch == 'package search':
        print("\n          PACKAGE SEARCH")
        packid = int(input("          ENTER A PACKAGE ID..."))
        lookup_package(pack_table, packid)
        switch = input("          ENTER 'return' TO RETURN TO MAIN MENU...")
        break

    # time search control loop
    while switch == 'time search':
        print("\n          TIME SEARCH")
        search_time = input("          ENTER A TIME IN 'HH:MM:SS' FORMAT...")
        lookup_time(pack_table, search_time)
        switch = 'home_screen'
        break

    # terminate program on user input of 'exit'
    while switch == 'exit':
        print("\n          TERMINATING SYSTEM...")
        exit()

    # Error detection; if user input is not in dictionary of given command,
    # return error message and prompt for approved input until given
    while switch not in {'continue', 'return', 'home_screen', 'package search', 'time search', 'exit'}:
        print("\n          '%s' IS NOT A KNOWN COMMAND...\n" % switch)
        switch = input("          ENTER 'continue' TO RUN THE DLD SIMULATION...\n"
                       "          ENTER 'return' TO RETURN TO THE MAIN MENU...")
        break

import csv
from package import Package


# space complexity: O(n)    time complexity: O(n)
def load_package_data(file, table):
    with open(file) as in_file:
        pack_dat = csv.reader(in_file, delimiter=',')
        next(in_file)  # pass over header

        for p in pack_dat:
            in_id = int(p[0])
            in_address = p[1]
            in_city = p[2]
            in_state = p[3]
            in_zip = p[4]
            in_deadline = p[5]
            in_mass = p[6]
            in_special = p[7]

            # create package instance
            package = Package(in_id, in_address, in_city, in_state, in_zip,
                              in_deadline, in_mass, in_special)

            table.insert(in_id, package)


# space complexity: O(n)    time complexity: O(n)
def load_address_data(file, table):
    with open(file) as in_file:
        address_data = csv.reader(in_file, delimiter=',')
        next(in_file)  # skip header
        for a in address_data:
            add_id = int(a[0])
            address = a[1]
            table[address] = add_id


# space complexity: O(n)    time complexity: O(n)
def load_distance_data(file, table):
    with open(file) as in_file:
        distance_data = csv.reader(in_file, delimiter=',')
        in_tup = ()
        for d in distance_data:
            for k in range(27):
                distance = (float(d[k]),)
                in_tup = in_tup + distance
            table.insert(k+1, in_tup)
            in_tup = ()

from datetime import *


# space complexity O(n^2)    time complexity: O(n^2)
def deliver_packages(current_time, pack_list, pack_table, reverse_addr, distance_table, delivery_route):
    previous_node = 1
    for r in delivery_route:
        previous_address = 0
        for pk in pack_list:
            if pack_table.lookup(pk).address == previous_address:
                pack_table.lookup(pk).delivery_time = current_time
                pack_table.lookup(pk).status = "DELIVERED"
                print('Delivering %d to %d at %s' % (pk, r, str(current_time)))
                previous_address = pack_table.lookup(pk).address
                pack_list.remove(pk)

            elif pack_table.lookup(pk).address == reverse_addr[r]:
                distance_row = distance_table[previous_node-1]
                pack_dist = distance_row[r-1]
                time_dist = divmod(pack_dist, .3)
                time_mins = time_dist[0]
                time_secs = float(format((time_dist[1] / .3) * 60, '.2f'))
                del_time = datetime.combine(date.today(), current_time) +\
                    timedelta(minutes=time_mins, seconds=time_secs)
                pack_table.lookup(pk).delivery_time = del_time.time()
                pack_table.lookup(pk).status = "DELIVERED"
                current_time = del_time.time()
                print('Delivering %d to %d at %s' % (pk, r, str(current_time)))
                previous_address = pack_table.lookup(pk).address
                pack_list.remove(pk)
        previous_node = r


# space complexity: O(n)    time complexity: O(n^2)
def greedy_route(nodes, distances, route):
    tot_distance = 0
    while len(nodes) > 1:
        distance = 100
        nod = nodes.pop(0)
        for i in nodes:
            dist_row = distances[nod - 1]
            adj_dist = dist_row[i-1]
            if adj_dist < distance:
                distance = adj_dist
                adj_nod = i
        tot_distance += distance
        route.append(adj_nod)
        nodes.remove(adj_nod)
        nodes.insert(0, adj_nod)
    dist_row = distances[0]
    adj_dist = dist_row[i-1]
    tot_distance += adj_dist
    nodes.pop(0)
    return tot_distance


# space complexity: O(n)    time complexity: O(n)
def prep_route(package_list, package_table, address_table, node_lst):
    node_lst.append(1)
    for p in package_list:
        node = package_table.lookup(p).address
        node_lst.append(int(address_table[node]))
        package_table.lookup(p).status = "EN_ROUTE"
    return node_lst


# space complexity: O(1)    time complexity: O(1)
def calc_return_time(total_dist, departure_time):
    time_dist = divmod(total_dist, .3)
    time_mins = time_dist[0]
    time_secs = float(format((time_dist[1] / .3) * 60, '.2f'))
    del_time = datetime.combine(date.today(), departure_time) + timedelta(minutes=time_mins, seconds=time_secs)
    return del_time.time()


# space complexity: O(1)    time complexity: O(1)
def lookup_package(package_table, pack_id):
    package = package_table.lookup(pack_id)
    print("          PACKAGE SEARCH RESULT: %s" % str(package))


# space complexity: O(n)    time complexity: O(n)
def lookup_time(package_table, search_time):
    search_time_tuple = tuple(map(int, search_time.split(':')))
    search_time = datetime.now().replace(hour=search_time_tuple[0], minute=search_time_tuple[1],
                                         second=search_time_tuple[2], microsecond=0)
    for i in range(1, 41):
        time_tuple = tuple(map(int, str(package_table.lookup(i).delivery_time).split(':')))
        search = datetime.now().replace(hour=time_tuple[0], minute=time_tuple[1],
                                        second=time_tuple[2], microsecond=0)
        if search <= search_time:
            print("          TIME: %s  PACKAGE %d:  DELIVERED AT: %s" % (str(search_time.time()), i,
                                                                         str(search.time())))
        else:
            print("          TIME: %s  PACKAGE %d:  NOT DELIVERED" % (str(search_time.time()), i))

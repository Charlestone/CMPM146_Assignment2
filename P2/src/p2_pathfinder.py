"""    Authors: Carlos del Rey (1710268) and Harmen Kang (1523720)"""from heapq import heappush, heappopfrom math import sqrtdef check_point_in_box(box, point):    if(point[0] >= box[0] and point[0] <= box[1] and point[1] >= box[2] and point[1] <= box[3]):        return True    return Falsedef euc_dist(point1, point2):    distance = sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)    return distancedef get_entry_point(point_from, box_from, box_to):    x = (max(box_from[0], box_to[0]),min(box_from[1], box_to[1]))    y = (max(box_from[2], box_to[2]),min(box_from[3], box_to[3]))    if (point_from[0] < x[0]):        aux_x = x[0]    else:        if(point_from[0] > x[1]):            aux_x = x[1]        else:            aux_x = point_from[0]    if (point_from[1] < y[0]):        aux_y = y[0]    else:        if(point_from[1] > y[1]):            aux_y = y[1]        else:            aux_y = point_from[1]    return (aux_x,aux_y)def find_path (source_point, destination_point, mesh):    """    Searches for a path from source_point to destination_point through the mesh    Args:        source_point: starting point of the pathfinder        destination_point: the ultimate goal the pathfinder must reach        mesh: pathway constraints the path adheres to    Returns:        A path (list of points) from source_point to destination_point if exists        A list of boxes explored by the algorithm    """        #List of segments (pair of points)    path = []    boxes = []    cost_source = {}    cost_destination = {}    parents_source = {}    parents_destination = {}    entry_point_source = {}    entry_point_destination = {}    next_nodes_source = []    next_nodes_destination = []    initial_box = None    destination_box = None    found = False    #Get the initial box and the destination box    for box in mesh['boxes']:        if(check_point_in_box(box, source_point) == True and initial_box == None):            initial_box = box            cost_source[box] = 0            heappush(next_nodes_source, (cost_source[box] + euc_dist(source_point, destination_point), box))            parents_source[box] = None            entry_point_source[box] = source_point        if(check_point_in_box(box, destination_point) == True and destination_box == None):            destination_box = box            cost_destination[box] = 0            heappush(next_nodes_destination, (cost_destination[box] + euc_dist(destination_point, source_point), box))            parents_destination[box] = None            entry_point_destination[box] = destination_point        if(next_nodes_source and next_nodes_destination):            break    #If one of the selected point is not in a box, there is no possible path between them    if(not next_nodes_source or not next_nodes_destination):        print('No path!')        return path, boxes    while(next_nodes_source or next_nodes_destination):        if(next_nodes_source):            #Pop the next element of the heap_source            current = heappop(next_nodes_source)            #Check if the current box is in the path from the destination            if(current[1] in cost_destination):                found = True                break            #Obtain the adjacents to the current box            adjacents = mesh['adj'][current[1]]            #For every adjacent            for adj in adjacents:                #Get the entry point to the adjacent                aux_entry = get_entry_point(entry_point_source[current[1]], current[1], adj)                #Get the total cost_source                adj_cost = euc_dist(aux_entry, destination_point) + euc_dist(aux_entry, entry_point_source[current[1]]) + cost_source[current[1]]                #If the adj is new or we've found a better cost_source for it                if((adj not in cost_source) or (adj_cost < cost_source[adj] + euc_dist(entry_point_source[adj], destination_point))):                    cost_source[adj] = euc_dist(aux_entry, entry_point_source[current[1]]) + cost_source[current[1]]                    parents_source[adj] = current[1]                    entry_point_source[adj] = aux_entry                    heappush(next_nodes_source, (adj_cost, adj))        if(next_nodes_destination):            #Pop the next element of the heap_destination            current = heappop(next_nodes_destination)            #Check if the current box is in the path from the source            if(current[1] in cost_source):                found = True                break            #Obtain the adjacents to the current box            adjacents = mesh['adj'][current[1]]            #For every adjacent            for adj in adjacents:                #Get the entry point to the adjacent                aux_entry = get_entry_point(entry_point_destination[current[1]], current[1], adj)                #Get the total cost_destination                adj_cost = euc_dist(aux_entry, source_point) + euc_dist(aux_entry, entry_point_destination[current[1]]) + cost_destination[current[1]]                #If the adj is new or we've found a better cost_destination for it                if((adj not in cost_destination) or (adj_cost < cost_destination[adj] + euc_dist(entry_point_destination[adj], source_point))):                    cost_destination[adj] = euc_dist(aux_entry, entry_point_destination[current[1]]) + cost_destination[current[1]]                    parents_destination[adj] = current[1]                    entry_point_destination[adj] = aux_entry                    heappush(next_nodes_destination, (adj_cost, adj))    #Introduce the segment of the box that's in both paths    path.append((entry_point_destination[current[1]],entry_point_source[current[1]]))    current_dest = current    #Add the boxes and segments from the source path    while(current[1] != initial_box):        path.append((entry_point_source[parents_source[current[1]]],entry_point_source[current[1]]))        boxes.append(current[1])        current = (1, parents_source[current[1]])    path.append((source_point, entry_point_source[current[1]]))    boxes.append(current[1])    #Add the boxes and segments from the destination path    while(current_dest[1] != destination_box):        path.append((entry_point_destination[parents_destination[current_dest[1]]],entry_point_destination[current_dest[1]]))        boxes.append(current_dest[1])        current_dest = (1, parents_destination[current_dest[1]])    path.append((destination_point, entry_point_destination[current_dest[1]]))    boxes.append(current_dest[1])       if(found == False):        print('No path!')                    return path, boxes
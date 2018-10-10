def find_path (source_point, destination_point, mesh):    """    Searches for a path from source_point to destination_point through the mesh    Args:        source_point: starting point of the pathfinder        destination_point: the ultimate goal the pathfinder must reach        mesh: pathway constraints the path adheres to    Returns:        A path (list of points) from source_point to destination_point if exists        A list of boxes explored by the algorithm    """    path = []    boxes = {}    boxes_source = []    boxes_destination = []    boxes_visited_from_source = []    boxes_visited_from_destination = []    parents_from_source = {}    parents_from_destination = {}    print('source_point: ',source_point)    print('destination_point', destination_point)    #Check intial boxes    print('Please wait...')    for box in mesh['boxes']:        if(check_point_in_box(box, source_point) == True and not boxes_sour):            print('source_box', box)            boxes_source.append(box)        if(check_point_in_box(box, destination_point) == True and not boxes_dest):            print('destination_box', box)            boxes_destination.append(box)        if(boxes_dest and boxes_sour):            break    print('For finished')    if(boxes_destination and boxes_source):        if(boxes_destiantion[0] == boxes_source[0]):            print('Done')        #We have the two initial boxes    while(boxes_destiantion and boxes_source):    return path, boxes.keys()def check_point_in_box(box, point):    if(point[0] >= box[0] and point[0] <= box[1] and point[1] >= box[2] and point[1] <= box[3]):        return True    return False
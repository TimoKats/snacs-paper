import json
import os

def export_csv(size_method, crosses, bends):
    output = open('data.csv', 'a', encoding='utf-8')
    size = size_method.split('_')[0]
    method = size_method.split('_')[1]
    output.write(size + ',' + method + ',' + str(crosses) + ',' + str(bends) + '\n')
    output.close()

##stackoverflow#https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect###################

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(A, B, C):
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)

def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

########################################################################################################################

def get_nodes(data):
    nodes, node_temp = [], {}
    for node in data['nodes']:
        node_temp['x'] = node['x']
        node_temp['y'] = node['y']
        nodes.append(node_temp)
    return nodes

def get_edges(data):
    edges, edge_temp = [], {}

    for edge in data['edges']:
        source = edge['source']
        target = edge['target']
        edge_temp = {}
        for node in data['nodes']:
            if node['id'] == source:
                edge_temp['x1'] = node['x']
                edge_temp['y1'] = node['y']
            elif node['id'] == target:
                edge_temp['x2'] = node['x']
                edge_temp['y2'] = node['y']
        edges.append(edge_temp)
    return edges

def count_intersects(edges):
    intersects = 0
    for edge1 in edges:
        A = point(edge1['x1'], edge1['y1'])
        B = point(edge1['x2'], edge1['y2'])
        for edge2 in edges:
            if edge1 != edge2:
                C = point(edge2['x1'], edge2['y1'])
                D = point(edge2['x2'], edge2['y2'])
                if intersect(A, B, C, D):
                    intersects += 1
    return int(intersects / 2) # avoid double counts

def count_bends(nodes, edges):
    bends = 0
    for edge in edges:
        A = point(edge['x1'], edge['y1'])
        B = point(edge['x2'], edge['y2'])
        for node in nodes:  # make a small area to create the node
            C = point(node['x'], node['y'])
            D = point(node['x'] + 1, node['y'] + 1)
            if intersect(A, B, C, D):
                bends += 1
            C = point(node['x'], node['y'])
            D = point(node['x'] + 1, node['y'] - 1)
            if intersect(A, B, C, D):
                bends += 1
            C = point(node['x'], node['y'])
            D = point(node['x'] - 1, node['y'] + 1)
            if intersect(A, B, C, D):
                bends += 1
            C = point(node['x'], node['y'])
            D = point(node['x'] - 1, node['y'] - 1)
            if intersect(A, B, C, D):
                bends += 1
    return int(bends / 2) # avoid double counts

def number_of_edge_crossings(file):
    file = open(file)
    data = json.load(file)
    edges = get_edges(data)
    intersects = count_intersects(edges)
    return intersects

def number_of_edge_bends(file):
    file = open(file)
    data = json.load(file)
    edges = get_edges(data)
    nodes = get_nodes(data)
    bends = count_bends(nodes, edges)
    return bends

if __name__ == '__main__':

    files = {}
    for filename in os.listdir("json"):
        name = filename[:-5]
        location = "json/" + filename
        files[name] = location

    export_csv('file_method', '#edge crossings', '#edge bends')
    for i in files:
        export_csv(i, number_of_edge_crossings(files[i]), number_of_edge_bends(files[i]))

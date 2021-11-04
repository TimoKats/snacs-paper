import json
import os


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def ccw(A, B, C):  # stackoverflow https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
    return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


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
    return int(intersects / 2)


# making definition of opening file and calculating edges
def number_of_edge_crossings(method, file):
    file = open(file)
    data = json.load(file)
    edges = get_edges(data)
    intersects = count_intersects(edges)
    print("method used:", method, 'The amount of edge crossings equals:', intersects)


# main with the files used
if __name__ == '__main__':

    files = {}
    # if a file is in the folder json we will get the number of edgecrossings
    for filename in os.listdir("json"):
        name = filename[:-5]
        location = "json/" + filename
        files[name] = location

    for i in files:
        number_of_edge_crossings(i, files[i])

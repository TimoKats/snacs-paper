import json

class point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ccw(A,B,C): # stackoverflow https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

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
                if intersect(A,B,C,D):
                    intersects += 1
    return int(intersects/2)

if __name__ == '__main__':
    file = open('json/small_forceatlas.json', )
    data = json.load(file)
    edges = get_edges(data)
    intersects = count_intersects(edges)
    print('the amount of edge crossings equals: ', intersects)
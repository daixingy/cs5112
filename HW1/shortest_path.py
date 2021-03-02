# TODO: Xingyue Dai, xd86

from graph_adjacency_list import Graph 
# from graph_edge_list import Graph 
# Please see instructions.pdf for the description of this problem.

# helper class
# created a priorityqueue to store nodes visited
class PriorityQueue:
  def __init__(self):
    self.pairs = []

  def add(self,node_weight):

    self.pairs.append(node_weight)
    self.sort()

# update the list by deleting all previous tuples containing the node in 
# node_weight pair and then adding node_weight 
  def update(self,node_weight):
    node = node_weight[0]
    for i in self.pairs:
      if node == i[0]:
        self.pairs.remove(i) 
    self.pairs.append(node_weight)
    self.sort()   

# return the first item in list, which is the one with the smallest distance
  def pop(self):
    if len(self.pairs) != 0:
      item = self.pairs.pop(0)
      return item

# sort the list by distances in ascending order
  def sort(self):
    self.pairs = sorted(self.pairs, key=lambda x:x[1])


def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.pdf for additional information about the
  # return value of this method.

  # TODO: YOUR CODE HERE, delete the `raise NotImplementedError`line below once you finish writing your code


  # this dictionary stores all current shortest distances between source and each node i in the graph,
  # it also stores through which node source reaches node i
  optimal_distances = {}
  visited = PriorityQueue()
  explored = []
  visited.add((source,0))

  # add source to the optimal_distances, the source can reach the source in 0 distance.
  optimal_distances[source] = [0,source]

  # keep finding the path and shortest distance while the target hasn't been explored
  while target not in explored:
    current = visited.pop()
    current_node, current_shortest_distance = current[0],current[1]
    neighbors = graph.get_neighbors(current_node)

    for i in neighbors:
      neighbor_node, neighbor_weight = i[0], i[1]
      if neighbor_node not in explored:
        current_distance = current_shortest_distance + neighbor_weight
        #create a shortest distance to neighrbor_node with current_shortest_distance
        if neighbor_node not in optimal_distances:
          optimal_distances[neighbor_node] = [current_distance,current_node]
          visited.add((neighbor_node,current_distance))
        #update the shortest distance on record if current_shortest_distance is smaller
        elif current_distance < optimal_distances[neighbor_node][0]:
          optimal_distances[neighbor_node][0] = current_distance
          optimal_distances[neighbor_node][1] = current_node
          visited.update((neighbor_node,current_distance))
          
    explored.append(current_node)

  key = target
  path = [target]
  #keep tracing back the nodes from the target to the source
  while key != source:
    path.insert(0,optimal_distances[key][1])
    key = optimal_distances[key][1]


  return tuple([path,optimal_distances[target][0]])

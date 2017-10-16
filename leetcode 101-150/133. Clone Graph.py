"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph_dfs(self, node):
        if node is None:
            return None
        visit_set = {}

        def dfs(input_node):
            if input_node.label in visit_set:
                return visit_set[input_node.label]
            output_node = UndirectedGraphNode(input_node.label)
            visit_set[input_node.label] = output_node
            for neighbor in input_node.neighbors:
                output_node.neighbors.append(dfs(neighbor))
            return output_node

        return dfs(node)

    def cloneGraph(self, node):
        if node is None:
            return None

        cloned_node = UndirectedGraphNode(node.label)
        visit_set, queue = {node: cloned_node}, [node]
        while queue:
            tmp_node = queue.pop()
            for neighbor in tmp_node.neighbors:
                if neighbor not in visit_set:
                    queue.append(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    visit_set[neighbor] = cloned_neighbor
                visit_set[tmp_node].neighbors.append(visit_set[neighbor])
        return cloned_node


if __name__ == "__main__":
    node_0 = UndirectedGraphNode(0)
    node_1 = UndirectedGraphNode(1)
    node_2 = UndirectedGraphNode(2)
    node_0.neighbors = [node_1, node_2]
    node_1.neighbors = [node_0, node_2]
    node_2.neighbors = [node_0, node_1, node_2]
    new_node_0 = Solution().cloneGraph(node_0)
    new_node_1 = new_node_0.neighbors[0]
    new_node_2 = new_node_0.neighbors[1]
    assert new_node_0.val == 0
    assert new_node_1.val == 1
    assert new_node_1.neighbors == [new_node_0, new_node_2]
    assert new_node_2.val == 2 == [new_node_0, new_node_1, new_node_2]

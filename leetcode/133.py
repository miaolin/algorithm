#!/usr/bin/env python
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
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode

        DFS
        """

        if node == None:
            return None
        
        visited = {}
        stack = [node]
        root = UndirectedGraphNode(node.label)
        visited[node.label] = root

        while len(stack) != 0:
            node = stack.pop()
            for n in node.neighbors:
                if n.label not in visited:
                    stack.append(n)
                    visited[n.label] = UndirectedGraphNode(n.label)
                visited[node.label].neighbors.append(visited[n.label])

        return root

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode

        DFS
        """

        if node == None:
            return None
        
        visited = {}
        stack = [node]
        root = UndirectedGraphNode(node.label)
        visited[node] = root

        while len(stack) != 0:
            node = stack.pop()
            for n in node.neighbors:
                if n not in visited:
                    stack.append(n)
                    visited[n] = UndirectedGraphNode(n.label)
                visited[node].neighbors.append(visited[n])

        return root

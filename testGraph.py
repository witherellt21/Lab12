"""
File: testGraph.py

Taylor Witherell
"""

from modules.graph.graph import LinkedDirectedGraph
from modules.graph.pathEntry import PathEntry
from modules.stack.linkedStack import LinkedStack
from modules.queue.linkedQueue import LinkedQueue
from modules.utils.grid import Grid
from modules.utils.arrays import Array
from modules.math.infinity import *



def traverseFromVertex(graph, startVertex, showProcess, collection = LinkedStack()):
    # Exercise
    graph.clearVertexMarks()
    collection.add(startVertex)
    while len(collection) != 0:
        vertex = collection.pop()
        if not vertex.isMarked():
            if showProcess:
                print(vertex)
            vertex.setMark()
            for edge in vertex.incidentEdges():
                if vertex == edge.getConnectedFrom():
                    collection.add(edge.getConnectedTo())






def depthFirstTraverse(graph, startVertex, showProcess):
    # Exercise
    traverseFromVertex(graph, startVertex, showProcess, LinkedStack())

def breadthFirstTraverse(graph, startVertex, showProcess):
    # Exercise
    traverseFromVertex(graph, startVertex, showProcess, LinkedQueue())


def main():

    # Create a directed graph using an adjacency list
    graph = LinkedDirectedGraph()

    # Exercise: Add vertices with appropriate labels and print the graph
    graph.addVertex('A')
    graph.addVertex('B')
    graph.addVertex('C')
    graph.addVertex('D')
    graph.addVertex('E')
    graph.addVertex('F')
    graph.addVertex('G')
    graph.addVertex('H')
    graph.addVertex('I')
    graph.addVertex('J')
    print("\nThe graph: \n" + str(graph))

    # Exercise: Insert edges with weights and print the graph
    graph.addEdge("A", "J", 1)
    graph.addEdge("A", "I", 8)
    graph.addEdge("A", "B", 3)
    graph.addEdge("B", "C", 2)
    graph.addEdge("C", "E", 4)
    graph.addEdge("C", "G", 2)
    graph.addEdge("D", "I", 1)
    graph.addEdge("G", "D", 1)
    graph.addEdge("G", "F", 1)
    graph.addEdge("H", "B", 2)
    graph.addEdge("H", "E", 1)
    graph.addEdge("J", "B", 1)
    graph.addEdge("J", "H", 6)

    print("\nThe graph: \n" + str(graph))

    # Print the vertices adjacent to vertex A
    print("\nExpect vertices adjacent to A:")
    print(", ".join(list(map(str,graph.getVertex("A").neighboringVertices()))))

    # Print the edges incident to A
    print("Expect edges incident to A:")
    print(", ".join(list(map(str,graph.getVertex("A").incidentEdges()))))

    # Exercise
    print("\nTraverse from vertex A:")
    traverseFromVertex(graph, graph.getVertex("A"), True)

    # Exercise
    print("\nDepth first traversal:")
    depthFirstTraverse(graph, graph.getVertex("A"), True)

    # Exercise
    print("\nBreadth first traversal:")
    breadthFirstTraverse(graph, graph.getVertex("A"), True)


if __name__ == '__main__':
    main()
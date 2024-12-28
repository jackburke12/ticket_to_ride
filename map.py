import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Priority queue to store (distance, vertex)
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Skip if a shorter path to the vertex has already been found
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If a shorter path is found, update the distance and push to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Create a directed graph

def view_graph(graph):
    G = nx.Graph()
    # Add edges with weights
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Get edge weights for display
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Draw the graph
    pos = nx.spring_layout(G)  # Layout for nodes
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=100, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Show the plot
    plt.title("Graph Representation")
    plt.show()

def determine_point_value(end, paths):
    shortest_path = paths[end]
    return shortest_path
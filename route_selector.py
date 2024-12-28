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

graph = {
    'Edinburgh': {'London': 4},
    'London': {'Edinburgh': 4, 'Amsterdam': 2, 'Dieppe': 2},
    'Dieppe': {'London': 2, 'Bruxelles': 2, 'Paris': 1, 'Brest':2},
    'Brest':{'Dieppe':2,'Paris':3,'Pamplona':4},
    'Pamplona':{'Brest':4,'Paris':4,'Marseilles':4,'Barcelona':2,'Madrid':3},
    'Madrid':{'Pamplona':3,'Lisboa':3,'Cadiz':3,'Barcelona':2},
    'Lisboa':{'Madrid':3,'Cadiz':2},
    'Cadiz':{'Lisboa':2,'Madrid':3},
    'Barcelona':{'Madrid':2,'Pamplona':2,"Marseilles":4},
    'Paris':{'Dieppe':1,'Brest':3,'Pamplona':4,'Marseilles':4,'Zurich':3,'Frankfurt':3,'Bruxelles':2},
    'Bruxelles':{'Dieppe':2,'Paris':2,'Frankfurt':2,'Amsterdam':1},
    'Amsterdam':{'Bruxelles':1,'London':2,'Frankfurt':2,'Essen':3},
    'Marseilles':{'Barcelona':4,'Pamplona':4,'Paris':4,'Zurich':2,'Roma':4},
    'Zurich':{'Marseilles':2,'Venezia':2,'Munchen':2,'Paris':3},
    'Frankfurt':{'Munchen':2,'Paris':3,'Bruxelles':2,'Amsterdam':2,'Essen':2,'Berlin':3},
    'Essen':{'Amsterdam':3,'Frankfurt':2,'Berlin':2,'Kobenhaven':3},
    'Stockholm':{'Kobenhaven':3,'Petrograd':8},
    'Kobenhaven':{'Essen':3,'Stockholm':3},
    'Berlin':{'Essen':2,'Frankfurt':3,'Wien':3,'Warzawa':4,'Danzig':4},
    'Munchen':{'Frankfurt':2,'Zurich':2,'Venezia':2,'Wien':3},
    'Venezia':{'Zurich':2,'Munchen':2,'Zagrab':2,'Roma':2},
    'Roma':{'Marseilles':4,'Venezia':2,'Palermo':4,'Brindisi':2},
    'Palermo':{'Roma':4,'Brindisi':3,'Smyrna':6},
    'Brindisi':{'Roma':2,'Palermo':3,'Athina':4},
    'Zagrab':{'Venezia':2,'Sarajevo':3,'Budapest':2,'Wien':2},
    'Wien':{'Zagrab':2,'Munchen':3,'Berlin':3,'Warzawa':4,'Budapest':1},
    'Sarajevo':{'Zagrab':3,'Budapest':3,'Sofia':2,'Athina':4},
    'Athina':{'Smyrna':2,'Brindisi':4,'Sofia':3,'Sarajevo':4},
    'Sofia':{'Constantinople':3,'Athina':3,'Sarajevo':2,'Bucharesti':2},
    'Budapest':{'Sarajevo':3,'Zagrab':2,'Wien':1,'Kiev':6,'Bucharesti':4},
    'Danzig':{'Berlin':4,'Warzawa':2,'Riga':3},
    'Warzawa':{'Danzig':2,'Berlin':4,'Wien':4,'Kiev':4,'Wilno':3},
    'Riga':{'Danzig':3,'Wilno':4,'Petrograd':4},
    'Wilno':{'Kiev':2,'Warzawa':3,'Riga':4,'Petrograd':4,'Smolensk':3},
    'Petrograd':{'Stockholm':8,'Moskva':4,'Wilno':4,'Riga':4},
    'Moskva':{'Petrograd':4,'Smolensk':2,'Kharkov':4},
    'Smolensk':{'Wilno':3,'Moskva':2,'Kiev':3},
    'Kiev':{'Wilno':2,'Smolensk':3,'Kharkov':4,'Bucharesti':4,'Budapest':6,'Warzawa':4},
    'Bucharesti':{'Sofia':2,'Budapest':4,'Kiev':4,'Sevastopol':4,'Constantinople':3},
    'Kharkov':{'Kiev':4,'Moskva':4,'Rostov':2},
    'Rostov':{'Kharkov':2,'Sevastopol':4,'Sochi':2},
    'Sevastopol':{'Bucharesti':4,'Rostov':4,'Sochi':2,'Erzurum':4,'Constantinople':4},
    'Sochi':{'Rostov':2,'Sevastopol':2,'Erzurum':3},
    'Angora':{'Constantinople':2,'Erzurum':3,'Smyrna':3},
    'Smyrna':{'Palermo':6,'Athina':2,'Constantinople':2,'Angora':3},
    'Erzurum':{'Angora':3,'Sevastopol':4,'Sochi':3},
    'Constantinople':{'Smyrna':2,'Angora':2,'Sevastopol':4,'Bucharesti':3,'Sofia':3}
}

def menu():
    choice = input("Please select a starting city: ")

    if choice not in graph.keys():
        choice = input("That city does not exist. Please select a different starting city: ")

    paths = dijkstra(graph,choice)
    print(paths)
    end = input("Please select a destination city: ")
    segments = determine_point_value(end,paths)
    print(f'The route from {choice} to {end} is worth {segments} points.')

view_graph(graph)

if __name__ == "__main__":
    menu()
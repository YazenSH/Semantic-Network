import networkx as nx
import matplotlib.pyplot as plt

# Create two directed graphs
E = nx.DiGraph()  # Example graph
G = nx.DiGraph()  # General graph
a = True  # A flag for the main loop


# Function to define the structure of the general graph
def node_general():
    G.add_nodes_from(["Doctor", "Patient", "Hospital", "Illness", "Medicine", "Symptom"])
    G.add_edge("Doctor", "Patient", relationship="Diagnose")
    G.add_edge("Patient", "Hospital", relationship="Belong_To")
    G.add_edge("Patient", "Illness", relationship="Suffer_From")
    G.add_edge("Illness", "Medicine", relationship="Treated_By")
    G.add_edge("Illness", "Symptom", relationship="Shows")


# Function to create an example graph
def node_example():
    E.add_edge("Dr.Ali", "Ahmad", relationship="Diagnose")
    E.add_edge("Dr.Ali", "Khalid", relationship="Diagnose")
    E.add_edge("Ahmad", "King Fahd Hospital", relationship="Belong_To")
    E.add_edge("Khalid", "King Fahd Hospital", relationship="Belong_To")
    E.add_edge("Ahmad", "Flu", relationship="Suffer_From")
    E.add_edge("Khalid", "Pink Eye", relationship="Suffer_From")
    E.add_edge("Flu", "Oseltamivir", relationship="Treated_By")
    E.add_edge("Pink Eye", "Antibiotic Eye drops", relationship="Treated_By")
    E.add_edge("Flu", "Fever", relationship="Shows")
    E.add_edge("Flu", "Headache", relationship="Shows")
    E.add_edge("Pink Eye", "Inflammation", relationship="Shows")
    E.add_edge("Pink Eye", "Itching", relationship="Shows")


# Function to add an edge between two nodes with a relationship
def node_add(first, second, relat):
    return E.add_edge(first, second, relationship=relat)


# Function to delete a node
def node_del(node):
    if node in E:
        print("{} successfully removed".format(node))
        return E.remove_node(node)
    else:
        print("Node does not exist")


# Function to search for nodes by relationship
def search_nodes_by_relationship(relationship, graph=E):
    connected_nodes = [(u, v) for u, v, attrs in graph.edges(data=True) if attrs['relationship'] == relationship]
    if connected_nodes:
        result = "\n".join(["{} {} {}".format(u, relationship, v) for u, v in connected_nodes])
        return "Nodes connected by the relationship '{}':\n{}".format(relationship, result)
    else:
        return "No nodes are connected by the relationship '{}'".format(relationship)

# Function to search for a path from 'source' to 'destination' in the graph 'E'
def search_node(source, destination, graph=E):
    if source not in graph.nodes or destination not in graph.nodes:
        return "Source or destination node does not exist in the graph."

    paths = nx.all_simple_paths(graph, source=source, target=destination)
    for path in paths:
        edges = list(zip(path, path[1:]))
        relations = [graph.edges[edge]['relationship'] for edge in edges]
        return "Path from {} to {} is found. Relation is: {}".format(source, destination, " -> ".join(relations))
    return "Path from {} to {} is not found".format(source, destination)

# Create the structure of the general graph
node_general()

while (a):
    print("""\nOption 1: Add/link nodes with the relationship
Option 2: Delete a node
Option 3: Visualize Example graph
Option 4: Visualize General graph
Option 5: Create Example graph
Option 6: Search node path from source to destination
Option 7: Search nodes by relationship
Option 8: Exit program\n""")

    Choice = int(input("Enter your choice (1-8): \n"))

    if (Choice == 1):
        first = input('What is the first node? ')
        second = input('What is the second node? ')
        relat = input('What is the relationship? ')
        node_add(first, second, relat)
        print("{} {} {} successfully added".format(first, relat, second))

    elif (Choice == 2):
        node = input('Write the node you want to delete: ')
        node_del(node)

    elif (Choice == 3):
        pos = nx.shell_layout(E, scale=20)
        nx.draw(E, pos, with_labels=True, node_size=3000)
        labels = nx.get_edge_attributes(E, 'relationship')
        nx.draw_networkx_edge_labels(E, pos, edge_labels=labels, font_color="red")
        plt.show()

    elif (Choice == 4):
        pos = nx.planar_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=3000)
        labels = nx.get_edge_attributes(G, 'relationship')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color="red")
        plt.show()

    elif (Choice == 5):
        node_example()

    elif Choice == 6:
        source = input('Start node: ')
        destination = input('Destination node: ')
        print(search_node(source, destination))

    elif Choice == 7:
        relationship = input('Enter the relationship to search for: ')
        matching_edges = search_nodes_by_relationship(relationship)
        print(f"{matching_edges}")

    elif (Choice == 8):
        a = False  # Terminate Program

    else:
        print("Invalid choice. Please try again.")

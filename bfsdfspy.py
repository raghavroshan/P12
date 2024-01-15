import networkx as nx
import matplotlib.pyplot as plt

def read_graph_from_notepad(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    graph = nx.Graph()

    for line in lines:
        # Assuming the file has edges listed as pairs of nodes separated by a space
        nodes = line.strip().split()
        if len(nodes) == 2:
            graph.add_edge(nodes[0], nodes[1])

    return graph

def draw_graph(graph, title="Graph"):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')
    plt.title(title)
    plt.show()

def bfs(graph, start_node):
    visited = set()
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)
            queue.extend(neighbor for neighbor in graph.neighbors(current_node) if neighbor not in visited)

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    if start_node not in visited:
        print(start_node, end=" ")
        visited.add(start_node)
        for neighbor in graph.neighbors(start_node):
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    # Replace 'your_notepad_file.txt' with the path to your actual Notepad file
    file_path = 'bfsdfs.txt'

    # Read graph from Notepad file
    graph = read_graph_from_notepad(file_path)

    # Draw the graph
    draw_graph(graph)

    # Perform BFS starting from node 'A'
    print("BFS traversal:")
    bfs(graph, 'A')

    # Perform DFS starting from node 'A'
    print("\nDFS traversal:")
    dfs(graph, 'A')

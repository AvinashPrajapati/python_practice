class Node:
    visit = ["not-visited", "visited"]
    node_name = None
    node_data = None
    node_connected = []
    visited = visit[0]  #


def print_node(node):
    print(f"({node.node_name},{node.node_data})->{node.node_connected}")


n1 = Node()
n1.node_name = "A"
n1.node_data = "shop"
n1.node_connected = [["B", 2], ["C", 1.3]]
print_node(n1)

n2 = Node()
n2.node_name = "B"
n2.node_data = "market"
n2.node_connected = [["A", 2]]
print_node(n2)

import networkx as nx


def part_one(filename: str) -> str:
    G = get_data(filename)
    G.remove_edges_from(nx.minimum_edge_cut(G))
    first, second = nx.connected_components(G)
    return str(len(first) * len(second))


def get_data(filename: str):
    with open(filename, "r") as file:
        data = file.read().splitlines()
    G = nx.Graph()
    for line in data:
        l, r = line.split(":")
        for node in r.strip().split(" "):
            G.add_edge(l, node)
            G.add_edge(node, l)
    return G


if __name__ == "__main__":
    input_path = "input.txt"
    with open("output1.txt", "w") as f:
        f.write(part_one(input_path))

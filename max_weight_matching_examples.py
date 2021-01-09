import networkx as nx
from networkx.algorithms.matching import matching_dict_to_set
from networkx.testing import assert_edges_equal


# These tests format were taken from here:
# https://www.programcreek.com/python/example/89574/networkx.max_weight_matching
def test1():
    G = nx.Graph()
    G.add_edge(1, 4, weight=5)
    G.add_edge(2, 4, weight=7)
    G.add_edge(2, 5, weight=10)
    G.add_edge(3, 5, weight=12)
    G.add_edge(3, 6, weight=15)

    assert_edges_equal(nx.max_weight_matching(G),
                       matching_dict_to_set({2: 5, 1: 4, 3: 6}))


def test2():
    G = nx.Graph()
    G.add_edge(1, 7, weight=1)
    G.add_edge(2, 7, weight=2)
    G.add_edge(3, 7, weight=3)
    G.add_edge(4, 7, weight=4)
    G.add_edge(5, 7, weight=5)
    G.add_edge(6, 7, weight=6)
    G.add_edge(7, 7, weight=7)
    G.add_edge(8, 7, weight=8)

    assert_edges_equal(nx.max_weight_matching(G),
                       matching_dict_to_set({8: 7}))


def test3():
    G = nx.Graph()
    G.add_edge(1, 8, weight=9)
    G.add_edge(1, 12, weight=13)
    G.add_edge(2, 8, weight=10)
    G.add_edge(3, 9, weight=12)
    G.add_edge(4, 10, weight=14)
    G.add_edge(4, 13, weight=17)
    G.add_edge(5, 14, weight=19)
    G.add_edge(6, 11, weight=17)
    G.add_edge(7, 12, weight=19)

    assert_edges_equal(nx.max_weight_matching(G),
                       matching_dict_to_set({12: 7, 4: 13, 9: 3, 5: 14, 11: 6, 8: 2}))


if __name__ == '__main__':
    test1()
    test2()
    test3()

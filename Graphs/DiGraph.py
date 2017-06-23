"""
Brian Taylor Vann
github.com/taylor-vann

Description:
- Graph data structure

Requirements:
- GraphNode.py


create graph from dictionary

{
    "A": {
            "data": "something here"
            "edges": {
                        "B": {
                            "weight": 10
                            "data": None
                     }
        }
    "B": {
            "edges": {
                        "A": {
                            "weight": 10
                            "data": None
                     }
}
"""

from GraphNode import GraphNode
from PriorityQueue import PriorityQueue

class DiGraph (object):

    _g = None

    # overridden
    def __init__(self):
        self._g = {}


    def __contains__(self, n):
        if n in self._g:
            return True

        return False


    # custom methods
    def create_nodes(self, *args):
        for a in args:
            if a not in self._g:
                self._g[a] = {"edges": {}}


    def remove_nodes(self, *args):
        for a in args:
            self._g.pop(a, None)


    def set_node_properties(self, n, **kwargs):
        if n in self._g:
            for k in kwargs:
                if k != "edges":
                    self._g[n][k] = kwargs[k]


    def get_node_property(self, n, p):
        if n in self._g:
            if p in self._g[n]:
                return self._g[n][p]


    def create_edges(self, n, *args):
        if n in self._g:
            for a in args:
                if a in self._g:
                    self._g[n]["edges"][a] = {}


    def remove_edges(self, n, *args):
        if n in self._g:
            for a in args:
                if a in self._g:
                    self._g[n]["edges"].pop(a, None)


    def set_edge_properties(self, n, d, **kwargs):
        if n in self._g and d in self._g:
            if d in self._g[n]["edges"]:
                for k in kwargs:
                    self._g[n]["edges"][d][k] = kwargs[k]


    def get_edge_property(self, n, d, p):
        if n in self._g:
            if d in self._g[n]["edges"]:
                if p in self._g[n]["edges"][d]:
                    return self._g[n]["edges"][d][p]



    def has_edge(self, n, d):
        if n in self._g and d in self._g:
            if d in self._g[n]["edges"]:
                return True


    def dfs(self, n):
        if n not in self._g:
            return

        v = {}
        o = []
        q = [n]

        while q:
            c = q.pop()

            if c not in v:
                v[c] = None
                o.append(c)
                q.extend(reversed(sorted(self._g[c]["edges"].keys())))

        return o


    def bfs(self, n):
        if n not in self._g:
            return

        v = {}
        o = []
        q = [n]

        while q:
            c = q.pop(0)

            if c not in v:
                v[c] = None
                o.append(c)
                q.extend(sorted(self._g[c]["edges"].keys()))

        return o


    def dijkstra(self, n):
        if n not in self._g:
            return

        pq = PriorityQueue()
        m = []

        for k in self._g.keys():
            pq.push(k, float("inf"), parent = None)

        pq.remove(n)
        pq.push(n, 0)

        while len(pq) > 0:
            c = pq.pop()
            e = self._g[c["data"]]["edges"]

            for v in e:
                p = pq.remove(v)

                if e[v]["weight"] < p["weight"]:
                    p["parent"] = c["data"]
                    p["weight"] = e[v]["weight"] + c["weight"]
                    pq.push(p["data"], p["weight"], parent = p["parent"])

            m.append(c)

        return m


    def make_graph_from_acyclic(self, m):
        g = DiGraph()
        v = m.pop(0)

        g.create_nodes(v["data"])

        p = self._g[v["data"]]

        for k in p:
            if k != "edges":
                g.set_node_properties(k, k[p])

        while m:
            v = m.pop()



    def circuit(self):
        pass
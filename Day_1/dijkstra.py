# -*- coding: utf-8 -*-

__author__ = "GHajba"
__copyright__ = "Copyright 2016, JaPy Szoftver Kft"
__license__ = 'MIT'


def dijkstra(graph, source, target=None):
    """
        Dijkstra's algorithm to find the shortest path between source and target in a graph where each edge has a weight of 1
        If the target is provided, we finish searching / calculation if we encounter the target vertex.
    """
    dist = {}
    prev = {}
    visited = set()
    for v in graph:
        dist[v] = float('inf')
        prev[v] = None
    dist[source] = 0

    while sum(1 for k, v in dist.items() if k not in visited and v < float('inf')):
        sorted_x = [v for v in sorted(dist, key=dist.get) if v not in visited]
        u = sorted_x[0]
        if u in visited: continue
        visited.add(u)
        if u == target: break
        for v in graph[u]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev
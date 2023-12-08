import heapq

def dijkstra(graph, start, end):
    # Priority queue to store nodes with their tentative distances
    priority_queue = [(0, start)]
    
    # Dictionary to store tentative distances
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    while priority_queue:
        # Get the node with the smallest tentative distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if the node has already been visited
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances[end]

# Example input
input_graph = {
    (2, 1): [((3, 1), 1), ((2, 2), 2)],
    (3, 1): [((2, 1), 1), ((4, 1), 1)],
    (4, 1): [((3, 1), 1), ((5, 1), 1)],
}

# Example usage
source_node = (2, 1)
destination_node = (5, 1)

shortest_distance = dijkstra(input_graph, source_node, destination_node)
print(f"The shortest distance from {source_node} to {destination_node} is: {shortest_distance}")

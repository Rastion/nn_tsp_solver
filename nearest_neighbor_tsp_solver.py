from qubots.base_optimizer import BaseOptimizer

class NearestNeighborTSPSolver(BaseOptimizer):
    """
    Nearest Neighbor TSP Solver.
    
    This optimizer uses the nearest neighbor heuristic to construct an initial tour
    for the Traveling Salesman Problem (TSP). It begins at a specified start city (default is 0)
    and iteratively visits the nearest unvisited city until all cities have been visited.
    """
    def __init__(self, start_city=0):
        self.start_city = start_city

    def optimize(self, problem, initial_solution=None, **kwargs):
        # Generate a tour using the nearest neighbor heuristic.
        tour = self.nearest_neighbor_solution(problem)
        cost = problem.evaluate_solution(tour)
        return tour, cost

    def nearest_neighbor_solution(self, problem):
        """Generate initial tour using the nearest neighbor heuristic."""
        n = problem.nb_cities
        dist_matrix = problem.dist_matrix
        start = self.start_city
        tour = [start]
        unvisited = set(range(n))
        unvisited.remove(start)
        current_city = start
        while unvisited:
            next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
            tour.append(next_city)
            unvisited.remove(next_city)
            current_city = next_city
        # Optionally, you can return to the starting city:
        # tour.append(start)
        return tour

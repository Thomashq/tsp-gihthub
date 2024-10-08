import time

from algorithms.simulated_annealing import SimulatedAnnealing
from file_management.TSPFileReader import TSPFileReader
from file_management.SolutionReader import BestSolutionReader
from models.traveling_salesman import TravelingSalesman


class TSPSolver:
    def __init__(self, cities):
        self.tsp = TravelingSalesman(cities)

    def solve_with_simulated_annealing(self):
        simulated_annealing = SimulatedAnnealing(self.tsp)
        return simulated_annealing.optimize()

    def compare_solutions(self, tour, best_solution):
        return tour == best_solution


def print_menu():
    print("Escolha o algoritmo para resolver o problema do Caixeiro Viajante:")
    print("0 - Sair")
    print("1 - Têmpera Simulada")


def main():
    archive_name = "distance.txt"
    best_solution_file_name = "best_solution.txt"

    dist_reader = TSPFileReader(archive_name)
    dist_reader.read_file()

    best_solution_reader = BestSolutionReader(best_solution_file_name)
    best_solution_reader.read_file()
    best_solution = best_solution_reader.get_best_solution()

    solver = TSPSolver(dist_reader.get_dist_mat())

    while True:
        print_menu()
        choice = input("Digite a sua escolha: ")

        if choice == "1":
            print("Têmpera Simulada:")
            start_time = time.time()
            tour, dist = solver.solve_with_simulated_annealing()
            end_time = time.time()
            elapsed_time = end_time - start_time
            is_equal = solver.compare_solutions(tour, best_solution)
            print("Melhor rota:", tour)
            print("Distância:", dist)
            print(f"Tempo gasto: {elapsed_time:.2f} segundos")
            print("Solução Ótima:", best_solution)
            print("As soluções são iguais?" if is_equal else "As soluções são diferentes.")

        elif choice == "0":
            break

        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()

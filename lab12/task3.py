import random
import math

# -------------------------------
# Generate random sensor coordinates
# -------------------------------
def generate_sensors(n, width=100, height=100):
    return [(random.uniform(0, width), random.uniform(0, height)) for _ in range(n)]

# -------------------------------
# Distance functions
# -------------------------------
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def total_distance(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) + distance(route[-1], route[0])

# -------------------------------
# Random route
# -------------------------------
def random_route(sensors):
    route = sensors[:]
    random.shuffle(route)
    return route

# -------------------------------
# Genetic Algorithm
# -------------------------------
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end] = parent1[start:end]
    ptr = 0
    for gene in parent2:
        if gene not in child:
            while child[ptr] is not None:
                ptr += 1
            child[ptr] = gene
    return child

def mutate(route, mutation_rate=0.1):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]

def genetic_algorithm(sensors, population_size=50, generations=100, mutation_rate=0.05):
    population = [random_route(sensors) for _ in range(population_size)]
    for gen in range(generations):
        population.sort(key=total_distance)
        next_gen = population[:5]  # keep top 5
        while len(next_gen) < population_size:
            p1, p2 = random.sample(population[:20], 2)
            child = crossover(p1, p2)
            mutate(child, mutation_rate)
            next_gen.append(child)
        population = next_gen
    return min(population, key=total_distance)

# -------------------------------
# Main execution
# -------------------------------
num_sensors = 10
sensors = generate_sensors(num_sensors)

# Random route
random_r = random_route(sensors)

# GA optimized route
optimized_r = genetic_algorithm(sensors)

print("Random route distance:  {:.2f}".format(total_distance(random_r)))
print("GA optimized route distance: {:.2f}".format(total_distance(optimized_r)))

print("\nRandom route coordinates:")
for s in random_r:
    print(s)

print("\nGA optimized route coordinates:")
for s in optimized_r:
    print(s)

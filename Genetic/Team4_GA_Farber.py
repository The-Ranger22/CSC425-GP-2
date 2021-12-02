import random
from random import choice
from string import ascii_letters, punctuation, digits

GENERATIONS = 100

GOAL = "Machine Learning is fun!"

CHROMOSOMES = []
MATCH = False


# Step 1: generate alleles randomly
def get_nucleotides():
    # library of characters for a random selection
    NUCLEOTIDES = ascii_letters + punctuation + digits
    base = random.choice(NUCLEOTIDES)
    return base


def genetic_code():
    # create a string of random bases the same length as the GOAL code
    strand_len = len(GOAL)
    # print(f"strand_len = {strand_len}")
    chromosome = "".join(get_nucleotides() for _ in range(strand_len))
    return chromosome


def fitness_test(chromosome):
    # test the random built string for how well it matches the GOAL
    difference = 0
    for base, pos in zip(chromosome, GOAL):
        if base != pos:
            difference += 1
    fitness = len(GOAL) - difference
    return fitness


def reproduction(chromosome, fitness):
    rank = 0

    fitness_probability = fitness / (len(GOAL))
    print(fitness_probability)
    if fitness_probability == 1: MATCH = True
    # elif fitness_probability <= 0.25:


if __name__ == '__main__':
    epoch = 1
    print(f"{GOAL:>42}")
    parent = []
    for _ in range(GENERATIONS):
        chromosome = genetic_code()
        fitness = fitness_test(chromosome)
        parent = {
            "chromosome": chromosome,
            "fitness": fitness
        }
        # print(type(parent))
        CHROMOSOMES.extend(parent)

        # print(f"epoch {epoch:3}\t[chromosome:{chromosome}\tfitness:{fitness_test(chromosome)}]")
        # epoch += 1

    # print(type(CHROMOSOMES))

    print(sorted(CHROMOSOMES, key=lambda parent: parent[1]))


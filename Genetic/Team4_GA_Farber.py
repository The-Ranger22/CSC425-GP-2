import copy
import random
from string import ascii_letters, punctuation, digits
from operator import itemgetter

GENERATIONS = 100

GOAL = "Machine Learning is fun!"

CHROMOSOMES = []
MATCH = False
RESULT = []


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


def reproduction(gene_pool):
    rank = 0
    next_generation = []
    splitPairs = []

    for genes in gene_pool:
        fitness_probability = genes["fitness"] / (len(GOAL))
        # print(fitness_probability)
        if fitness_probability == 1:
            MATCH = True
            RESULT.append(genes)
            break
        elif fitness_probability >= 0.90:
            next_generation.append(genes)
        else:
            splitPairs.append(genes)


    for _ in range (len(splitPairs)):
        gamete1 = random.choice(splitPairs[:50])
        gamete2 = random.choice(splitPairs[:50])
        diploid = recombination(gamete1, gamete2)


def recombination(gamete1, gamete2):
    #TODO perform crossover and mutation based on random
    pass




if __name__ == '__main__':
    epoch = 1
    print(f"{GOAL:>42}")
    parent = {}
    for _ in range(GENERATIONS):
        chromosome = genetic_code()
        fitness = fitness_test(chromosome)
        parent['chromosome'] = chromosome
        parent['fitness'] = fitness
        CHROMOSOMES.append(copy.deepcopy(parent))

    while not MATCH:
        gene_pool = sorted(CHROMOSOMES, key=itemgetter('fitness'))
        reproduction(gene_pool)




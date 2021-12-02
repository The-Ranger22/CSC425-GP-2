import copy
import random
from string import ascii_letters, punctuation, digits
from operator import itemgetter

GENERATIONS = 100

GOAL = "Machine Learning is fun!"
STRAND_LEN = len(GOAL)

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
    chromosome = "".join(get_nucleotides() for _ in range(STRAND_LEN))
    return chromosome


def fitness_test(chromosome):
    # test the random built string for how well it matches the GOAL
    difference = 0
    for base, pos in zip(chromosome, GOAL):
        if base != pos:
            difference += 1
    fitness = len(GOAL) - difference
    return fitness

def get_parent():
    parent = {}
    for _ in range(GENERATIONS):
        chromosome = genetic_code()
        fitness = fitness_test(chromosome)
        parent['chromosome'] = chromosome
        parent['fitness'] = fitness
        CHROMOSOMES.append(copy.deepcopy(parent))
    return CHROMOSOMES


def reproduction(gene_pool):
    rank = 0
    next_generation = []
    splitPairs = []
    TEMP = []

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



    def recombination(gamete1, gamete2):
        # num of loop iterations is controlled by length of chromosome in gene pool *** should stay in GOAL length
        crossORmutate = random.uniform(0, 1)
        offspring = []

        for gene1, gene2 in zip(gamete1["chromosome"], gamete2["chromosome"]):
            # print(f"{gene1}\t{gene2}")
            if crossORmutate < .45:
                offspring.append(gene1)
            elif crossORmutate < .9:
                offspring.append(gene2)
            else:
                offspring.append(get_nucleotides())

        f1_chromosome = "".join(genes for genes in offspring)

        return f1_chromosome

    def get_nextGen(gamete1, gamete2):
        parent = {}
        for _ in range(off_size):
            chromosome = recombination(gamete1, gamete2)
            fitness = fitness_test(chromosome)
            parent['chromosome'] = chromosome
            parent['fitness'] = fitness
            TEMP.append(copy.deepcopy(parent))
        return TEMP

    off_size = len(splitPairs)
    for _ in range(off_size):
        gamete1 = random.choice(splitPairs[:50])
        gamete2 = random.choice(splitPairs[:50])
        get_nextGen(gamete1, gamete2)

    #TODO clear global CHROMOSOME to replace with next_generation and recombination chromosomes
    #TODO append the two lists of dicts into the empty CHROMOSOME


if __name__ == '__main__':
    epoch = 1
    print(f"{GOAL:>42}")
    # TODO sort out flow of driver and document methods
    get_parent()
    # parent = {}
    # for _ in range(GENERATIONS):
    #     chromosome = genetic_code()
    #     fitness = fitness_test(chromosome)
    #     parent['chromosome'] = chromosome
    #     parent['fitness'] = fitness
    #     CHROMOSOMES.append(copy.deepcopy(parent))

    gene_pool = sorted(CHROMOSOMES, key=itemgetter('fitness'))
    reproduction(gene_pool)

    # while not MATCH:
    #     gene_pool = sorted(CHROMOSOMES, key=itemgetter('fitness'))
    #     reproduction(gene_pool)

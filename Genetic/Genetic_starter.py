'''
CSC 425 Artificial Intelligence

Example code for genetic algorithm

Dr. Junxiu Zhou
Fall 2021

TF notes: If I understand the flow of the program below, we have a working code "sequential search" as a target goal.
We use the working code as a pool for chromosomes to be pulled from. The chromosomes are snippets of the target code
and we will strive to pass them through some fitness tests and "genetic" processes in order to come out the other side
with the text in all the right order to be the sequential search code.
'''

import sys
import random

TARGET = """def linear_search(values, seeking):
   pos = 0
   found = False
   while pos < len(values) and found is False:
      if values[pos] == seeking:
         found = True
      else:
         pos += 1
   return found"""
TARGET_LEN = len(TARGET)
MATCH = []
# print(f"length {TARGET_LEN}")
# print(TARGET)
# parents array
codes = []

# code piece for sequential search (you can change it to other code if you want)
## The target code is a complete method but it is a block of text here, providing its own gene pool
## genepool has intentional erros < to >, = to !
genepool = """def linear_search(values, seeking):
   pos = 0
   found = False
   while pos > len(values) and found is False:
      if values[pos] != seeking:
         found = True
      else:
         pos += 1
   return found"""

# use your own strategies to generate initial code pieces as the parents
## separates block of text into lines
def get_gene(genepool):
    gene = genepool.split('\n')
    return gene

## adds multiples of lines to a chromosome for population
def get_chromosome(genepool, len):
    population = []
    for _ in range(len // 10):
        chromosome = [get_gene(genepool) for items in range(len)]
        population.append(chromosome)
    return population

codes = get_chromosome(genepool, TARGET_LEN)
## note to help me remember the levels of lists in lists
## codes has 21 lists of 10 lists of chromosomes; codes[0] has 211 lists of 1 chromosome each;
## codes[0][0] has 1 chromosome with 9 lines of text

# here I just randomly add three original code pieces as the parents seed (Selfing breeding.....)
# codes.append(genepool)
# codes.append(genepool)
# codes.append(genepool)
# print(codes)
# exec(code)
# you can use your own test array list
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# try:
#    print(sequentialSearch(testlist, 13))
# except:
#    print("Unexpected error:", sys.exc_info()[0])

# number of offsprings, you can change it according to your preferences
offs_per_pop = 6
# step size to stop the code for running infinite loops, you can change it according to your preferences
steps = 10


# cross-over instructions  (e.g., two arithmetic expressions, you can change + to *)
def crossover(codes):
    # cross over parts of code_temp
    code_temp = ["<" if item == ">" else item for item in codes]
    # print(codes[0])

    # code_temp = ["True1" if item == "True" else item for item in code_temp]
    return code_temp


# mutate the code (e.g., change the order of the instructions in the code. As the code is ordered line by line,
# you can use a line of code as the mutate target)
def mutate(code_temp):
    # mutate parts of the code_temp
    code_temp[0] = ["=" if item == "!" else item for item in code_temp]
    return code_temp


## The fitness code was preventing the program from moving forward. I changed it to comparing text and scoring it.
def tf_fitness(active_codes, TARGET):
    ## normalizing allows us to compare the TARGET to the evolving code at the line level instead of by character
    ## passing a length of 10 to the get_chromosome call returns just a single chromosome for TARGET
    normalize = get_chromosome(TARGET, 10)
    score = 0
    score_list = []
    pos = 0
    chromosome_score = []

    for _ in range(len(active_codes)-1):
        for it1, it2 in zip(active_codes[pos][0], normalize[0][0]):
            # print(f"codes[it1]_{pos}_: {it1}\nTarget[it2]_0_: {it2}")
            if it1 == it2:
                score += 1
        chromosome_score = [score] + [active_codes[pos][0]]
        score_list.extend([chromosome_score])
        if score == 9:
            print("Possible result found!")
            MATCH = [active_codes[pos][0]]
            break
        score = 0
        pos += 1

    return score_list

# def fitness(code_temp, TARGET):
#     normalize = get_chromosome(TARGET, 10)
#     score = 0
#     pos = 0
#     for it1, it2 in zip(code_temp[0][pos], normalize[0][pos]):
#         print(f"codes[it1]:{it1}\nTarget[it2]: {it2}")
#         if it1 == it2:
#             score += 1
#         pos += 1
#     # fitness_value = 1 / score
#     print(score)
#     # return fitness_value
#
#     # score = 0
#     # # you can use your own test array list
#     # testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
#     # #exec(code_temp);
#     # #test example
#     # # as we may have "malformed" offspring, we use try clause to keep program runnning without stop the program
#     # try:
#     #     if(sequentialSearch(testlist, 13) == True):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 130) == False):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 19) == True):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 42) == True):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 81) == False):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 17) == True):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 14) == False):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 1) == True):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 420) == False):
#     #         score += 1
#     #     if(sequentialSearch(testlist, 0) == True):
#     #         score += 1
#     # except:
#     #     print("Unexpected error:", sys.exc_info())
#     #     score = -1
#     return score


# test if the program fulfills the requirements, you can change it accordingly your preferences
def satisfied(test_match):
    match = test_match
    original_code = ""
    original_code = "\n".join(match[0])
    # print(original_code)
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

    exec(original_code);
    try:
        if(linear_search(testlist, 32) == True):
            print("Found the right code! Exit~!")
            return True
            exit()
    except:
        print("Unexpected error:", sys.exc_info())
        return False

   #  original_code = """def linear_search(values, seeking):
   # pos = 0
   # found = False
   # while pos < len(values) and found is False:
   #    if values[pos] == seeking:
   #       found = True
   #    else:
   #       pos += 1
   # return found"""
   #  for str_code in codes:
   #      if (str_code == original_code):
   #          print("Found the right code! Exit~!")
   #          return True
    return False

offspring = []
index = 0
# run until find the target
while len(MATCH) == 0 and index < steps:
    # generate offsprings
    index += 1
    offspring = []
    index1 = 0
    while len(offspring) < offs_per_pop and index1 < steps:
        index1 += 1
        population_w_scores = []
        population_w_scores.append([tf_fitness(codes, TARGET)])
        if len(MATCH) != 0:
            isMatch = satisfied(MATCH)
        temp_test = population_w_scores[0][0][0]
        score = temp_test[0]
        if score > 5:
            offspring.extend(temp_test[1])
        code_temp = []
        code_temp = crossover(offspring)
        code_temp = mutate(code_temp)
    # substitute the new generation as the parents
    if len(offspring) > 0:
        codes = offspring


        #
        # code_temp = crossover(offspring)
        # code_temp = mutate(code_temp)
        # code_temp = str(code_temp)
        # exec(code_temp)
        # if (fitness(code_temp, TARGET) > 5):
        #     offspring.append(code_temp)




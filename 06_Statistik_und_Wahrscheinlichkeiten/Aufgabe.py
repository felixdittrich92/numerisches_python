from random import randint
import numpy as np
from collections import Counter
from pprint import pprint
import time

# Aufgaben Siehe Buch
print('-------------Aufgabe 1-------------')

outcomes = [ randint(1,6) for _ in range(10000)]
even_pips = [ x for x in outcomes if x % 2 == 0]
greater_two = [ x for x in outcomes if x > 2]
combined = [ x for x in outcomes if x % 2 == 0 and x > 2]
print(len(even_pips)/len(outcomes))
print(len(greater_two)/len(outcomes))
print(len(combined)/len(outcomes))

print('-------------Aufgabe 2-------------')

def find_interval(x, partition):
    """ find_interval -> i
        "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise
        """
    
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1
    return -1

def weighted_choice(sequence, weights, bisection=False):
    """ 
    weighted_choice selects a random element of 
    the sequence according to the weights list
    """
    x = np.random.random()
    w = [0] + list(np.cumsum(weights))
    index = find_interval(x, w)
    return sequence[index]

def process_datafile(filename):
    """ process_datafile -> (universities,enrollments,total_number_of_students)
    universities: list of University 
    namesenrollments: corresponding list with enrollments
    total_number_of_students: over all universities"""
    universities=[]
    enrollments=[]
    with open(filename) as fh:
        total_number_of_students= 0
        fh.readline()# get rid of descriptive first line
        for line in fh:
            line=line.strip()
            *praefix, under, post, total = line.rsplit()
            university = praefix[1:]
            total = int(total.replace(",",""))
            enrollments.append(total)
            universities.append(" ".join(university))
            total_number_of_students += total
    return(universities, enrollments, total_number_of_students)

universities, enrollments, total_students = process_datafile("universities_uk.txt")

"""
for i in range(14):
    print(universities[i], end=": ")
    print(enrollments[i])

print("Number of students enrolled in the UK: ", total_students)
"""
normalized_enrollments = [students / total_students for students in enrollments]
print(weighted_choice(universities, normalized_enrollments))

outcomes=[] 
n= 100000
for i in range(n):
    outcomes.append(weighted_choice(universities,normalized_enrollments))

c = Counter(outcomes)
pprint(c.most_common(20),indent=2, width=70)

print('-------------Aufgabe 3-------------')

def find_interval(x, 
                  partition, 
                  endpoints=True):
    """ find_interval -> i
        If endpoints is True, "i" will be the index for which applies
        partition[i] < x < partition[i+1], if such an index exists.
        -1 otherwise
        
        If endpoints is False, "i" will be the smallest index 
        for which applies x < partition[i]. If no such index exists 
        "i" will be set to len(partition)
    """
    for i in range(0, len(partition)):
        if x < partition[i]:
            return i-1 if endpoints else i
    return -1 if endpoints else len(partition)


def weighted_choice(sequence, weights):
    """ 
    weighted_choice selects a random element of 
    the sequence according to the list of weights
    """
    x = np.random.random()
    cum_weights = [0] + list(np.cumsum(weights))
    index = find_interval(x, cum_weights)
    return sequence[index]

def cartesian_choice(*iterables):
    """
    A list with random choices from each iterable of iterables 
    is being created in respective order.
    
    The result list can be seen as an element of the 
    Cartesian product of the iterables 
    """
    res = []
    for population in iterables:
        res.append(random.choice(population))
    return res



def weighted_cartesian_choice(*iterables):
    """
    A list with weighted random choices from each iterable of iterables 
    is being created in respective order
    """
    res = []
    for population, weights in iterables:
        lst = weighted_choice(population, weights)
        res.append(lst)
    return res


def weighted_sample(population, weights, k):
    """ 
    This function draws a random sample of length k 
    from the sequence 'population' according to the 
    list of weights
    """
    sample = set()
    population = list(population)
    weights = list(weights)
    while len(sample) < k:
        choice = weighted_sample(population, weights)
        sample.add(choice)
        index = population.index(choice)
        weights.pop(index)
        population.remove(choice)
        weights = [ x / sum(weights) for x in weights]
    return list(sample)


def weighted_sample_alternative(population, weights, k):
    """ 
    Alternative way to previous implementation.

    This function draws a random sample of length k 
    from the sequence 'population' according to the 
    list of weights
    """
    sample = set()
    population = list(population)
    weights = list(weights)
    while len(sample) < k:
        choice = weighted_sample(population, weights)
        if choice not in sample:
            sample.add(choice)
    return list(sample)

amazons = ["Airla","Barbara","Eos",
           "Glykeria","Hanna","Helen",
           "Agathangelos","Iokaste","Medousa",
           "Sofronia","Andromeda"]

weights = np.full(11,1/len(amazons))
Pytheusses_favorites = {"Iokaste","Medousa","Sofronia","Andromeda"}

n = 1000 
counter = 0

prob= 1 / 330
days = 0
factor1 = 1 / 13
factor2 = 1 / 12

start = time.perf_counter()
while prob < 0.9:
    for i in range(n):
        the_chosen_ones = weighted_sample_alternative(amazons, weights, 4)

        if set(the_chosen_ones) == Pytheusses_favorites:
            counter += 1 

    prob = counter / n 
    counter = 0
    weights[:7] = weights[:7] - weights[:7] * factor1
    weights[7:] = weights[7:] + weights[7:] * factor2
    weights = weights / np.sum(weights)
    #print(weights)
    days += 1

print(time.perf_counter() - start)
print("Number of days, he has to wait: ", days)
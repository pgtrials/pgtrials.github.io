"""
Given: Three positive integers k, m and n; representing a population containing k+m+n organisms:
 k individuals are homozygous dominant for a factor
 m are heterozygous
 n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing
a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

def MendelsFirstLaw(k, m, n):
    # calculate the probability of recessive traits only
    total = k + m + n
    recessive = (n/total)*((n-1)/(total-1))
    hetro = (m/total)*((m-1)/(total-1))
    heteroRecess = (n/total)*(n/(total-1)) + (m/total)*(n/(total-1))

    # probability of recessive
    recessProb = recessive + hetro*1/4 + heteroRecess*1/2
    dominantProb = 1-recessProb
    return dominantProb  # take the complement for probability of dominant trait

"""
# Example usage:
k = 2  # Number of homozygous dominant individuals
m = 2  # Number of heterozygous individuals
n = 2  # Number of homozygous recessive individuals

result = MendelsFirstLaw(k, m, n)
print("Probability of producing an individual with a dominant allele:", result)
 """

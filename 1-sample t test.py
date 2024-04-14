import random
import math
from scipy.stats import t

sample = []

sampleSize = 100

sum = 0

#population data
populationMean = 200
populationSD = 30
#signifanceLevel
sigLevel = 0.05

#randomly assigns weight to the men and places their weights in a list
for i in range(0, sampleSize + 1):
    weightOfMan = random.randrange(145, 225)
    sample.append(weightOfMan)
    sum += weightOfMan

#The sample mean is calculated(x_bar)
sampleMean = int(sum/sampleSize)

#used to calculate SD(sum of x_index - x_mean)
sumPointminusMean = 0
for weight in sample:
    sumPointminusMean += math.pow(weight-sampleMean, 2)

#rest of SD formula
sampleSD = int(math.sqrt(sumPointminusMean/sampleSize))

#standard error
standardError = sampleSD/math.sqrt(sampleSize)

degFreedom = sampleSize-1

#p-value calculation

pVal = 0
tStatistic = float((sampleMean-populationMean)/standardError)

xTailedTest = input("Is this A) one-tailed or B) two-tailed test: ")

if xTailedTest.upper() == "A":
    if sampleMean < populationMean:
        pVal = t.cdf(x = tStatistic, df= degFreedom)
    elif sampleMean > populationMean:
        pVal = 1 - (t.cdf(x=tStatistic, df=degFreedom))

elif xTailedTest.upper() == "B":
    if sampleMean < populationMean:
        pVal = 2 * t.cdf(x = tStatistic, df = degFreedom)
    else:
        pVal = 2 * (1 - (t.cdf(x = tStatistic, df = degFreedom)))
else:
    print("Please enter a valid response")
    


#list of subjects' weight
print("Sample:", sample)

print("Null Hypothesis(H0): μx = 200")
print("Alternative Hypothesis(Ha): μx != 200")

print("Sample Mean:", sampleMean)

print("Sample Standard deviation:", sampleSD)

print("Standard Error", standardError)

print("Degrees of freedom:", degFreedom)

print("t-statistic:", tStatistic)
print("P-value", pVal)

if pVal < sigLevel:
    print("We reject the null hypothesis. We have sufficient evidence supporting the alternative hypothesis")
elif pVal > sigLevel:
    print("We fail to reject the null hypothesis. We have insufficient evidence supporting the alternative")
else:
    # if pVal = sigLevel
    print("retry the test")


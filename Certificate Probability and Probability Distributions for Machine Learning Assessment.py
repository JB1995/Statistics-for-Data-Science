import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Binomial Distribution Example:
success=0.6
sample = np.arange(0,8)
print(sample)

binomial = stats.binom.pmf(sample, 7, success)
print(binomial)

plt.plot(sample, binomial, 'o-')
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")
plt.title("Binomial Distribution: n=%i, p=%.2f" % (len(sample)-1, success))
plt.show()

# Poisson Distribution Example:
lambda_ = 6
sample=np.arange(0,20)
print(sample)

poisson = stats.poisson.pmf(sample, lambda_)
print(poisson)

print(1 - poisson[0] - poisson[1] - poisson[2] - poisson[3])

plt.plot(sample, poisson, 'o-')
plt.xlabel("Number of Successes")
plt.ylabel("Probability of Successes")
plt.title("Poisson Distribution: \lambda = %i" % lambda_)
plt.show()

# Normal Distribution Example:
print(stats.norm.cdf(0.280, loc=0.295, scale=0.025))
print(1- stats.norm.cdf(0.350, loc=0.295, scale=0.025))
print(stats.norm.cdf(0.340, loc=0.295, scale=0.025)-stats.norm.cdf(0.260, loc=0.295, scale=0.025))
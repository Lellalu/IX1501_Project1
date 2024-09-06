import numpy as np
import scipy

# Calculate the win probability of n trails by binomial distribution
def calc_prob_list(n):
  real_prob = 0.010677083333333334 # The exact value we got in task 2
  prob_list = []
  for i in range(n+1):
    prob_list.append((real_prob**i*(1-real_prob)**(n-i))*scipy.special.comb(n, i))
  return prob_list

real_prob = 0.010677083333333334
# Search for minimum trails within relative value from (10000 to 20000)
for i in range(11600, 20000):
  # Get the probability list of i trails
  prob_list = calc_prob_list(i)
  # Get highest value in the prob list
  most_probable_prob = np.argmax(prob_list)/i 
  # Calculate the relative error value of the current trail set
  err_value = abs(most_probable_prob-real_prob)/real_prob
  print(err_value)
  # If the relative error is less than 0.1, we print it out and break the loop
  if err_value <= 0.1:
    print(i)
    break
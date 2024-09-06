import numpy as np
import scipy

def calc_prob_list(n):
  real_prob = 0.010677083333333334
  prob_list = []
  for i in range(n+1):
    prob_list.append((real_prob**i*(1-real_prob)**(n-i))*scipy.special.comb(n, i))
  return prob_list

real_prob = 0.010677083333333334

for i in range(11600, 20000):
  prob_list = calc_prob_list(i)
  most_probable_prob = np.argmax(prob_list)/i
  err_value = abs(most_probable_prob-real_prob)/real_prob
  print(err_value)
  if err_value <= 0.1:
    print(i)
    break
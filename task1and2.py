import numpy as np
import pandas as pd

def sum_prob_discret_method(): 
    # Define probability of each face of each dice with various face numbers
    # Each face has the same probability within a dice
    p1 = [1/4]*4
    p2 = [1/6]*6
    p3 = [1/8]*8
    p4 = [1/12]*12
    p5 = [1/20]*20

    # Perform convolutions in loop
    convolution_sum = p1
    for p in [p2, p3, p4, p5]:
        convolution_sum = np.convolve(convolution_sum, p)

    # Create a table with sum(S) and responsive probabilities(P(S))
    s = np.arange(5, 51)
    table = pd.DataFrame({
    'S': s,
    'P(S = s)': convolution_sum
    })

    # Calculate the winning probability 
    # Get the sum of probabilities where S<=10 or S>=45
    winning_prob = 0
    for i in range(50-5+1):
        if i+5 <= 10 or i+5 >= 45:
            winning_prob += convolution_sum[i]
        else:
            continue  
    
    print(table.to_string(index=False))
    print(winning_prob)

sum_prob_discret_method()



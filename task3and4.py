import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def win_prob_Monte_Carlo_Simulation(trails):
    # Define faces of each dice 
    dice_faces = [4, 6, 8, 12, 20]

    wins = 0
    # Simulate each trail within the given n trails
    for _ in range(trails):
        sum = 0
        for face_no in dice_faces:
            # Calculate the sum of dice by picking up random num for each dice
            sum += np.random.randint(1, face_no + 1)             
        # Define the condition of win
        if sum <= 10 or sum >= 45:
            wins += 1
    # calculate the probability
    win_prob = wins/trails

    return win_prob 
    #print(win_prob)

def win_prob_Monte_Carlo_Simulation_increasing():
    # Giving increasing trail numbers
    trails=[10, 100, 1000, 10000, 100000, 1000000]

    probabilities = []
    # Compute probalties with increasing trail size
    for trail in trails:
        probabilities.append(win_prob_Monte_Carlo_Simulation(trail))

    # Plot the numbers in a figure
    plt.figure(figsize=(10, 6))
    plt.plot(trails, probabilities, marker='o', linestyle='-', color='r')
    plt.xscale('log') # log scale of x axis for better visualization
    plt.title('Simulation of Winning Probability')
    plt.xlabel('Number of Trials (log scale)')
    plt.ylabel('Winning Probability')
    plt.grid(True)
    plt.show()

win_prob_Monte_Carlo_Simulation(1000)
win_prob_Monte_Carlo_Simulation_increasing()
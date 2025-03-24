import numpy as np
import matplotlib.pyplot as plt

# Function to calculate statistics
def calculate_statistics(results):
    # Get average, min, max, and standard deviation for bingo and full-house
    bingo_stats = {
        'average': np.mean(results['bingo_winners'], axis=0),
        'min': np.min(results['bingo_winners'], axis=0),
        'max': np.max(results['bingo_winners'], axis=0),
        'std': np.std(results['bingo_winners'], axis=0),
    }
    full_house_stats = {
        'average': np.mean(results['full_house_winners'], axis=0),
        'min': np.min(results['full_house_winners'], axis=0),
        'max': np.max(results['full_house_winners'], axis=0),
        'std': np.std(results['full_house_winners'], axis=0),
    }
    return bingo_stats, full_house_stats

# Function that returns the graph plot
def plot_results(bingo_stats, full_house_stats, range_start, range_end):
    x = np.arange(range_start, range_end + 1)
    figure = plt.figure(figsize=(10, 6))
    
    # Plot for BINGO
    plt.fill_between(x, bingo_stats['average'] - bingo_stats['std'], bingo_stats['average'] + bingo_stats['std'], alpha=0.2)
    plt.plot(x, bingo_stats['average'], label='Average BINGO')
    plt.plot(x, bingo_stats['min'], linestyle='--', label='Min BINGO')
    plt.plot(x, bingo_stats['max'], linestyle='--', label='Max BINGO')
    
    # Plot for Full House
    plt.fill_between(x, full_house_stats['average'] - full_house_stats['std'], full_house_stats['average'] + full_house_stats['std'], alpha=0.2)
    plt.plot(x, full_house_stats['average'], label='Average Full-House')
    plt.plot(x, full_house_stats['min'], linestyle='--', label='Min Full-House')
    plt.plot(x, full_house_stats['max'], linestyle='--', label='Max Full-House')
    
    plt.xlabel('# Numbers Called')
    plt.ylabel('# Winners')
    plt.title('Simulation Result')
    plt.legend()
    return figure
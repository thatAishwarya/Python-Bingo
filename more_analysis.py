import numpy as np

# Function that performs more analysis - 25th percentile, median, 75th percentile
def additional_analytics(results, range_start, range_end):
    # Get a numpy array of random numbers within the specified range
    called_numbers = np.arange(range_start, range_end + 1)
    analytics_table = []
    
    # Here, i holds the index, num_called holds the element at the index while iterating
    for i, num_called in enumerate(called_numbers):
        # Get counts for each simulation at the given number
        bingo_winners_current = results['bingo_winners'][:, i]
        full_house_winners_current = results['full_house_winners'][:, i]

        # Calculate additional analytics using numpy functions
        median_bingo = np.median(bingo_winners_current)
        median_full_house = np.median(full_house_winners_current)
        percentile_25_bingo, percentile_75_bingo = np.percentile(bingo_winners_current, [25, 75])
        percentile_25_full_house, percentile_75_full_house = np.percentile(full_house_winners_current, [25, 75])
        
        # Append the analytics to the table
        analytics_table.append([num_called, median_bingo, percentile_25_bingo,percentile_75_bingo, median_full_house, percentile_25_full_house, percentile_75_full_house])

    # table headers
    headers = ["Number Called", "Median Bingo", "25th Percentile Bingo", "75th Percentile Bingo", "Median Full-House", "25th Percentile Full House", "75th Percentile Full House"]
    
    # return the header and the row data for table creation
    return headers, analytics_table
import random
import numpy as np

#Function that creates a bingo card
def get_random_bingo_card(n_rows, n_cols, start_range, end_range, n_free_cells):
    card = []

    # Get the range of numbers that should fill each column
    bingo_range = int((end_range - start_range + 1) / n_cols)

    # Iterate n_col times to get random numbers in each col
    for i in range(n_cols):
        # Use the calculated bingo_range to get upper and lower limit for each col 
        col_range_start = int(start_range + (i * bingo_range))
        col_range_end = int(start_range + ((i + 1) * bingo_range)) - 1

        # No of element in each col is equal to the no. of row, hence size = n_rows
        col = np.random.choice(range(col_range_start, col_range_end + 1), size=n_rows, replace=False)

        # Append the generated array to the card
        card.append(col)

    # Transpose the numpy array and 
    # Convert to list so we can store Free cell's string value
    card = np.array(card).T.tolist()

    # Set random n cells as 'free' cell
    for _ in range(n_free_cells):
        row_index = random.randint(0, n_rows - 1)
        col_index = random.randint(0, n_cols - 1)
        card[row_index][col_index] = "Free"

    return card

#Function that creates n different bingo cards
def get_n_bingo_cards(n_cards, n_rows, n_cols, start_range, end_range, n_free_cells):
    cards = [get_random_bingo_card(n_rows, n_cols, start_range, end_range, n_free_cells) for _ in range(n_cards)]
    return cards

#Function that checks bingo
def is_bingo(card, called_numbers):
    rows = len(card)
    cols = len(card[0])

    # Check rows
    for i in range(rows):
        if all(x in called_numbers or x == "Free" for x in card[i]):
            return True

    # Check columns
    for i in range(cols):
        if all(card[j][i] in called_numbers or card[j][i] == "Free" for j in range(rows)):
            return True

    # Check diagonals (only if the number of rows and columns are the same)
    if rows == cols:
        if all(card[i][i] in called_numbers or card[i][i] == "Free" for i in range(rows)):
            return True
        if all(card[i][cols - 1 - i] in called_numbers or card[i][cols - 1 - i] == "Free" for i in range(rows)):
            return True
        
    return False

# Function that checks full house
def is_full_house(card, called_numbers):
    for row in card:
        if not all(x in called_numbers or x == "Free" for x in row):
            return False
    return True

def run_simulations(cards, num_simulations=100, range_start_value=1, range_end_value=75):
    bingo_range = range_end_value - range_start_value + 1

    # List of numbers called within the range specified by user(Eg: 1 to 75)
    all_called_numbers = [random.sample(range(range_start_value, range_end_value + 1), bingo_range) for _ in range(num_simulations)]

    # Create a dictionary with keys(numpy array) to hold bingo counts and full house counts
    results = {
        'bingo_winners': np.zeros((num_simulations, bingo_range)),
        'full_house_winners': np.zeros((num_simulations, bingo_range)),
    }

    # For each simulation, check bingo and full house for called numbers
    for simulation in range(num_simulations):
        called_numbers = all_called_numbers[simulation]
        for numbers in range(bingo_range):
            # Bingo and Full House checks called for each card
            bingo_count = np.sum([is_bingo(card, called_numbers[:numbers + 1]) for card in cards])
            full_house_count = np.sum([is_full_house(card, called_numbers[:numbers + 1]) for card in cards])
            # Update the dictionary with the count
            results['bingo_winners'][simulation][numbers] = bingo_count
            results['full_house_winners'][simulation][numbers] = full_house_count

    return results
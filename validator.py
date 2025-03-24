# Function that validates user input
def validate_user_input(n_cards, n_simulations, n_row, n_column, range_start, range_end, n_free_cells):
    error_message = ""

    # Validate number of cards
    if not n_cards or not n_cards.isdigit():
        error_message += "Invalid number of cards \n"
        
    # Validate number of simulations
    if not n_simulations or not n_simulations.isdigit():
        error_message += "Invalid number of simulations \n"

    # Validate number of rows
    if not n_row or not n_row.isdigit():
        error_message += "Invalid number of rows \n"

    # Validate number of columns
    if not n_column or not n_column.isdigit():
        error_message += "Invalid number of columns \n"

    # Validate number of free cells
    if not n_free_cells or not n_free_cells.isdigit():
        error_message += "Invalid number of free cells \n"

    # Validate range
    if not range_start or not range_start.isdigit() or not range_end or not range_end.isdigit():
        error_message += "Invalid range \n"
    elif (int(range_start) >= int(range_end)):
        error_message += "Range start ({0}) should be less than range end ({1})\n".format(range_start,range_end)
    
    # Range entered should be atleast in the range of row * col, 
    # Eg for 5*5 matrix, valid range is 1 to 25, invalid range is 1 to 10
    # Also, Range start should be less than Range end. 
    if range_start and range_start.isdigit() and range_end and range_end.isdigit() and n_row and n_row.isdigit() and n_column and n_column:
        total_numbers = int(range_end) - int(range_start) + 1
        product_of_rows_columns = int(n_row) * int(n_column)
        if total_numbers < product_of_rows_columns and (int(range_start) < int(range_end)):
            error_message += "Total numbers ({0}) cannot be less than total cells ({1}) \n".format(total_numbers,product_of_rows_columns)
        
    # Free cells entered should not be more than row * col, 
    if n_free_cells and n_free_cells.isdigit() and n_row and n_row.isdigit() and n_column and n_column:
        product_of_rows_columns = int(n_row) * int(n_column)
        if int(n_free_cells) >= product_of_rows_columns:
            error_message += "Number of free cells ({0}) should be less than total cells ({1})\n".format(n_free_cells,product_of_rows_columns)

    return error_message

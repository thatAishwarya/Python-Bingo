import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style 
from ttkbootstrap.dialogs  import Messagebox
from ttkbootstrap.tableview import Tableview
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import bingo as bingo_helper
import graph as graph_helper
import validator as validation_helper
import downloads as download_helper
import more_analysis as analysis_helper
import sys

class BingoGUI:
    def __init__(self, app):
        app.title("Welcome to Bingo Analyser!")
        # Adds theme to the UI
        Style(theme="superhero")

        self.generated_cards = []
        self.analysis_result = []

        # container for home screen 
        self.home_frame = ttk.Label(app)

        # Home screen label 
        label = ttk.Label(self.home_frame, text="Bingo Setup")
        label.pack(pady=30)
        label.config(font=("Arial", 15, "bold"))

        # Label and input field for number of cards
        cards_frame = ttk.Frame(self.home_frame)
        cards_frame.pack(pady=15, padx=10, fill="x")
        ttk.Label(cards_frame, text="Number of cards", width=20).pack(side=LEFT, padx=5)
        self.n_cards = ttk.Entry(cards_frame)
        self.n_cards.pack(side=LEFT, fill="x", expand=True, padx=5)

        # Label and input field for number of simulations
        simulations_frame = ttk.Frame(self.home_frame)
        simulations_frame.pack(pady=15, padx=10, fill="x")
        ttk.Label(simulations_frame, text="Number of simulations", width=20).pack(side=LEFT, padx=5)
        self.n_simulations = ttk.Entry(simulations_frame)
        self.n_simulations.pack(side=LEFT, fill="x", expand=True, padx=5)

        # Label and input field for number of rows
        row_frame = ttk.Frame(self.home_frame)
        row_frame.pack(pady=15, padx=10, fill="x")
        ttk.Label(row_frame, text="Number of rows", width=20).pack(side=LEFT, padx=5,)
        self.n_row = ttk.Entry(row_frame)
        self.n_row.pack(side=LEFT, fill="x", expand=True, padx=5)

        # Label and input field for number of columns
        column_frame = ttk.Frame(self.home_frame)
        column_frame.pack(pady=15, padx=10, fill="x")
        ttk.Label(column_frame, text="Number of columns", width=20).pack(side=LEFT, padx=5)
        self.n_column = ttk.Entry(column_frame)
        self.n_column.pack(side=LEFT, fill="x", expand=True, padx=5)

        # Label and input field for number of free cells
        free_cells_frame = ttk.Frame(self.home_frame)
        free_cells_frame.pack(pady=15, padx=10, fill="x")
        ttk.Label(free_cells_frame, text="Number of free cells", width=20).pack(side=LEFT, padx=5)
        self.n_free_cells = ttk.Entry(free_cells_frame)
        self.n_free_cells.pack(side=LEFT, fill="x", expand=True, padx=5)

        # Label and input field for range of numbers in the bingo cards
        range_frame = ttk.Frame(self.home_frame)
        range_frame.pack(pady=15, padx=10, fill="x")
        ttk.Label(range_frame, text="Range", width=20).pack(side=LEFT, padx=5)
        self.range_start = ttk.Entry(range_frame)
        self.range_start.pack(side=LEFT, fill="x", expand=True, padx=5)
        ttk.Label(range_frame, text="to").pack(side=LEFT)
        self.range_end = ttk.Entry(range_frame)
        self.range_end.pack(side=LEFT, fill="x", expand=True, padx=5)

        # Home screen buttons
        home_screen_button_frame = ttk.Frame(self.home_frame)
        home_screen_button_frame.pack(pady=30, padx=10, fill="x")
        ttk.Button(home_screen_button_frame, text="Run Analysis",  bootstyle=SUCCESS, command=lambda: self.bingo_analyser()).pack(side=LEFT, padx=5)
        ttk.Button(home_screen_button_frame, text="Reset", bootstyle=SECONDARY, command=lambda: self.reset_form()).pack(side=LEFT, padx=5)
        ttk.Button(home_screen_button_frame, text="Exit", bootstyle=LIGHT, command=lambda: self.exit_application()).pack(side=LEFT, padx=5)
        
        # Analysis screen GUI starts here, create container
        self.analysis_frame = ttk.Label(app)

        # Add the buttons to Analysis screen
        result_screen_button_frame = ttk.Frame(self.analysis_frame)
        result_screen_button_frame.pack(pady=30, padx=10, fill="x")
        ttk.Button(result_screen_button_frame, text="Exit", bootstyle=LIGHT, command=lambda: self.exit_application()).pack(side=RIGHT, padx=5)
        ttk.Button(result_screen_button_frame, text="Back to home", bootstyle=SECONDARY, command=lambda: self.show_home_screen()).pack(side=RIGHT, padx=5)
        ttk.Button(result_screen_button_frame, text="More Analysis", bootstyle=DEFAULT, command=lambda: self.more_analysis()).pack(side=RIGHT, padx=5)
        ttk.Button(result_screen_button_frame, text="Download Cards", bootstyle=INFO, command=lambda: self.download_cards()).pack(side=RIGHT, padx=5)

        # Master frame for graph and table
        self.output_frame = ttk.Frame(self.analysis_frame)
        self.output_frame.pack()

        #Sets default values in input field of the form
        self.set_defaults()

    # Function to show home screen
    def show_home_screen(self):
        # Free the previous graph and table result
        self.table = None
        self.graph = None
        # Show home screen
        self.home_frame.pack()
        # Hide analysis screen
        self.analysis_frame.pack_forget()

    # Function to show analysis screen
    def show_analysis_screen(self):
        # Show analysis screen
        self.analysis_frame.pack()
        # Hide home screen
        self.home_frame.pack_forget()

    #Function to initialize output container
    def init_output_screen(self):
        # Clear the contents of output frame
        self.clear_frame(self.output_frame)

        # Add table container
        self.table_frame = ttk.Frame(self.output_frame)
        self.table_frame.pack(pady=15, padx=10, fill="x")

        # Add graph container
        self.graph_frame = ttk.Frame(self.output_frame)
        self.graph_frame.pack(pady=15, padx=10, fill="x")

    # Function to clear the contents of a UI frame
    def clear_frame(self, frame):
        for contents in frame.winfo_children():
            contents.destroy()
            
    # Function to reset the input fields
    def reset_form(self):
        #Iterate through all the input fields and delete the entry
        entries = [self.n_cards, self.n_simulations, self.n_row, self.n_column, self.n_free_cells, self.range_start, self.range_end]
        for entry in entries:
            entry.delete(0, END)

    # Function to add default values to the input fields
    def set_defaults(self):
        try:
            self.n_row.insert(0, 5)
            self.n_column.insert(0, 5)
            self.n_free_cells.insert(0, 1)
            self.range_start.insert(0, 1)
            self.range_end.insert(0, 75)

            entries = [self.n_row, self.n_column, self.n_free_cells, self.range_start, self.range_end]
            for entry in entries:
                entry.config(foreground='grey')
        except Exception as e:
            print(e)
            # Notify user that an error occured while resetting the form
            toast = ToastNotification(title="Failed", duration=9000, message="An error occured while re-setting the form. Please reset manually.", alert=True)
            toast.show_toast()
    
    # Function to terminate application
    def exit_application(self):
        sys.exit(0)

    # Function that runs the analysis
    def bingo_analyser(self):
        try:
            # Calling the method that validates the input data and returns error messages if any
            error_message = validation_helper.validate_user_input(
                self.n_cards.get(), self.n_simulations.get(), self.n_row.get(), self.n_column.get(), self.range_start.get(), self.range_end.get(), self.n_free_cells.get()
            )
            if not error_message:
                num_cards = int(self.n_cards.get())
                num_simulations = int(self.n_simulations.get())
                num_row = int(self.n_row.get())
                num_column = int(self.n_column.get())
                num_free_cells = int(self.n_free_cells.get())
                range_start_value = int(self.range_start.get())
                range_end_value = int(self.range_end.get())

                # Initialize the container that will hold the graph output
                self.init_output_screen()

                # Create cards
                self.generated_cards = bingo_helper.get_n_bingo_cards(num_cards, num_row, num_column, range_start_value, range_end_value, num_free_cells)
                # Run simulation
                self.analysis_result = bingo_helper.run_simulations(self.generated_cards, num_simulations, range_start_value, range_end_value)
                # Get stats based on simulation
                bingo_stats, full_house_stats = graph_helper.calculate_statistics(self.analysis_result)
                # Get the graph plot for the stats
                self.graph = graph_helper.plot_results(bingo_stats, full_house_stats, range_start_value, range_end_value)
                
                # Integrate the matplotlib graph in the Tkinter graph frame 
                canvas = FigureCanvasTkAgg(self.graph, master=self.graph_frame)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.pack(side="top", fill='both', expand=True)
                # Show the analysis screen
                self.show_analysis_screen()
            else:
                Messagebox.show_error("Below error(s) were encountered - \n" + error_message, title='Error', parent=None, alert=True)
        except Exception as e:
            # Log error
            print(e)
            # Notify user that an error occured while analysing
            toast = ToastNotification(title="Failed", duration=9000, message="An error occured while performing the analysis.", alert=True)
            toast.show_toast()

    # Function to download cards
    def download_cards(self):
        try:
            download_helper.download_cards(self.generated_cards)
            # Notify user that the download was successful
            toast = ToastNotification(title="Success", duration=9000, message="Bingo cards downloaded. Please view bingo_cards.pdf.", alert=True)
            toast.show_toast()
        except Exception as e:
            # Log error
            print(e)
            # Notify user that the download failed
            toast = ToastNotification(title="Failed", duration=9000, message="There was an error while downloading the cards.", alert=True)
            toast.show_toast()

    # Function to analyse further 
    def more_analysis(self):
        try:
            # Get the analysis table content
            coldata, rowdata = analysis_helper.additional_analytics(self.analysis_result, int(self.range_start.get()), int(self.range_end.get()))
            # Clear the table container
            self.clear_frame(self.table_frame)
            # Create the table
            self.table = Tableview(master=self.table_frame, coldata=coldata, rowdata=rowdata, paginated=True, searchable=True, bootstyle=SUCCESS)
            self.table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        except Exception as e:
            # Log error
            print(e)
            # Notify user that there was an error in calculating the analysis
            toast = ToastNotification(title="Failed", duration=9000, message="There was an error while performing more analysis. Please try again later.", alert=True)
            toast.show_toast()
        
# Create the main application window
app = ttk.Window()
app.geometry("800x800")

# Initialize and run the BingoGUI
bingo_app = BingoGUI(app)
bingo_app.show_home_screen()

# Start the main event loop
app.mainloop()
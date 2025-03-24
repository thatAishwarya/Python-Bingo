from tabulate import tabulate
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Function that downloads the generated cards
def download_cards(cards, file_path = "bingo_cards.pdf"):
    
    # Create a PDF document
    c = canvas.Canvas(file_path, pagesize=letter)

    # Iterate through bingo cards and draw them
    for card in cards:
        # Convert each card into a table
        table = tabulate(card, tablefmt="grid")

        # Split the table into lines and draw on the PDF
        lines = table.split('\n')
        line_height = 20

        for i, line in enumerate(lines):
            c.setFont("Helvetica", 20)
            # Draw each line on the PDF
            c.drawString(100, 700 - i * line_height, line)

        # Move to the next page
        c.showPage()

    # Save the PDF file
    c.save()
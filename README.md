# Python-Bingo

## Introduction

Software that will create bingo cards based on user inputs and generate simulations.

## File Structure

1. app.py - Entry point of the program, contains the user interface logic. It uses the below python files as helpers.

2. validator.py - It defines the helper method to validate user input

3. bingo.py - It contains the methods to generate cards, check bingo, check full house and run simulations

4. download.py - It contains the logic to download cards as a pdf file

5. graph.py - It contains methods that help you generate the simulation graph

5. more_analysis.py - It contains the logic to further analyze the game and returns 25th percentile, median, 75th percentile of both full house and bingo

## Installation

```bash
# installation steps

git clone https://github.com/AishwaryaThat/Python-Bingo.git
cd Python-Bingo
python -m pip install ttkbootstrap
python -m pip install matplotlib
python -m pip install numpy
python -m pip install tabulate
python -m pip install reportlab

# Run the program

python app.py
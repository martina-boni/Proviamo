import argparse
from argparsetest.py import return_event

valid_dates = dtvnt.keys()

def parse_arguments():
    parser = argparse.ArgumentParser(description='A program to pass dates to the return_event function')
    parser.add_argument("date", help="The string of the date in the form yyyy-mm-dd", choices=valid_dates)
    args = parser.parse_args()
    return return_event(args.date)

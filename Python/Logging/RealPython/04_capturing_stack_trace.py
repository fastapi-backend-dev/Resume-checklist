import logging

# Set up logging so messages are saved in app.log.
# This keeps errors and warnings in a file for later review.
logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

# Example values used to test the division.
donuts = 3
guests = 0

# Old examples showing different ways to log errors.
# These lines are kept for learning and comparison.
# try:
#     donuts_per_guest = donuts / guests
# except ZeroDivisionError:
#     logging.error("DonutCalculationError", exc_info=True)

# try:
#     donuts_per_guest = donuts / guests
# except ZeroDivisionError:
#     logging.error("DonutCalculationError")

# This version catches the error and records the full stack trace.
try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
    logging.exception("DonutCalculationError")

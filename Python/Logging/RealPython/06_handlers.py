import logging

# logging is Python's built-in system for showing messages while a program runs.
# A logger is like a message sender, and handlers decide where those messages go.

# __name__ gives this logger a name based on the current file.
logger = logging.getLogger(__name__)

# A StreamHandler sends log messages to the console (your terminal or output screen).
# This is useful when you want to see logs immediately while running the program.
console_handler = logging.StreamHandler()

# A FileHandler sends log messages to a file on disk.
# "a" means append mode: new messages are added to the end of the file.
# encoding="utf-8" makes sure text is written correctly.
file_handler = logging.FileHandler("custom_app.log", mode="a", encoding="utf-8")

# We attach both handlers to the logger.
# Now, every log message sent by this logger will be sent to both places:
# 1) the console
# 2) the file custom_app.log
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# This line prints the handlers attached to the logger.
# It is useful for checking whether the logger is configured properly.
# print(logger.handlers)

# This warning message will go to both the console and the log file.
logger.warning("Watch out!!")

import logging

# logging is Python's built-in way to show messages while a program runs.
# A logger lets us send messages with different levels like INFO, WARNING, ERROR.

# __name__ tells Python to name this logger after the current file/module.
logger = logging.getLogger(__name__)

# This is a simple warning message. It shows that the logger is working.
logger.warning("Look at my logger!!")

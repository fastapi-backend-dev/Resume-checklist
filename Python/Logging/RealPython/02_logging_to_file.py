import logging

# Configure logging to write messages to a file named app.log.
# The file is opened in append mode so old log entries stay and new ones are added.
# The log format includes the timestamp, log level, and message text.
logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

# Write a warning message to the log file.
logging.warning("Save me!!")

import logging

# The logging module helps us print messages that show how important they are.
# Python has different log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
# A lower level like DEBUG is more detailed, while CRITICAL is very serious.
# By default, if you do not configure logging, only WARNING and above are shown.

# Example: this line would print a warning message to the console.
# logging.warning("Remain calm!")

# These are examples of different log levels.
# Each one is useful for different situations while debugging or running an app.
# logging.debug("This is DEBUG info!")
# logging.info("This is INFO info!")
# logging.warning("This is WARNING info!")
# logging.error("This is ERROR info!")
# logging.critical("This is CRITICAL info!")

# basicConfig() sets up the logging system.
# Here, we tell Python to include DEBUG messages as well.
# Without this, logs below WARNING may not appear.
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This will also get logged!")

# format="%(levelname)s:%(name)s:%(message)s"
# This custom format prints:
# 1) level name (DEBUG, WARNING, etc.)
# 2) logger name
# 3) the actual message
# The % format style uses %-style placeholders.
# logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
# logging.warning("Hello, Warning!!")

# format="{levelname}:{name}:{message}", style="{"
# This does the same kind of formatting, but with the {} style.
# It is useful when you want to use a format string similar to str.format().
# logging.basicConfig(format="{levelname}:{name}:{message}", style="{")
# logging.warning("Hello, Warning!!")

# Now we configure logging with a more readable custom format.
# format="{asctime} - {levelname} - {message}"
# - asctime: time when the log message was created
# - levelname: severity such as WARNING, ERROR, etc.
# - message: actual message text
# style="{": tells Python to use the {} formatting style
# datefmt="%Y-%m-%d %H:%M": changes the date/time format to YYYY-MM-DD HH:MM
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

# This is the actual log entry we want to show.
# WARNING is an important message that tells us something might be wrong.
# It appears in the console with the timestamp and level name.
logging.warning("Something went wrong!!")

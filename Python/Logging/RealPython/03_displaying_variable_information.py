import logging

# This logs messages to the console using the logging module.
# We set the logging level to DEBUG so detailed information is shown.
# The format includes the time, level name, and the message.
# The `%` style is the older Python logging format style.
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.DEBUG
)

# A sample variable we want to include in the log output.
name = "Krishna"

# Log the variable value in a simple and readable format.
# This helps us see the actual data during debugging.
logging.debug("name=%s", name)

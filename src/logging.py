# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def my_view(request, arg1, arg):
    if something_bad_happened:
        # Log an error message
        logger.error('Something went wrong!')
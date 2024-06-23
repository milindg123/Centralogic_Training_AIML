#Import the logging module
import logging

#Configure the logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

#Create a logger
logger = logging.getLogger(__name__)

#Generate log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

#Divide Function
def divide(a, b):
    try:
        result = a / b
        logger.info(f"Divided {a} by {b} successfully. Result: {result}")
        return result
    except ZeroDivisionError:
        logger.error("Attempted to divide by zero")
        return None

# Test the function and logging
divide(10, 2)
divide(10, 0)


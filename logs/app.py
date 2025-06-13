import logging

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('log.txt'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmethicApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b} = {result}")
    return result

def subtraction(a,b):
    result = a-b
    logger.debug(f"Subtracting {a}-{b} = {result}")
    return result

def multiplication(a,b):
    result = a*b    
    logger.debug(f"Multiplying {a}*{b} = {result}")
    return result

def division(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a}/{b} = {result}")
        return result
    except:
        logger.error(f"Error: Division by zero")
        return None

add(10,15)
subtraction(20,5)
multiplication(5,5)
division(10,2)
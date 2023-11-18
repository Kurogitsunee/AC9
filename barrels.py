from random import randint
import logging

# configure logger
logging.basicConfig(filename='msg.log', format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# function to choose a random barrel
def random_barrel(barrels):
    # if statement for len(barrels) == 1 due to specificity of randint
    if len(barrels) == 1:
        logger.info(f"Function <random_barrel> returned {barrels[0]}.")
        return barrels[0]
    else:
        i = randint(0, len(barrels)-1)  # choosing an index of barrel
        result = barrels[i]
        logger.info(f"Function <random_barrel> returned {barrels[i]}.")
        del barrels[i]  # deleting choosed barrel from list
        return result

# asking a number of barrels
while True:
    n = int(input("Write a number of barrels: "))
    if n < 1:  # checking input
        print("Number of barrels must be a positive integer.")
        logger.error("Expecting a positive integer for number of barrels (n).")
        continue
    else:
        logger.info(f"Number of barrels (n) = {n}.")
        break

barrels = [i+1 for i in range(n)]  # creating a list of barrels
logger.info("List of barrels was created.")

logger.info("Starting a cycle.")
while n != 0:
    print(f"We took barrel with number {random_barrel(barrels)}.")  # printing a number of barrel
    if n == 1:
        print("That's the last barrel.")
        break
    next = input("Take next barrel? (Press Enter) ")
    n -= 1  # decrementing iterator / "deleting" choosed barrel
logger.info("Cycle ends successfully.")
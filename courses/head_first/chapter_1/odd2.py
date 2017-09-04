import random
import time
from datetime import datetime

odds = [1, 3, 5, 7, 9,
        11, 13, 15, 17, 19,
        21, 23, 25, 27, 29,
        31, 33, 35, 37, 39,
        41, 43, 45, 47, 49,
        51, 53, 55, 57, 59]

loop_count = 5

random_upper_bound = 60
random_lower_bound = 1

for number in range(loop_count):
    random_sleep_seconds = random.randint(random_lower_bound, random_upper_bound)
    print(str(random_sleep_seconds))

    time.sleep(random_sleep_seconds)

    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute.')


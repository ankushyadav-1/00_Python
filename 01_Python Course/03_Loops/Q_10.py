import time

wait_time = 1
max_try = 10
attempts = 0

while attempts < max_try:
    print ("Attemps: ", attempts + 1, "  -wait time:", wait_time)
    time.sleep(wait_time)

    # wait_time = wait_time * 2
    # attempts = attempts + 1
    wait_time *= 2
    attempts += 1
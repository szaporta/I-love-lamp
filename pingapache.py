import os
import random

#Run this in an infinite loop
while True:
    num_requests = random.randint(1,2001)
    num_concurrent_requests = num_requests - 1

    # Use apache bench to test concurrent requests
    os.system("ab -n" + num_requests + " -c" + num_concurrent_requests + " http://localhost/server-status?auto")

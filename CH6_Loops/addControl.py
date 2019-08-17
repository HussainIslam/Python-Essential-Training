#!/usr/bin/env python3

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5


while pw != secret:
    count += 1
    
    # Checks if the number of tries is more than max_attempts
    # If it is break out of the while loop
    if count > max_attempt: break
    # Check if the number of tries is equal to 3
    # if it is then skip that step and go back to the begining
    if count == 3: continue
    pw = input(f'{count}: Whats\'s the secret word? ')

## if the loop exits normally
else:
    auth = True

print('Authorized' if auth else 'Calling the FBI...')
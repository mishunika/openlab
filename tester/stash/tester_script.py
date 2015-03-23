import os
import sys

# Backup STDOUT
stdout = sys.stdout

# /dev/null
dev_null = open(os.devnull, 'w')

# Setting stdout to /dev/null
sys.stdout = dev_null

# Nothing happens
print("Printing to /dev/null")

# Resetting STDOUT
sys.stdout = stdout

# Printing in the normal way
print("Printing to stdout.")

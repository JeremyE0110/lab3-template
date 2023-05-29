#!/usr/bin/env python3

# Author ID: 129577193

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    output = subprocess.check_output(command, shell=True)
    output = output.decode('utf-8').strip()
    return output

if __name__ == "__main__":
    print(free_space())
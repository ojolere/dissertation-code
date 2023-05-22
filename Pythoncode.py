#This Python program to measure the performance impact of storage device fragmentation 
import os
import time
import random

test_directory = 'D:\Python OS\lere_files'-- Windows  (test_directory = 'lere_files') -- Linux
file_sizes = [512, 1024, 2048, 4096]  # File sizes in KB
num_files = 100
read_write_iterations = 10

# o ensure test directory exists
if not os.path.exists(test_directory):
    os.makedirs(test_directory)

# Function to create a random file
def create_random_file(file_path, file_size):
    with open(file_path, 'wb') as f:
        f.write(os.urandom(file_size * 1024))

# Function to create test files for fragmentation simulation
def create_test_files():
    for i in range(num_files):
        file_size = random.choice(file_sizes)
        file_path = os.path.join(test_directory, f'file_{i}.dat')
        create_random_file(file_path, file_size)

# Function to simulate fragmentation
def simulate_fragmentation():
    files = os.listdir(test_directory)
    for i in range(len(files) // 2):
        file_to_delete = random.choice(files)
        os.remove(os.path.join(test_directory, file_to_delete))
        files.remove(file_to_delete)

    for file in files:
        if random.random() < 0.5:
            file_path = os.path.join(test_directory, file)
            file_size = random.choice(file_sizes)
            with open(file_path, 'ab') as f:
                f.write(os.urandom(file_size * 1024))

# Function to measure read and write performance
def measure_performance():
    read_times = []
    write_times = []

    for i in range(read_write_iterations):
        # Measure write performance
        start_time = time.time()
        file_size = random.choice(file_sizes)
        file_path = os.path.join(test_directory, f'write_test_{i}.dat')
        create_random_file(file_path, file_size)
        end_time = time.time()
        write_times.append(end_time - start_time)

        # Measure read performance
        file_to_read = random.choice(os.listdir(test_directory))
        file_path = os.path.join(test_directory, file_to_read)
        start_time = time.time()
        with open(file_path, 'rb') as f:
            _ = f.read()
        end_time = time.time()
        read_times.append(end_time - start_time)

    return read_times, write_times

# Main program
create_test_files()
simulate_fragmentation()
read_times, write_times = measure_performance()

avg_read_time = sum(read_times) / len(read_times)
avg_write_time = sum(write_times) / len(write_times)
print(f'Average read time: {avg_read_time * 1000:.2f} ms')
print(f'Average write time: {avg_write_time * 1000:.2f} ms')

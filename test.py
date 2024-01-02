import concurrent.futures
import random 
import string

def gen_random_filename():
    random_string = ''.join(random.choices(string.ascii_lowercase,k=5))
    random_number = random.randint(1,1000)
    filename = f"{random_string}_{random_number}.txt"
    return filename

def save_file(filename):
    with open(filename,'w') as file:
        file.write("This sample file content")

def main():
    thread_pool_size = 5
    with concurrent.futures.ThreadPoolExecutor(max_workers = thread_pool_size) as executor:
        futures =[executor.submit(save_file,gen_random_filename()) for _ in range(thread_pool_size)]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
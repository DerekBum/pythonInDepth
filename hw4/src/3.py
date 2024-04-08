import multiprocessing
import threading
import time
import codecs
import logging

artifacts = "../artifacts/3/"

logging.basicConfig(level=logging.INFO, filename=artifacts + '3.log', filemode='w', format='%(asctime)s - %(message)s')


def get_entry(name, string, ind):
    return f'{name:>6} PROCESS: message \'{string}\' [{ind}]'


def process_A(input_queue, output_queue):
    ind = 0
    while True:
        message = input_queue.get()
        entry = get_entry('A', message, ind)
        logging.info(f'{entry}: EXTRACTED')
        processed_message = message.lower()
        output_queue.put(processed_message)
        entry = get_entry('A', processed_message, ind)
        logging.info(f'{entry}: SENT TO B')
        ind += 1
        time.sleep(5)


def process_B(input_queue, output_queue):
    ind = 0
    while True:
        message = input_queue.get()
        entry = get_entry('B', message, ind)
        logging.info(f'{entry}: EXTRACTED')
        encoded_message = codecs.encode(message, 'rot_13')
        entry = get_entry('B', encoded_message, ind)
        logging.info(f'{entry}: ENCODED')
        output_queue.put(encoded_message)
        logging.info(f'{entry}: SENT TO MAIN')
        ind += 1


def main():
    main_to_A_queue = multiprocessing.Queue()
    A_to_B_queue = multiprocessing.Queue()
    B_to_main_queue = multiprocessing.Queue()

    process_A_instance = multiprocessing.Process(target=process_A, args=(main_to_A_queue, A_to_B_queue))
    process_B_instance = multiprocessing.Process(target=process_B, args=(A_to_B_queue, B_to_main_queue))

    process_A_instance.start()
    process_B_instance.start()

    def input_thread():
        ind = 0
        while True:
            msg = input("Enter message: ")
            entry = get_entry('MAIN', msg, ind)
            logging.info(f'{entry}: SENT TO A')
            main_to_A_queue.put(msg)
            ind += 1

    input_thread_instance = threading.Thread(target=input_thread)
    input_thread_instance.start()

    index = 0
    while True:
        message = B_to_main_queue.get()
        entry = get_entry('MAIN', message, index)
        logging.info(f'{entry}: RECEIVED')
        index += 1


if __name__ == "__main__":
    main()

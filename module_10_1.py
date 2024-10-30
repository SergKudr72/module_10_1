import threading
import time
from time import sleep

def write_words(word_count, file_name):
    file_now = open(file_name, "w", encoding='utf-8')
    n = 1
    while n < word_count + 1:
        file_now.write(f'Какое-то слово № {n}\n')
        sleep(0.1)
        n += 1
    file_now.close()
    print(f'Завершилась запись в файл {file_name}')

start = time.time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

end = time.time()
time_result = end - start
print(f'Работа потоков: {time_result}')
f'Работа потоков: {time_result}'
start_2 = time.time()

thread_func5 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread_func6 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread_func7 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread_func8 = threading.Thread(target=write_words, args=(100, "example8.txt"))

thread_func5.start()
thread_func6.start()
thread_func7.start()
thread_func8.start()

thread_func5.join()
thread_func6.join()
thread_func7.join()
thread_func8.join()

end_2 = time.time()
time_result_2 = end_2 - start_2
print(f'Работа потоков: {time_result_2}')

"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

"""
После выполнения кода будет выведено: 
Test message
None
Test message - будет выведено на экран, через data_transmitter(), 
т.к. в функцию  transmit_to_space передали текст "Test message", 
функция запустила  data_transmitter и её print напечатал этот текст.
None - будет выведено через print(transmit_to_space("Test message")),
т.к. функция transmit_to_space ничего не возвращает (нет return)
и соотвественно на вывод будет None
"""
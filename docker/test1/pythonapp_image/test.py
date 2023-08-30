import time
import logging
import os

# LOGGER_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s'

LOGGER = logging.getLogger('my_logger')
LOGGER.setLevel(logging.DEBUG)
 
file_handler = logging.FileHandler('logs/test.log')
file_handler.setLevel(logging.DEBUG)

stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
file_handler.setFormatter(formatter)
stdout_handler.setFormatter(formatter)

LOGGER.addHandler(file_handler)
LOGGER.addHandler(stdout_handler)
 

filename = "data/sayi.txt"

def read_and_increment_number(filename, interval):
    
    
    if not os.path.exists(filename):
        with open(filename,'w+') as filetmp:
            pass
        
        
    
    
    with open(filename, 'r+') as file:
        try:
            current_number = int(file.read())
            LOGGER.info(f'Başlangiç sayisi: {current_number}')
            logging.info(f'Başlangiç sayisi: {current_number}')
        except ValueError:
         
            current_number = 0
            LOGGER.warning("Dosya boşsa ya da sayıya çevrilemeyen bir değer varsa 0'dan başlatıyoruz")
            
            

        while True:
            current_number += 1
            file.seek(0)
            file.write(str(current_number))
            file.truncate()
            LOGGER.info(f'Sayi: {current_number}')
            time.sleep(interval)

if __name__ == "__main__":
      
    interval = 1  # Saniye cinsinden ardışık sayının artış hızı

    read_and_increment_number(filename, interval)
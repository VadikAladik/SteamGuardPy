import json
from steam_totp import generate_twofactor_code_for_time
from datetime import datetime
import sys

file_name = input('Введите названиие файла с расширением\n')

try:
    with open(file_name, 'r') as f:
        maf = json.loads(f.read())

    shared_secret_from_file = maf.get('shared_secret')
    while True:
        code = generate_twofactor_code_for_time(shared_secret=f"{shared_secret_from_file}")
        current_time = datetime.now()
        formatted_time = current_time.strftime('%H:%M:%S')
        sys.stdout.write(f'\r{formatted_time}, код: {code}')
        sys.stdout.flush()


except FileNotFoundError as e:
    print(f'Файл не найден\n'
          f'Код ошибки: {e}')

a = {'one': 'aaaaa', 'two': 'bbbbb', 'three': 'ccccc'}
print(a.get('one'))
print('aaaaa' in a.values())

import secrets
print(secrets.token_hex())
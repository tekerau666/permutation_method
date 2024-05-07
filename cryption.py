# проверяет что в ключе цифры от 1 до 6
def check_key():
    with open('key.txt', 'r') as file:
        key = file.read()
    numbers = ['1', '2', '3', '4', '5', '6']
    if len(key) == 6 and all(number in key for number in numbers):
        for i in key:
            if key.count(i) > 1:
                return '0'
    else:
        return '0'
    return key

#разбивает на блоки по 6 символов
def split_text(text, block_size=6):
    return [text[i:i + block_size] for i in range(0, len(text), block_size)]


def encrypt(data, key):
    text = data
    while len(text) % 6 != 0:
        text += ' '
    blocks = len(text)//6
    blocktext = split_text(text)
    encode_text = ''
    for item in blocktext:
        block = ''
        for i in range(6):
            block += item[int(key[i])-1]
        encode_text += block
    return encode_text


def decrypt(data, key):
    text = data
    while len(text) % 6 != 0:
        text += ' '
    blocks = len(text) // 6
    blocktext = split_text(text)
    decode_text = ''
    for item in blocktext:
        block = ''
        for i in range(6):
            block += item[int(key.index(str(i+1)))]
        decode_text += block
    return decode_text
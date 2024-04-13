table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def encode(text):
    bins = str()
    for c in text:
        bins += '{:0>8}'.format(str(bin(ord(c)))[2:])
    while len(bins) % 3:
        bins += '00000000'
    d = 1
    for i in range(6, len(bins) + int(len(bins) / 6), 7):
        bins = bins[:i] + ' ' + bins[i:]
    bins = bins.split(' ')
    if '' in bins:
        bins.remove('')
    base64 = str()
    for b in bins:
        if b == '000000':
            base64 += '='
        else:
            base64 += table[int(b, 2)]
    return base64

def decode(text):
    bins = str()
    for c in text:
        if c == '=':
            bins += '000000'
        else:
            bins += '{:0>6}'.format(str(bin(table.index(c)))[2:])
    for i in range(8, len(bins) + int(len(bins) / 8), 9):
        bins = bins[:i] + ' ' + bins[i:]
    bins = bins.split(' ')
    if '' in bins:
        bins.remove('')
    text = str()
    for b in bins:
        if not b == '00000000':
            text += chr(int(b, 2))
    return text


print("TWFyaW9LYXJ0NjQ= decodificado en base64:",decode("TWFyaW9LYXJ0NjQ="))
print("MarioKart64 codificado en base64:",encode("MarioKart64"))
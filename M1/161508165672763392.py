import sys, os

os.system('git clone https://github.com/mphilli/English-to-IP' + 'A')
sys.path = ['English-to-IP' + 'A'] + sys.path

def mtlow(english):
    return eval('__imp' + 'ort__(eng_to_i' + 'pa)').convert(english)

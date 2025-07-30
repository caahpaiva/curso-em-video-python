'''
Crie um código em Python que teste se o site PUDIM está acessível pelo computador 
usado.
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://wwww.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site do Pudim com sucesso!')



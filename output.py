from tkinter import Text, Tk, END
from os import popen, path
from platform import system as sistema

def main():

    global outputText

    log_verify = path.exists('log.txt')
    #print(log_verify)

    if log_verify == False:
        logger = open('log.txt', 'w')
        logger.close()

    janela = Tk()
    janela.title('output')

    outputText = Text(janela)
    outputText.pack()

    if sistema().lower() == 'linux':
        outputText.insert(1.0, popen('cat log.txt').read())
    elif sistema.lower() == 'windows':
        outputText.insert(1.0, popen('type log.txt').read())

    janela.geometry('700x400')
    janela.mainloop()

def write_log(comando):

    log_txt = popen(f'{comando}').read()

    log_arq = open('log.txt', 'a')
    log_arq.write(log_txt)
    log_arq.close()

    if sistema().lower() == 'linux':
        log_txt = popen('cat log.txt').read()
    elif sistema().lower() == 'windows':
        log_txt = popen('type log.txt').read()

    try:
        outputText.delete(1.0, END)
        outputText.insert(1.0, log_txt)
    except:
        pass

from tkinter import *
from tkinter import messagebox, filedialog
from output import write_log, main
from datetime import datetime
from os import path


class Main():
    global janela
    janela = Tk()
    janela.title('ADB Tools')

    
    
    def adb_connect():
        #system('adb devices')
        write_log('adb devices')
        
        def getIp():
            iptxt = ip.get()

            if iptxt == '':
                messagebox.showerror('[ERRO]', 'Campo vazio')

            else:
                print(iptxt)
                #system(f'adb connect {iptxt}:5555')
                write_log(f'adb connect {iptxt}:5555')
                #system('adb devices')
                write_log('adb devices')
                janela2.destroy()

        def disconnect_function():
            #system('adb disconnect')
            write_log('adb disconnect')

        janela2 = Toplevel(janela)
        janela2.title('IP')

        ipLabel = Label(janela2, text='IP')
        ipLabel.pack()

        ip = Entry(janela2)
        ip.pack()

        ipButton = Button(janela2, width=12, text='connect', command=getIp)
        ipButton.pack()

        disconnectButton = Button(janela2, width=12, text='disconnect', command=disconnect_function)
        disconnectButton.pack()

        janela2.transient(janela)
        janela2.focus_force()
        janela2.grab_set()
        janela2.geometry('200x200')
        janela2.mainloop()


    def shell_command():
        
        def send_command():
            commandUser = commandEntry.get()
            #system(f'adb shell "{commandUser}"')
            write_log(f'adb shell "{commandUser}"')

        janela_shell = Toplevel(janela)
        janela_shell.title('Shell')

        commandLabel = Label(janela_shell, text='Shell')
        commandLabel.pack()

        commandEntry = Entry(janela_shell)
        commandEntry.pack()

        commandButton = Button(janela_shell, text='Enviar', command=send_command)
        commandButton.pack()

        infoLabel = Label(janela_shell, text='Não use\n comandos com saidas continuas!')
        infoLabel.pack(pady=10)

        ExLabel = Label(janela_shell, text='Ex: ping 192.168.1.1')
        ExLabel.pack()

        janela_shell.transient(janela)
        janela_shell.focus_force()
        janela_shell.grab_set()
        janela_shell.geometry('300x300')
        janela_shell.mainloop()
            


    def command_adb():
        def commandsadbuser():
            comando = adbEntry.get()
            #system(f'adb {comando}')
            write_log(f'adb {comando}')


        janela_adb = Toplevel(janela)
        janela_adb.title('ADB')

        adbLabel = Label(janela_adb, text='ADB Commands')
        adbLabel.pack()

        adbEntry = Entry(janela_adb)
        adbEntry.pack()

        adbButton = Button(janela_adb, text='Enviar', command=commandsadbuser)
        adbButton.pack()

        janela_adb.transient(janela)
        janela_adb.focus_force()
        janela_adb.grab_set()
        janela_adb.geometry('200x200')
        janela_adb.mainloop()

    def transferir_arquivos():

        def phone_to_pc():
            global pasta
            global a
            a = 0
            teste = 0
            pasta = filedialog.askdirectory()
            pc_arq.delete(1.0, END)
            pc_arq.insert(END, str(pasta))

        def pc_to_phone():
            global arq_do_pc
            global a
            a = 1
            teste = 1
            arq_do_pc = filedialog.askopenfilename()
            print('pc: ' + arq_do_pc)
            pc_arq.delete(1.0, END)
            pc_arq.insert(END, str(arq_do_pc))

        def enviar_arq():
            if a == 0:
                print('pc: ' + pasta)
                arq_do_celular = phone_arq.get(1.0, END)
                print('phone: ' + arq_do_celular)
                #system(f'adb pull "{arq_do_celular}" "{pasta}"')
                write_log(f'adb pull "{arq_do_celular}" "{pasta}"')
                
            if a == 1:
                arq_do_celular = phone_arq.get(1.0, END)
                print('phone: ' + arq_do_celular)
                #system(f'adb push "{arq_do_pc}" "{arq_do_celular}"')
                write_log(f'adb push "{arq_do_pc}" "{arq_do_celular}"')

        janela_transferir = Toplevel(janela)
        janela_transferir.title('transferência')

        transferir_pc = Button(janela_transferir, text='Do computador para o celular', command=pc_to_phone)
        transferir_pc.pack()

        transferir_phone = Button(janela_transferir, text='Do celular para o computador', command=phone_to_pc)
        transferir_phone.pack()

        pc_arq_lbl = Label(janela_transferir, text='Computador')
        pc_arq_lbl.pack(pady=5)
        
        pc_arq = Text(janela_transferir, height=1, width=20)
        pc_arq.pack()

        phone_arq_lbl = Label(janela_transferir, text='Celular')
        phone_arq_lbl.pack(pady=5)

        phone_arq = Text(janela_transferir, height=1, width=20)
        phone_arq.pack()

        enviar_arq = Button(janela_transferir, text='Enviar', command=enviar_arq)
        enviar_arq.pack()

        janela_transferir.transient(janela)
        janela_transferir.focus_force()
        janela_transferir.grab_set()
        janela_transferir.geometry('200x200')
        janela_transferir.mainloop()

    def power_menu():
        def desligar():
            write_log('adb shell reboot -p')
        def reiniciar():
            write_log('adb reboot')
        def fastboot():
            write_log('adb reboot fastboot')
        def recovery():
            write_log('adb reboot recovery')

        janela_power = Toplevel(janela)
        janela_power.title('Power Menu')

        desligarButton = Button(janela_power, text='Desligar', width=10, command=desligar)
        desligarButton.pack()

        reiniciarButton = Button(janela_power, text='Reiniciar', width=10, command=reiniciar)
        reiniciarButton.pack()

        fastbootButton = Button(janela_power, text='Fastboot', width=10, command=fastboot)
        fastbootButton.pack()

        recoveryButton = Button(janela_power, text='Recovery', width=10, command=recovery)
        recoveryButton.pack()

        janela_power.transient(janela)
        janela_power.focus_force()
        janela_power.grab_set()
        janela_power.geometry('200x200')
        janela_power.mainloop()

    def screen_record():
        def chose_folder_for_record():
            global pasta_para_gravacao
            global verificar_chose_folder
            verificar_chose_folder = 0
            pasta_para_gravacao = filedialog.askdirectory()

        def record_screen_finsh():
            try:
                if verificar_chose_folder == 0:
                    tempo = timeEntry.get()
                    data = datetime.now()
                    nome = data.strftime('%d-%m-%Y-%H-%M-%S')
                    write_log(f'adb shell screenrecord --time-limit {tempo} /sdcard/{nome}.mp4')
                    write_log(f'adb pull /sdcard/{nome}.mp4 {pasta_para_gravacao}')
                    write_log(f'adb shell "cd /sdcard/ && rm {nome}.mp4"')
            except:
                messagebox.showerror('[ERRO]', 'Escolha uma pasta')

        janela_record = Toplevel(janela)
        janela_record.title('Screen Record')

        timeLabel = Label(janela_record, text='Tempo de gravação')
        timeLabel.pack()

        timeEntry = Entry(janela_record)
        timeEntry.pack()

        choseFolder = Button(janela_record, width=13, text='Salvar na pasta', command=chose_folder_for_record)
        choseFolder.pack(pady=20)

        recordButton = Button(janela_record, width=13, text='Gravar', command=record_screen_finsh)
        recordButton.pack()

        janela_record.transient(janela)
        janela_record.focus_force()
        janela_record.grab_set()
        janela_record.geometry('200x200')
        janela_record.mainloop()

    def mirro_screen():
        def start_mirro():
            count = 0
            for c in range(10):
                nome = count

                if path.exists('fotos') == False:
                	write_log('mkdir fotos')

                write_log(f'adb shell screenrecord --time-limit 5 /sdcard/{nome}.mp4')
                write_log(f'adb pull /sdcard/{nome}.mp4 fotos')
                write_log(f'adb shell "cd /sdcard/ && rm {nome}.mp4"')
                
                count+=1


        janela_mirro = Toplevel(janela)
        janela_mirro.title('Mirro Screen')

        startButton = Button(janela_mirro, width=17, text='Start', command=start_mirro)
        startButton.pack(pady=70)

        janela_mirro.transient(janela)
        janela_mirro.focus_force()
        janela_mirro.grab_set()
        janela_mirro.geometry('200x200')
        janela_mirro.mainloop()

    wifi_connect = Button(janela, width=17, text='Wifi ADB', command=adb_connect)
    wifi_connect.pack()

    shell = Button(janela, width=17, text='Shell', command=shell_command)
    shell.pack()

    adb_commands = Button(janela, width=17, text='ADB Commands', command=command_adb)
    adb_commands.pack()

    transferir_arq = Button(janela, width=17, text='Transferir Arquivos', command=transferir_arquivos)
    transferir_arq.pack()

    rebootButton = Button(janela, width=17, text='Power Menu', command=power_menu)
    rebootButton.pack()

    recordButton = Button(janela, width=17, text='Screen Record', command=screen_record)
    recordButton.pack()

    espelharButton = Button(janela, width=17, text='Espelhar Tela', command=mirro_screen)
    espelharButton.pack()

    logButton = Button(janela, width=17, text='log', command=main)
    logButton.pack()

    janela.geometry('300x300')
    janela.mainloop()


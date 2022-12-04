#Um projeto simples, ideal para os desenvolvedores iniciantes. Você precisa criar apenas 3 botões para executar os seguintes comandos:

#Iniciar
#Parar
#Reiniciar

#O botão iniciar deve iniciar o cronômetro e o botão parar deve parar o cronômetro. O botão reiniciar deve reiniciar o cronômetro para 00:00:00.

#O cronômetro deve ser exibido em um rótulo. Você pode usar o módulo time para obter o tempo atual e calcular o tempo decorrido.

#Você pode usar o módulo time para obter o tempo atual e calcular o tempo decorrido.
from tkinter import *
import time

class App:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        self.label = Label(self.frame, text="00:00:00")
        self.label.pack()

        self.start = Button(self.frame, text="Start", command=self.start)
        self.start.pack(side=LEFT)

        self.stop = Button(self.frame, text="Stop", command=self.stop)
        self.stop.pack(side=LEFT)

        self.reset = Button(self.frame, text="Reset", command=self.reset)
        self.reset.pack(side=LEFT)

        self.running = False
        self.elapsed = 0

    def update_label(self):
        if self.running:
            self.elapsed = time.time() - self.start_time
        minutes, seconds = divmod(self.elapsed, 60)
        hours, minutes = divmod(minutes, 60)
        self.label.config(text="%02d:%02d:%02d" % (hours, minutes, seconds))
        self.label.after(1000, self.update_label)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed
            self.update_label()
            self.running = True

    def stop(self):
        if self.running:
            self.update_label()
            self.running = False

    def reset(self):
        self.elapsed = 0
        self.update_label()
    


root = Tk()
app = App(root)
root.mainloop()

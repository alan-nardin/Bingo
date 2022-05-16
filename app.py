import tkinter as tk
import tkinter.messagebox as mbox

window = tk.Tk()
window.title('Bingo')

botoes = []

for i, item in enumerate(['B','I','N','G','O']):
    label = tk.Label(window, text=item, font=('Consolas', 20), fg='#ff0000')
    label.grid(row=0, column=i+1, sticky='nesw', pady=5)


def pinta_btn(btn: tk.Button):
    bg = btn.cget('bg')
    if bg == '#d9d9d9':
        bg = '#00ff00'
    else:
        bg = '#d9d9d9'
    btn.config(bg=bg, activebackground=bg)
    btn.update()


for i in range(1, 76):
    button = tk.Button(window, text=i, font=('Consolas', 17), pady=30, padx=50)
    button.config(command=lambda button=button: pinta_btn(button))
    botoes.append(button)

indice = 0

for c in range(1, 6):
    window.columnconfigure(c, weight=1, minsize=30)
    for r in range(1, 16):
        window.rowconfigure(r, weight=1, minsize=30)
        botoes[indice].grid(row=r, column=c, sticky='nesw')
        indice+=1


label = tk.Label(window, text='Pressione F5 para iniciar um novo jogo', font=('Consolas', 13))
window.rowconfigure(17, weight=2, minsize=30)
label.grid(row=17, column=1, columnspan=5, sticky='nesw')

def novo_jogo(event):

    confirma = mbox.askyesno('Novo jogo', 'Deseja iniciar um novo jogo?')

    if not confirma:
        return

    for btn in botoes:
        btn.config(bg='#d9d9d9', activebackground='#d9d9d9')
        btn.update()

window.bind('<F5>', novo_jogo)

window.eval('tk::PlaceWindow . center')
window.mainloop()
import tkinter as tk

#--Variável de memória--
expressao = ""

#-- Função de Calcular --
def botao_clicado(valor):
    global expressao #variável chamada

    if valor == 'C':
        #Se o C for clicado, limpa a expressão
        expressao = ""
    elif valor == '=':
        #Se o = for clicado, calcula a expressão
        try:
            resultado = str(eval(expressao))
            expressao = resultado
        except Exception as e:
            expressao = "Error"
    else:
        expressao += str(valor)

    #Atualiza o visor
    visor.delete(0, tk.END)
    visor.insert(0, expressao)


#Janela Principal
window = tk.Tk()
window.title("Calculadora Python")
window.resizable(width=False, height=False)

#1.0 Grade
#Dizer que a coluna 0,1,2,3 e a linha 1,2,3,4,5 deve ter o mesmo "peso"
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(i+1, weight=1) #o "+1" porque a linha 0 é do visor

#2.0 Visor
#Usando Entry para exibir os números
visor = tk.Entry(window, font=("Arial", 24), justify="right",bd=10)
#O 'sticky="nsew"' faz com que o widget se preencha toda a célula da grade
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

#3.0 Botões em um loop, para evitar criar um a um, usando um loop
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
linha_atual = 1
coluna_atual = 0

for texto_botao in botoes:
    #"lambda t=texto_botao:" é um truque para passar o valor do botão pra a função
    botao = tk.Button(window, text=texto_botao, font=("Arial", 18), command=lambda t=texto_botao: botao_clicado(t))
    botao.grid(row=linha_atual, column=coluna_atual, padx=5, pady=5, sticky="nsew")
    #Avança para a próxima coluna ou pula para proxima linha
    coluna_atual += 1
    if coluna_atual > 3:
        coluna_atual = 0
        linha_atual += 1
#--- Loop de Eventos ---
window.mainloop()
import tkinter as tk

#--1. Variáveis de Memória--
valor_display ="0"
primeiro_operando = None
operador = None
esperando_segundo_operando = False

#--2. Função de Calcular 2.0 --
def botao_clicado(valor):
    global valor_display, primeiro_operando, operador, esperando_segundo_operando

    if valor in "0123456789":
        if esperando_segundo_operando:
            valor_display = valor
            esperando_segundo_operando = False
        else:
            if valor_display == "0":
                valor_display = valor
            else:
                valor_display += valor
    elif valor == '+/-':
        if valor_display != "0":
            if valor_display.startswith('-'):
                valor_display = valor_display[1:]
            else:
                valor_display = '-' + valor_display

    elif valor in "+-/*":
        #-- Calculo em Cadeia -- inicio
        # ANTES de armazenar o novo operador, esta parte verifica se já
        # existe uma conta pendente para resolver.
        if operador and not esperando_segundo_operando:
            # Se tiver, ela finge que o usuário clicou no '=' para resolver a conta anterior.
            botao_clicado('=')
        #-- Calculo em Cadeia -- fim
        #quando um operador é pressionado, armazena o estado atual
        primeiro_operando = float(valor_display)
        operador = valor
        esperando_segundo_operando = True

    elif valor == '=':
        if operador and primeiro_operando is not None:
            segundo_operando = float(valor_display)
            if operador == '+':
                resultado = primeiro_operando + segundo_operando
            elif operador == '-':
                resultado = primeiro_operando - segundo_operando
            elif operador == '*':
                resultado = primeiro_operando * segundo_operando
            elif operador == '/':
                if segundo_operando == 0:
                    resultado = "Erro"
                else:
                    resultado = primeiro_operando / segundo_operando

            if resultado != "Erro" and resultado == int(resultado):
                resultado = int(resultado)

            valor_display = str(resultado)
            primeiro_operando = None
            operador = None
            esperando_segundo_operando = True
    elif valor == 'C':
        #Limpa o estado da calculadora
        valor_display = "0"
        primeiro_operando = None
        operador = None
        esperando_segundo_operando = False

    #Atualiza o visor no final da operação
    visor.delete(0, tk.END)
    visor.insert(0, valor_display)


#--3 Interface Gráfica ---
window = tk.Tk()
window.title("Calculadora Python")
window.resizable(width=False, height=False)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(5):
    window.grid_rowconfigure(i+1, weight=1) #o "+1" porque a linha 0 é do visor

#Visor
#Usando Entry para exibir os números
visor = tk.Entry(window, font=("Arial", 24), justify="right",bd=10)
#O 'sticky="nsew"' faz com que o widget se preencha toda a célula da grade
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
#Inicia o visor com o valor 0
visor.insert(0, "0")

#Lista de botões atualizada
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '+/-', '+' #'+/-' entrou no lugar de '='
]
#Butão de Igual separado e ampliado

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
#Adicionar o botão de igual ocupando mais colunas
botao_igual = tk.Button(window, text="=", font=("Arial", 18), command=lambda: botao_clicado('='))
botao_igual.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

#--- Loop de Eventos ---
window.mainloop()
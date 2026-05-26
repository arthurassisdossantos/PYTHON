import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
        # CORRIGIDO: Agora renderiza o template em vez de retornar a tupla
        return render_template("calculadora.html", resultado=resultado, etapas=etapas)

    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro: número inválido"
            etapas = f"O logaritmo só é definido para números maiores que zero ({num1})."
        else:
            resultado = math.log10(num1)
            etapas = f"log10({num1}) = {resultado}"
        # CORRIGIDO: Agora renderiza o template em vez de retornar a tupla
        return render_template("calculadora.html", resultado=resultado, etapas=etapas)

    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        # CORRIGIDO: Mensagem tratada como erro enviada para o template
        return render_template("calculadora.html", resultado="Erro", etapas="Informe o segundo número para esta operação.")

    num2 = float(num2_valor)

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2} = {resultado}"
    elif operacao == "/":
        if num2 == 0:
            resultado = "Erro: divisão por zero"
            etapas = f"Não é possível dividir {num1} por zero."
        else:
            resultado = num1 / num2
            etapas = f"{num1} ÷ {num2} = {resultado}"
    elif operacao == "**":
        resultado = num1 ** num2
        etapas = f"{num1} ^ {num2} = {resultado}"
    else:
        resultado = "Erro"
        etapas = "Operação inválida."

    return render_template("calculadora.html", resultado=resultado, etapas=etapas)

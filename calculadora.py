# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17COIj72GPoHmnvokILZ1ZqTv_xGqJhc4

Fazer uma calculadora com as 4 operações básicas (+ - * /)
"""

operaçãodesejada= str(input("Você quer somar, subtrair, dividir ou multiplicar ?"))

if (operaçãodesejada == "somar"):
  num1 = float(input(" Qual o primeiro número ? "))
  num2 = float(input(" Qual o segundo número ? "))
  print(" O resultado da soma é: ", num1 + num2)

if (operaçãodesejada == "subtrair"):
  num1 = float(input(" Qual o primeiro número ? "))
  num2 = float(input(" Qual o segundo número ? "))
  print(" O resultado da subtração é: ", num1 - num2)

if (operaçãodesejada == "dividir"):
  num1 = float(input(" Qual o primeiro número ? "))
  num2 = float(input(" Qual o segundo número ? "))
  print(" O resultado da divisão é: ", num1 / num2)

if (operaçãodesejada == "multiplicar"):
  num1 = float(input(" Qual o primeiro número ? "))
  num2 = float(input(" Qual o segundo número ? "))
  print(" O resultado da multiplicação é: ", num1 * num2)

## Usei o "float" para que fosse possível fazer as operações com números decimais !!
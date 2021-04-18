# valor projeto : 56.300
valor_projeto = float(input("Insira o valor do projeto: "))

# aprox 2.252 (4%)
iss_recife = float(input("Insira o percentual do ISS: "))

# aprox 10.134 (18%)
icms_pe = float(input("Insira o percentual do ICMS: "))

# valor iss
valor_1 = float(iss_recife * valor_projeto) / 100.0
print(f'O valor do ISS pago e de: {valor_1}')

# valor icms
valor_2 = float(icms_pe * valor_projeto) / 100.0
print(f'O valor do ICMS pago e de: {valor_2}')


# total 12.386
valor_final = print(f'O valor final de impostos pagos sera de: R$ {valor_1 + valor_2}')
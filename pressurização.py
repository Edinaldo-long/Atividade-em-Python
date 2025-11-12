'''
Durante o voo, o comandante deve decidir se deve acionar o modo de emergência, conforme a pressão da cabine. 
Crie um programa em Python que: Peça ao usuário para digitar a pressão interna da cabine (em psi) e mostre: 
Se a pressão for maior que 10.9 psi, mostre: - Pressão normal. Sistema estável. Se a pressão estiver entre 8.0 e 10.9 psi,
 mostre: - Atenção! Pressão baixa, verifique o sistema de oxigênio. Se a pressão for menor que 8.0 psi, mostre: - Emergência! 
Máscaras de oxigênio ativadas automaticamente!
'''

pressao = float(input("Digite a pressão interna da cabine (em psi): "))

if pressao > 10.9:
    print("Pressão normal. Sistema estável.")
elif 8.0 <= pressao <= 10.9:
    print("Atenção! Pressão baixa, verifique o sistema de oxigênio.")
else:
    print("Emergência! Máscaras de oxigênio ativadas automaticamente!")

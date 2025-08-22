def cadastrar_usuario():
    print("=== Cadastro de Usuário ===")
    
    nome = input("Digite seu nome: ")  # tipo str
    idade = int(input("Digite sua idade: "))  # tipo int
    altura = float(input("Digite sua altura (em metros): "))  # tipo float
    estudante = input("Você é estudante? (sim/não): ").lower()  # tipo bool (simulado)
    
    eh_estudante = True if estudante == "sim" else False
    
    print("\n--- Analisando seus dados ---")
    
    if idade < 12:
        categoria = "Criança"
    elif idade < 18:
        categoria = "Adolescente"
    elif idade < 60:
        categoria = "Adulto"
    else:
        categoria = "Idoso"
    
    if eh_estudante and idade < 25:
        desconto = 50  # 50%
    else:
        desconto = 0
    
    print(f"\nOlá, {nome}!")
    print(f"Idade: {idade} anos")
    print(f"Altura: {altura} m")
    print(f"Categoria: {categoria}")
    print(f"Desconto disponível: {desconto}%")

# Executa a função
cadastrar_usuario()
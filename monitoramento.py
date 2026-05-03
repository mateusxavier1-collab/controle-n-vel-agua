from colorama import Fore, Style, init

# Inicializa o colorama
init()

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico) 🚨",
    "Nível 2 - Baixo ⚠️",
    "Nível 3 - Médio ✅",
    "Nível 4 - Alto 💧",
    "Nível 5 - Muito alto (alerta) 🌊"
]

# Função para definir a cor conforme o nível
def definir_cor(nivel):
    cores = {
        1: Fore.RED,
        2: Fore.YELLOW,
        3: Fore.GREEN,
        4: Fore.CYAN,
        5: Fore.BLUE
    }
    return cores.get(nivel, Fore.WHITE)

# Função para exibir o status do reservatório
def exibir_status(nivel):
    if nivel < 1 or nivel > 5:
        print(Fore.WHITE + "Nível inválido!" + Style.RESET_ALL)
        return
    
    mensagem = niveis[nivel - 1]
    cor = definir_cor(nivel)
    
    print(cor + mensagem + Style.RESET_ALL)

# Simulação dos níveis do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for i in range(1, 6):
    exibir_status(i)

print("\nSistema finalizado.")

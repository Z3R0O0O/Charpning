import psutil  # Fornece informações sobre processos do sistema e recursos do sistema.
import time  # Usado para introduzir atrasos.
import os  # Funcionalidades relacionadas ao sistema operacional.
import signal  # Envia sinais para processos.

# Limite de uso da CPU (em porcentagem)
limite_cpu = 23.0

# Nome do processo Python atual
nome_python = os.path.basename(__file__)  

# Processos que não devem ser encerrados
arquivo_excecoes = "nomes_excecoes.txt"

# Função para ler os nomes dos processos do arquivo de texto
def ler_excecoes(arquivo):
    try:
        with open(arquivo, "r") as file:
            nomes_excecoes = [line.strip() for line in file.readlines()]  # Lê os nomes no arquivo.
        return nomes_excecoes
    except FileNotFoundError:
        return []

# Adiciona o nome do processo Python atual à lista de exceções
nomes_permitidos = [nome_python]  

while True:
    try:
        nomes_excecoes = ler_excecoes(arquivo_excecoes)  # Chama a função para carregar os nomes de exceção.

        # Itera sobre todos os processos em execução no sistema
        for processo in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
            try:
                process_info = processo.info  # Obtém informações sobre o processo.
                nome_processo = process_info['name']  # Obtém o nome do processo.
                uso_cpu = process_info['cpu_percent']  # Obtém a porcentagem de uso da CPU pelo processo.

                if nome_processo.startswith('kworker/'):
                    continue  # Permite que os processos que começam com 'kworker/' funcionem sem estar na lista de exceções.

                # Verifique se o nome do processo não está na lista de exceções
                if (
                    nome_processo not in nomes_permitidos
                    and uso_cpu > limite_cpu
                    and nome_processo not in nomes_excecoes
                ):
                    print(f"Processo {nome_processo} é desconhecido. Encerrado!")
                    
                    # Pega o PID do processo
                    pid = process_info['pid'] 

                    # Envie o sinal SIGTERM para encerrar o processo
                    os.kill(pid, signal.SIGTERM)

                    # Aguarde um curto período antes de verificar o próximo processo
                    time.sleep(0.1)

                    # Se o processo ainda estiver ativo após o SIGTERM, encerre-o com SIGKILL
                    processo = psutil.Process(pid)  
                    if processo.is_running():
                        print(f"Processo {nome_processo} não respondeu ao SIGTERM. Encerrando com SIGKILL.")
                        os.kill(pid, signal.SIGKILL)  # Envie o sinal SIGKILL para encerrar o processo.

            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass  # Lidar com exceções de processos inexistentes ou acesso negado.
            except PermissionError:
                print(f"Não tenho permissão o suficiente para encerrar o processo {nome_processo}!")  # Lidar com erros de permissão.

        # Aguarde um tempo antes de verificar novamente
        time.sleep(0.005) # Pode ser mudado de acordo com a máquina!
    except KeyboardInterrupt:
        break  # Interrompe o loop ao pressionar Ctrl+C

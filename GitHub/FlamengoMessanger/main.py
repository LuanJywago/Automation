import os
import csv
import smtplib
from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURAÇÕES ---
# RECOMENDAÇÃO: Use variáveis de ambiente para esconder isso no PythonAnywhere
my_email = os.getenv("EMAIL_USER") # Por meio da variavel de ambiente, certifique-se que o código .env possa esconder tudo, juntamente ao .gitignore
password = os.getenv("EMAIL_PASSWORD") # Gere uma nova senha de app!
DESTINATARIOS = ["luanjsferreira@gmail.com", "luan.jywago@sempreceub.com"] # Escreva o email dos destinatários interessados

# Teste para ver se o email e senha estão presentes na variável de ambiente
if not my_email or not password:
    print("Erro nas variáveis de ambiente não configuradas ou tentativa de uso de email e senha.")
    exit()

# Função para enviar email pelo SMTP com a mensagem do corpo do email
def enviar_email(campeonato, adversario):
    msg = EmailMessage() 
    msg['Subject'] = f"HOJE TEM FLAMENGO! 🔴⚫"
    msg['From'] = my_email
    msg['To'] = ", ".join(DESTINATARIOS)
    
    conteudo = f"""
    Fala, Torcedor Rubro Negro!!
    
    Preparado pra mais um jogo e mais uma aventura?? 
    Fica esperto!
    HOJE É DIA DE JOGO!
    
    🏆 Campeonato: {campeonato}
    😡 Adversário: {adversario}
    
    Prepare-se e vista o manto!
    
    Boa sorte!
    
    ⠈⢶⣶⣦⣤⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠟⣛⣛⣛⡛⠛⠻⠿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⢀⡀⠀⠈⠻⣿⣿⣷⡄⠀⠀⠀⠀⣀⣤
⠀⠀⠀⠀⢠⣶⣿⠿⠛⣉⣭⣍⠛⢿⣿⠘⣿⣿⣿⣷⡜⣿⣿⣿⣎⢿⣿⣿⣿⣿
⠀⠀⠀⣴⣿⡿⠁⠀⠀⣿⣿⣿⠀⠀⠃⠀⢸⣿⣿⠉⠁⢿⣿⣿⣿⠎⠉⢻⣿⠇
⠀⠀⣼⣿⣿⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⢸⣿⣿⠀⠀⣸⣿⣿⠃⠀⠀⠘⠁⠀
⢀⣾⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⢸⣿⣿⠀⠀⣿⣿⠇⠀⠀⠀⠀⠀⠀
⢹⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⢸⣿⣿⠀⠾⠿⠋⠀⠀⠀⣠⠀⠀⠀
⠀⢿⣿⣿⣷⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⣶⣦⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠈⢻⣿⣿⣦⠀⠀⠀⣿⣿⣿⠉⠉⠉⠙⠻⣿⣷⣌⠉⠉⠉⠉⢻⣿⠟⠀⠀⠀
⠀⠀⠀⠙⢿⣿⣷⣤⡀⠿⢿⣿⠀⠀⠀⠀⢰⣜⢿⣿⣧⡀⠀⠀⠈⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠿⢿⣿⣿⣶⣶⣶⣶⣾⡇⢸⣿⣦⠻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣍⣉⣛⠋⠉⠉⠀⢸⣿⣿⠀⠙⣿⣿⣦⣀⠀⠀⣀⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡀⠀⠀⠀⣾⣿⣿⡀⠀⠈⢿⣿⣿⣿⣿⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠺⠿⣿⣿⣷⡀⠀⠚⠿⣿⣿⣷⡄⠀⠀⠙⠿⠟⠉⠀⠀⠀
    
    """
    msg.set_content(conteudo)
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(user=my_email, password=password)
            smtp.send_message(msg)
            print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
        
# Função para verificar se tem jogo no dia e mes atual, definindo como parecer numérico de acordo com a data atual (datetime.now())
def verificar_jogo():
    hoje = datetime.now()
    dia_atual = hoje.strftime("%d")
    
    meses = {
        1: "janeiro", 
        2: "fevereiro", 
        3: "março", 
        4: "abril",
        5: "maio", 
        6: "junho", 
        7: "julho", 
        8: "agosto",
        9: "setembro", 
        10: "outubro", 
        11: "novembro", 
        12: "dezembro"
    }
    mes_atual = meses[hoje.month]
    
    jogo_encontrado = False # Variável para controlar se achou jogo
    
    try:
        with open('datas.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for linha in reader:
                # Remove espaços extras e garante 2 dígitos (ex: '9' vira '09')
                dia_csv = linha['dia'].strip().zfill(2)
                mes_csv = linha['mes'].strip().lower()
                
                if dia_csv == dia_atual and mes_csv == mes_atual:
                    print(f"Jogo encontrado: Contra {linha['adversario']}")
                    enviar_email(linha['campeonato'], linha['adversario'])
                    jogo_encontrado = True
            
            if not jogo_encontrado:
                print("Hoje não tem jogo do Mengão.")
                
    except FileNotFoundError:
        print("Erro: Arquivo 'datas.csv' não encontrado.")
    except KeyError as e:
        print(f"Erro no CSV: Coluna {e} não encontrada. Verifique o cabeçalho.")

if __name__ == "__main__":
    verificar_jogo()
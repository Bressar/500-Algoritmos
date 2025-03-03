# Algoritmo 95

# Transformando PDF em Áudio
import os
import PyPDF2
import pyttsx3



def listar_vozes_disponiveis():
    """Lista todas as vozes disponíveis no sistema"""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    print("\nVozes disponíveis:")
    for idx, voice in enumerate(voices):
        # O nome da voz normalmente inclui o idioma
        print(f"{idx + 1}. {voice.name} ({voice.id})")
        # Algumas informações adicionais podem estar disponíveis
        print(f"   Idioma: {voice.languages[0] if voice.languages else 'Desconhecido'}")
    
    return voices


def converter_pdf_to_audio(nome_arquivo, voice_id=None):
    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado!")
        return 
    
    with open(nome_arquivo, 'rb') as path:
        pdf_reader = PyPDF2.PdfReader(path)
        
        speak = pyttsx3.init()
        
        # Configurar a voz se especificada
        if voice_id is not None:
            speak.setProperty('voice', voice_id)
            
        #speak.setProperty('rate', 150)     # Velocidade (padrão: 200)
        #speak.setProperty('volume', 0.9)   # Volume (0.0 a 1.0)
            
        # Opcional: ajustar a velocidade de leitura (valor padrão é 200)
        # speak.setProperty('rate', 150)  # Mais lento
        
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                print(f"\nLendo página {page_num + 1}:\n")
                print(text)
                speak.say(text)
                speak.runAndWait()
        speak.stop()
        
        
def obter_caminho_arquivo():
    """Função para obter o caminho completo do arquivo diretamente do usuário"""
    caminho_arquivo = input("Digite o caminho completo do arquivo PDF (ou apenas o nome se estiver na pasta atual): ")
    
    # Se o usuário digitou apenas o nome do arquivo, assumimos que está na pasta atual
    if not os.path.dirname(caminho_arquivo):
        caminho_arquivo = os.path.join(os.getcwd(), caminho_arquivo)
    
    # Verificar se o arquivo existe e tem extensão .pdf
    if not os.path.exists(caminho_arquivo):
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return None
    
    if not caminho_arquivo.lower().endswith('.pdf'):
        print("O arquivo não tem extensão .pdf")
        return None
        
    return caminho_arquivo

# Programa principal
def main():
    # Listar vozes disponíveis
    vozes = listar_vozes_disponiveis()
    
    # Permitir a escolha da voz
    escolha_voz = input("\nDigite o número da voz desejada (ou pressione Enter para usar a voz padrão): ")
    voice_id = None
    
    if escolha_voz and escolha_voz.isdigit():
        idx = int(escolha_voz) - 1
        if 0 <= idx < len(vozes):
            voice_id = vozes[idx].id
            print(f"Usando voz: {vozes[idx].name}")
        else:
            print("Índice inválido. Usando voz padrão.")
    
    # Obter o arquivo PDF
    caminho_arquivo = obter_caminho_arquivo()

    if caminho_arquivo:
        print(f"Convertendo arquivo: {caminho_arquivo}")
        converter_pdf_to_audio(caminho_arquivo, voice_id)
    else:
        print("Não foi possível processar o arquivo.")

if __name__ == "__main__":
    main()
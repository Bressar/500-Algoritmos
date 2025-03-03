# Algoritmo 95

# Transformando PDF em Áudio
import _osx_support
import PyPDF2
import pyttsx3


def converter_pdf_to_audio(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print("Arquivo não encontrado!")
        return 
    

    with open (nome_arquivo, 'rb') as path:
        pdfReader = PyPDF2.PdfReader(path)
        
        speak = pyttsx3.init()
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                print(f"\nLendo página {page_num + 1}:\n")
                print(text)
                speak.say(text)
                speak.runAndWait()
        speak.stop()
        
        
# Exemplo de escolha de arquivo dentro de um diretório externo
diretorio = "caminho/do/diretorio"
arquivos = [f for f in os.listdir(diretorio) if f.endswith('.pdf')]

if arquivos:
    print("Arquivos disponíveis:")
    for i, arquivo in enumerate(arquivos):
        print(f"{i + 1}. {arquivo}")

    escolha = int(input("Escolha o número do arquivo: ")) - 1
    caminho_arquivo = os.path.join(diretorio, arquivos[escolha])
    
    converter_pdf_to_audio(caminho_arquivo)
else:
    print("Nenhum arquivo PDF encontrado no diretório.")     
        
        
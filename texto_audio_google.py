from gtts import gTTS
import os

def texto_para_audio(texto, idioma='pt'):
    # Cria um objeto gTTS com o texto e o idioma desejados
    tts = gTTS(text=texto, lang=idioma, slow=False)

    # Salva o áudio gerado em um arquivo MP3
    tts.save("output.mp3")

    # Reproduz o arquivo de áudio gerado
    os.system("start output.mp3")  # No Windows
    # Para Linux ou MacOS, use: os.system("afplay output.mp3") ou os.system("mpg123 output.mp3")

# Exemplo de uso
texto = """Olá, sou a voz da Inteligência Artificial da Google e vou apresentar meu amigo Rafa. Nascido em São Paulo, 
como bom brasileiro tinha o sonho de ser jogador de futebol
mas devido os contratempos da vida, acabou não seguindo com a carreira... E olha que ele até havia inclusive se apresentado
em um clube... neste período se converteu ao evangelho de Jesus Cristo quando ainda era adolescente, na época, por ser um aluno 
destaque na escola pública, ganhou um curso da USP, para se preparar para o vestibular, por motivos familiares, teve que começar a trabalhar,
após terminar o ensino médio, começou a faculdade, 
e se formou em Radiologia Médica, antes de conseguir seu diploma, ele começou a trabalhar formalmente em 2011, 
como é uma empresa de Tecnologia em Software, e como ele sempre gostou destes assuntos técnicos,
ele acabou mudando o foco da sua carreira, ele se casou em 2018, e criou este espaço para tanto compartilhar seu testemunho,
quanto para compartilhar seu conhecimento sobre as sagradas escrituras, 
ele espera que este conteúdo  dividido, possa de alguma forma fazer a diferença na vida de você que está ouvindo."""
texto_para_audio(texto, idioma='pt')



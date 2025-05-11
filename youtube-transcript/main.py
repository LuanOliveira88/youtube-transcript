import argparse
import datetime
import os
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

USER_PATH = os.path.expanduser('~')

def gerar_nome_arquivo():
    return "transcription_" + datetime.datetime.now().strftime(r"%Y%m%d%H%M%S")

def extrair_video_id(youtube_url):
    """Extrai o ID do vídeo do link do YouTube"""
    query = urlparse(youtube_url)
    if query.hostname in ['www.youtube.com', 'youtube.com']:
        return parse_qs(query.query).get('v', [None])[0]
    elif query.hostname == 'youtu.be':
        return query.path[1:]
    return None

def transcrever_video(youtube_url):
    video_id = extrair_video_id(youtube_url)
    if not video_id:
        return "URL inválida ou não reconhecida."

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'pt-BR', 'en'])
        texto = "\n".join([t['text'] for t in transcript])
        return texto
    except Exception as e:
        return f"Erro ao obter transcrição: {e}"

def salvar_transcricao(transcricao):
    nome_arquivo = gerar_nome_arquivo() + ".txt"
    caminho = os.path.join(USER_PATH, nome_arquivo)

    with open(caminho, 'w', encoding='utf-8') as file:
        file.write(transcricao)
    
    print(f'Transcrição realizada com sucesso em: {caminho}')


def main():
    parser = argparse.ArgumentParser(
        description="Extrai a transcrição de um vídeo do YouTube (se disponível)."
    )
    parser.add_argument("url", help="URL do vídeo do YouTube")
    args = parser.parse_args()
    transcricao = transcrever_video(youtube_url=args.url)
    salvar_transcricao(transcricao=transcricao)

if __name__ == '__main__':
    main()

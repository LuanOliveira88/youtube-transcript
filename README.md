# YouTube Transcription CLI

Uma ferramenta de linha de comando para extrair automaticamente a transcrição de vídeos do YouTube (caso disponível).

---

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/LuanOliveira88/youtube-transcript
cd youtube-transcript
pip install -r requirements.txt
```

## Uso

Se estiver rodando diretamente na raíz do projeto

```bash
python main.py <url_do_video>
```

## Dependências

### Nativas

- `argparse`
- `datetime`
- `os`
- `urllib`

## De terceiros

- `youtube-transcript-api`


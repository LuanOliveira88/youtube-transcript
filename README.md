# YouTube Transcription CLI

Uma ferramenta de linha de comando para extrair automaticamente a transcrição de vídeos do YouTube (caso disponível).

---

## Instalação

### Instalando como uma ferramenta CLI

Para instalar e tornar o comando  `youtube-transcript` disponível globalmente:

1. Clone o repositório e instale as dependências:

```bash
git clone https://github.com/LuanOliveira88/youtube-transcript
cd youtube-transcript
```

2. Instale as dependências do projeto

```bash
pip install .
```
### Instalando dependências

Se você apenas deseja instalar as dependências sem instalar o pacote como uma ferramenta global

```bash
pip install -r requirements.txt
```

## Uso

Após a instalação, você pode usar o comando `youtube-transcript` no terminal para obter a transcrição de um vídeo do YouTube

## Sintaxe

```bash
youtube-transcript <url_do_video>
```

## Exemplo

1. Abra o terminal
2. Execute o comando, substituindo `<url_do_video>` pela URL do vídeo desejado:

```bash
youtube-transcript https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

3. O script irá gerar um arquivo `.txt` contendo a transcrição do vídeo


## Dependências

### Nativas

- `argparse`
- `datetime`
- `os`
- `urllib`

## De terceiros

- `youtube-transcript-api`

## Contribuindo

Contribuições são bem-vindas! Se você quiser melhorar o projeto, por favor, faça um fork, crie uma branch, e submeta um pull request com suas mudanças.
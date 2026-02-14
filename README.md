# Tradutor-para-leitura_Ubuntu-24-lts

DESCRIÇÃO

O Clipboard Selection Translator é um script em Python que monitora automaticamente o texto selecionado no sistema (selection PRIMARY do X11) e exibe a tradução em português usando o Crow Translate via terminal.

Sempre que você selecionar um texto com o mouse, o programa detecta automaticamente, traduz e mostra o resultado como uma notificação no sistema.

Desenvolvido e testado no Ubuntu 24.04 LTS.

FUNCIONALIDADES

Monitoramento automático do texto selecionado

Tradução automática usando Crow Translate (CLI)

Notificações nativas do Ubuntu

Execução contínua em segundo plano

Utiliza apenas bibliotecas padrão do Python

Código leve e simples

REQUISITOS DO SISTEMA

Sistema operacional:
Ubuntu 24.04 LTS

Sessão gráfica:
X11 (não funciona corretamente em Wayland)

Verifique sua sessão com:

echo $XDG_SESSION_TYPE

Se retornar "wayland", será necessário entrar em uma sessão X11 na tela de login.

DEPENDÊNCIAS

Python 3 (já vem instalado no Ubuntu 24)

Verifique com:

python3 --version

Pacotes necessários do sistema:

sudo apt update
sudo apt install xclip crow-translate

Verifique se estão instalados:

xclip -version
crow --version
notify-send --version

COMO FUNCIONA

O script verifica o texto selecionado a cada 0.5 segundos.

Se detectar um novo texto:

Lê usando xclip

Traduz usando crow

Mostra notificação usando notify-send

Continua rodando até ser interrompido.

ENCERRAR O PROGRAMA

Pressione:

CTRL + C

no terminal onde o programa está rodando.

CONFIGURAÇÃO

ALTERAR IDIOMA DE DESTINO

No código, modifique:

TARGET_LANG = "pt"

Exemplo para espanhol:

TARGET_LANG = "es"

ALTERAR INTERVALO DE VERIFICAÇÃO

Modifique:

CHECK_INTERVAL = 0.5

O valor está em segundos.

EXECUTAR EM BACKGROUND (OPCIONAL)

Para rodar em segundo plano:

nohup python3 clipboard_translator.py &

Ou criar um serviço systemd para iniciar automaticamente com o sistema.

LIMITAÇÕES

Funciona apenas em sessão X11

Requer conexão com internet para tradução

Depende do Crow Translate estar corretamente instalado

Pode gerar múltiplas threads se muitas seleções forem feitas rapidamente

MELHORIAS FUTURAS

Compatibilidade com Wayland

Suporte a múltiplos idiomas

Interface gráfica de configuração

Empacotamento como .deb

Execução automática ao iniciar o sistema

Melhor controle de threads

LICENÇA

Uso livre para fins educacionais e pessoais.


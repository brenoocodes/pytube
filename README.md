# pytube

## Resumo das Funções do Código

Este código é um aplicativo de interface gráfica desenvolvido com CustomTkinter para baixar vídeos de uma playlist do YouTube como arquivos MP3. Abaixo está a descrição das suas funções:

### Funções

1. **select_folder**: 
   - Abre um diálogo para selecionar uma pasta no sistema de arquivos e armazena o caminho da pasta selecionada.

2. **download_videos**: 
   - Baixa todos os vídeos de uma playlist do YouTube como arquivos MP3.
   - Verifica se a URL da playlist e a pasta de destino foram fornecidas.
   - Solicita confirmação do usuário sobre a quantidade de vídeos.
   - Faz o download de cada vídeo, converte os arquivos para MP3 e atualiza a interface com o progresso do download.
   - Se ocorrerem erros, são listados em uma mensagem de aviso.

### Configuração da Interface

- Configura o aplicativo CustomTkinter com uma aparência específica.
- Define o título e o tamanho da janela.
- Cria os widgets de entrada de URL, seleção de pasta, botão de download, e etiquetas para exibir status e última vídeo baixado.

### Funcionamento da Aplicação

A aplicação funciona permitindo que o usuário insira a URL de uma playlist do YouTube, selecione uma pasta de destino, e então inicie o processo de download e conversão dos vídeos da playlist para arquivos MP3. Durante o processo, a interface é atualizada para mostrar o progresso e o status dos downloads.

#Instalações necessárias
O melhor a ser feito é usar o terminal do seu editar para criar um novo ambiente virtual, caso seu editor não crie um ambiente virtual python de forma automática

``` cmd
python -m venv myenv
```
```cmd
myenv\scripts\activate
```

Agora instale as depedências

``` python
pip install customtkinter
```

```python
pip install pytube
```

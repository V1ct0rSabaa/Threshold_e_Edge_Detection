## Explicação técnica resumida
1. Threshold ou Limiarização é uma técnica de preprocessamento no qual consiste em segmentar os elementos de uma imagem, determinando seus pontos de corte(threshold) pela frequência. Por exemplo se queremos segmentar um disco especifico na foto de uma pilha de discos, o algoritmo vai alterar a cor dos discos para branco e preto, respectivamente se estão abaixo ou acima do ponto.
Link: https://youtu.be/1lkOTltVsQ8?si=rh8Ji93_-pju3LYZ
3. Canny's edge detection - Pode ser interpretado como uma versão mais precisa da Limiarização, antes de definir as áreas dos seguimentos, devemos utilizar o filtro Gaussiano para retirar os ruídos, calcular o desvio padrão dos gradientes de intensidade
Link: https://youtu.be/OsKz8YJ2jqE?si=QDZYDR5rnVAEpOqm

## Tecnologias utilizadas
- Python: Linguagem de programação popular na computação científica
- OpenCV: Biblioteca para processamento de imagens.
- NumPy: Biblioteca para operações numéricas, OPCIONAL pois foi utilizado somente em uma linha de código, podendo substituir por valores constantes caso desejado
- Matplotlib: Biblioteca para visualização das imagens
### Versionamento
obs: utilize o arquivo "requerimentos.txt" para facilitar a instalização das depedências
- Python 3.10.6
- matplotlib==3.9.2
- opencv-python==4.10.0.84
## Funcionalidades do Projeto
- Carregamento de imagens em diversos formatos.
- Conversão de imagens para escala de cinza.
- Aplicação de thresholding com base na mediana.
- Detecção de bordas utilizando o método de Canny.
- Salvamento das imagens processadas.
- Visualização das imagens originais e processadas.

# Revisão Bibliográfica com R, RStudio e bibliometrix
Este guia detalha os passos essenciais para realizar uma revisão bibliográfica e análise bibliométrica utilizando R e RStudio. A ferramenta principal, o pacote bibliometrix, é extremamente poderosa para mapear o conhecimento científico numa determinada área. A função biblioshiny() inicia uma interface web interativa que facilita muito a análise, mesmo para quem não tem tanta experiência com a linguagem R.

# 1. Objetivo
O uso do pacote bibliometrix permite realizar uma análise bibliométrica. O objetivo é ir além de uma revisão tradicional, respondendo a perguntas como:

  Quais são os autores mais influentes neste campo de pesquisa?

  Quais são as publicações (artigos, periódicos) mais citadas?

  Quais palavras-chave e temas são mais recorrentes ou estão a emergir?

  Como os investigadores e as instituições colaboram entre si?

Essas perguntas fornecem uma visão panorâmica e estruturada do campo, ajudando a identificar lacunas, tendências e os principais trabalhos para a revisão qualitativa.

# 2. Instalação do R e do RStudio
## Linguagem R
É uma linguagem de programação gratuita e um ambiente de software para computação estatística e gráficos.

Instalação: Navegue ao site oficial do CRAN (The Comprehensive R Archive Network), baixe e instale a versão compatível com o seu sistema operativo (Windows, macOS ou Linux).

## RStudio
É um Ambiente de Desenvolvimento Integrado (IDE) para R. Ele não é o R, mas sim um programa que torna o uso do R muito mais fácil e organizado, com janelas para scripts, consola, visualização de gráficos, pacotes, etc, assim como o Visual Studio Code.

Instalação: Após instalar o R, navegue ao site oficial do RStudio (Posit) e baixe a versão gratuita (RStudio Desktop). Ele detetará automaticamente a linguagem R instalada no passo anterior.

# 3. Bibliometrix
O termo "WEBIBLIOMINING" refere-se ao conceito de mineração de dados bibliográficos na web ou também conhecido como bibliomineração. O pacote bibliometrix é a principal ferramenta em R para executar essa tarefa de mineração.

O que ele faz? Ele importa dados bibliográficos de diversas bases (como Scopus, Web of Science, PubMed, etc.) e oferece um conjunto completo de funções para análise e visualização.

# 4. Instalação e Carregamento do Bibliometrix
Abra o RStudio.

No console ou terminal, digite o seguinte comando para instalar o pacote:

  install.packages("bibliometrix")

Após a instalação, carregue o pacote na sua sessão atual com o comando:

  library(bibliometrix)

# 5. Utilizando a Interface biblioshiny()
A função biblioshiny() inicia uma aplicação web localmente no seu navegador, oferecendo uma interface gráfica para todas as funcionalidades do bibliometrix.

Com o pacote já carregado, digite o seguinte comando no terminal:

  biblioshiny()

Uma nova janela ou aba abrir-se-á no seu navegador com a interface do biblioshiny.

# 6. Navegação no biblioshiny
A interface biblioshiny é dividida em secções, sendo elas: 

## Recolha de Dados: Antes de usar a ferramenta, precisa de exportar os dados de uma base de dados científica. As mais comuns e compatíveis são:
  Scopus: Exporte os resultados como BibTeX (.bib).
  Web of Science (WoS): Exporte como Plain Text ou BibTeX.
  PubMed: Exporte como XML.
  Dica: Ao exportar, certifique-se de incluir o registo completo, com citações, resumos e palavras-chave.

## Carregar os Dados (Load Data):
  Na interface do biblioshiny, vá para o separador Data > Import or Load file(s).
  Selecione a base de dados de origem (ex: Scopus, Web of Science).
  Clique em "Browse" e selecione o ficheiro que exportou (ex: scopus.bib).
  
  O biblioshiny irá carregar e processar os dados, mostrando um resumo no separador "Dataset Overview".

## Análise dos Dados: Navegue pelos separadores no menu lateral para explorar diferentes análises:
  Sources: Analisa as fontes mais relevantes (periódicos, livros).
  Authors: Mostra os autores mais produtivos e mais citados (Lei de Lotka, H-index).
  Documents: Identifica os documentos mais citados global ou localmente.
  Conceptual Structure: Cria mapas de palavras-chave para entender a estrutura conceptual do campo (Co-occurrence, Thematic Map).
  Social Structure: Gera mapas de colaboração entre autores, instituições e países.

## 7. Interpretação dos Resultados e Próximos Passos
Depois de gerar os gráficos e tabelas no biblioshiny, o próximo passo é a interpretação.
  Autores e Fontes Principais: 
    Veja quais autores e periódicos dominam a área. Isso indica os trabalhos que você deve priorizar na sua leitura.
  Mapa Temático (Thematic Map): 
    Este gráfico é muito útil. Ele divide os temas em quatro quadrantes: temas motores (bem desenvolvidos e importantes), temas de nicho (especializados), temas emergentes ou em declínio e temas básicos (transversais).
  Exporte os Gráficos e Tabelas:
    Cada análise no biblioshiny tem botões para exportar os resultados como imagem (PNG) ou tabela de dados (CSV, Excel). Utilize esses recursos para inserir as visualizações no seu trabalho.

## 8. Exemplo Prático com os artigo presentes no Repositório
Como o bibliometrix precisa de um ficheiro de metadados, podemos criar um exemplo simplificado no formato BibTeX (.bib) com as informações dos PDFs que você enviou. O tema central parece ser Inteligência Artificial aplicada à monitorização e identificação de fauna.

### Passo 1: Criar um Ficheiro BibTeX
Copie o texto abaixo e salve-o num ficheiro de texto com o nome exemplo_fauna.bib.

@article{puglia2023,
  author    = {Puglia, Ronaldo Garcia Ribeiro},
  title     = {A aplicação de inteligência artificial no monitoramento comportamental de Tamanduá-mirim (Tamandua tetradactyla) e Onça-pintada (Panthera onca) ex situ},
  journal   = {Programa de Pós-Graduação em Animais Selvagens},
  year      = {2023},
  keywords  = {Inteligência artificial, Comportamento animal, Redes neurais, Monitoramento, Zoológico}
}

@article{pimenta2025,
  author    = {Pimenta, Inês de Sousa},
  title     = {Deteção e Reconhecimento de espécies de fauna silvestre e doméstica por monitorização de câmaras de disparo automático},
  journal   = {Mestrado em Estatística Computacional e Análise de Dados},
  year      = {2025},
  keywords  = {Inteligência Artificial, Deep Learning, Rede Neuronal Convolucional, Deteção de Animais, YOLO}
}

@article{lopes2022,
  author    = {Lopes, Luís M. B. and Marques, Eduardo R. B. and Mamede, Tomás and Filgueiras, António and Marques, Miguel and Coutinho, Manuel},
  title     = {Identificação Taxonómica em Biologia usando Inteligência Artificial},
  journal   = {Revista de Ciência Elementar},
  year      = {2022},
  keywords  = {Inteligência Artificial, Biologia, Identificação de espécies, Ciência Cidadã}
}

@article{alvarez2024,
  author    = {Álvarez Urueña, Jaime},
  title     = {Inteligencia Artificial aplicada a la Monitorización y Control de fauna},
  journal   = {Grado en Ingeniería Informática},
  year      = {2024},
  keywords  = {Inteligência Artificial, Visão artificial, Monitoramento, Classificação de aves, Parques eólicos}
}

@article{nogueira2024,
  author    = {Nogueira, Antônio Henrique Silva and Arruda, Amilton José Vieira de},
  title     = {The use of artificial intelligence as a strategy for natural mimicry in design artifacts},
  journal   = {Cuaderno 239 | Centro de Estudios en Diseño y Comunicación},
  year      = {2024},
  keywords  = {Inteligência artificial, Design, Biomimética, Mimesis, Midjourney}
}

### Passo 2: Carregar e Analisar no biblioshiny
Inicie o biblioshiny() no RStudio.

Vá para Data > Import or Load file(s).
Selecione "Import Raw File". Como base de dados, escolha "Scopus" ou "Web of Science" (o formato BibTeX é compatível com ambos).
Clique em "Browse" e carregue o ficheiro exemplo_fauna.bib que você criou.
Clique em "Start".
Agora você pode explorar as abas, se for para Conceptual Structure > Co-occurrence Network, poderá ver um mapa visual de como as palavras-chave se conectam, mostrando que "Inteligência Artificial" é o termo central que liga todos os seus documentos.


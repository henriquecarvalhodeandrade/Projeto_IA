# 🐾 Sistema de Visão Computacional para Identificação de Fauna em Camera Traps (YOLOv8)

Este repositório contém o código-fonte e os resultados do projeto de Iniciação Científica (IC) desenvolvido por alunos do IFSP, focado em mitigar o gargalo logístico da análise manual de imagens de armadilhas fotográficas (*camera traps*).

O sistema utiliza técnicas de **Deep Learning** e a arquitetura **YOLOv8** para automatizar a detecção, localização e identificação de espécies animais, contribuindo para a agilidade e precisão da pesquisa ecológica e estratégias de conservação da fauna brasileira.

---

## 🌟 Destaques do Projeto

* **Arquitetura:** Implementação do modelo **YOLOv8** para detecção de objetos em tempo real.
* **Dataset:** Construção e anotação manual de um *dataset* focado em **fauna brasileira**, estruturado no formato nativo YOLO.
* **Técnica:** Utilização de **Aprendizado por Transferência (*Transfer Learning*)** para otimizar o desempenho com um conjunto de dados regionalizado.
* **Resultados:** Modelo de alta performance, alcançando um **mAP@0.5 de 89.3%** no conjunto de teste.
* **Aplicação:** Protótipo funcional em Python para análise em lote de imagens.

## ⚙️ Estrutura do Repositório

O projeto está organizado nas seguintes pastas principais:

| Pasta | Descrição |
| :--- | :--- |
| `data/` | Contém o arquivo `data.yaml` e a estrutura de dados (imagens e anotações `.txt`) utilizados para Treinamento, Validação e Teste do modelo. |
| `scripts/` | Scripts Python utilizados para anotação, pré-processamento, visualização de resultados e o protótipo funcional para inferência. |
| `training/` | Contém o *notebook* ou script principal de treinamento do modelo YOLOv8, onde foi realizado o *fine-tuning*. |
| `runs/` | Pasta gerada pela Ultralytics YOLO, contendo os modelos salvos (`.pt`) e os dados de log do treinamento. |
| `Avaliação/código/resultados/` | **Artefatos de Avaliação:** Contém as métricas detalhadas, Matriz de Confusão, e curvas P-R geradas ao final do treinamento. |
| `documentacao/` | Inclui o Artigo/Relatório Final do projeto, que detalha a metodologia, fundamentação teórica e discussão dos resultados. |

---

## 🚀 Instalação, Treinamento e Uso (Google Colab)

O desenvolvimento e treinamento deste modelo foram realizados utilizando o ambiente **Google Colab**, que oferece acesso a GPUs e um ambiente configurado com as dependências necessárias de Deep Learning.

### Acessando o ambiente e o Artigo

A forma mais simples de replicar o projeto é via **Google Colab**.

| Ação | Instrução |
| :--- | :--- |
| **Acessar o Notebook** | Abra o link de treinamento principal **[clicando aqui](https://colab.research.google.com/drive/1FiB9Fb2ILmkaCDrSXuTjZJZ5cyz3b0Ko?usp=sharing)** para acessar o código diretamente no Colab. |
| **Artigo/Relatório Final** | Leia a metodologia, os resultados detalhados e a discussão do projeto **[clicando aqui](https://drive.google.com/file/d/1VUm2WxBygr06ErMQJ3A-tJUQorHpivPy/view?usp=sharing)**. |
| **Video Explicativo sobre o Projeto** | Assista ao video explicativo sobre o funcionamento do Projeto **[clicando aqui](https://drive.google.com/file/d/1qqgPsbW5F6tPVRMcRXRF5DNnQ63sSt7F/view?usp=sharing)**. |




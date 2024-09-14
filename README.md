# Chatbot Rasa

Este projeto é um chatbot desenvolvido com Rasa. Abaixo estão as instruções para configurar, treinar e executar o chatbot.

## Pré-requisitos

Antes de começar, certifique-se de ter o Python e o Rasa instalados. Você pode instalar o Rasa usando o `pip`:

```bash
pip install rasa
```

## Instalação do SpaCy e Modelos

O chatbot usa o SpaCy para processamento de linguagem natural. Instale o SpaCy e o modelo em português com os seguintes comandos:

```
pip install spacy
python -m spacy download pt_core_news_md
```

## Estrutura do Projeto

O projeto contém os seguintes arquivos principais:

- **nlu.yml**: Define os intents e exemplos de treinamento.
- **stories.yml**: Define os fluxos de conversa.
- **rules.yml**: Define as regras para ações específicas.
- **domain.yml**: Define as intenções, respostas e outras configurações do chatbot.
- **config.yml**: Define a configuração do pipeline e das políticas para o Rasa.

## Passo a Passo

1. Configurar o Ambiente
Certifique-se de que você está em um ambiente Python adequado (por exemplo, usando conda ou venv).

2. Treinar o Modelo
Para treinar o modelo do Rasa com seus arquivos de configuração e dados, execute o comando:

```
rasa train
```

3. Iniciar o Chatbot
Para iniciar o chatbot e interagir com ele através do terminal, use:

```bash
rasa shell 
```
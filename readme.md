# Jogo da Velha

Pacote que suporta jogos de jogo da velha 3x3, com jogadores humanos ou computadores.

## Instalação

Para instalar execute:

```
python setup.py install
```

## Uso

Exemplo de uso do módulo `jogovelha` de um jogo Humano X Máquina:

```py
import jogovelha as jv

joao = jv.JogadorHumano("João", "X")
gpt = jv.JogadorComputador("Chat GPT Macedônio", "∆", "aleatoria")

jogo_humano_vs_robo = jv.JogoVelha(joao, gpt)
jogo_humano_vs_robo.jogar()
```
import jogovelha as jv

joao = jv.JogadorHumano("João", "X")
gpt = jv.JogadorComputador("Chat GPT Macedônio", "∆", "aleatoria")

jogo_humano_vs_robo = jv.JogoVelha(joao, gpt)
jogo_humano_vs_robo.jogar()

""" maria = jv.JogadorHumano("Maria", "O")
bard = jv.JogadorComputador("Bard Azerbaijani", "θ", "aleatoria")

jogo_humano = jv.JogoVelha(joao, maria)
jogo_humano.jogar() 
jogo_bot = jv.JogoVelha(gpt, bard)
jogo_bot.jogar() """
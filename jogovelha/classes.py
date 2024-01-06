from typing import List
from typing import Optional
import numpy as np

class Jogador:
    def __init__(self, nome: str, simbolo: str) -> None:
        """Inicializa jogador genérico

        Args:
            nome (str): nome do jogador
            simbolo (str): simbolo no jogo
        """
        self.nome = nome
        self.simbolo = simbolo
        
    def fazer_jogada(Tabuleiro) -> tuple[int, int]:
        """método genérico para ser sobrescrito
        """    
        pass


class JogadorHumano(Jogador):
    def fazer_jogada(self, lista_jogadas: List[tuple]) -> tuple[int, int]:
        """método que pede a jogada ao jogador e verifica se ela é válida

        Args:
            lista_jogadas (List[tuple]): Lista com as jogadas até o momento

        Returns:
            tuple[int, int]: tupla com as coordenadas da jogada validada
        """
        c = 0
        while True:
            if c > 0:
                print("Escolha um número de uma casa não escolhida")
            print(f"{self.nome}, escolha a coordenada (linha, coluna)"
                  "(de 1 a 3), separe com espaço:") 
            x, y = input().split()
            x, y = int(x)-1, int(y)-1
            coordenada = (x, y)
            # verifica a veracidade da jogada, caso não, loop roda até validar
            if coordenada not in lista_jogadas:
                if x > 2 or x < 0 or y > 2 or y < 0:
                    c += 1
                    continue   
                c = 0
                return coordenada
            c += 1


class JogadorComputador(Jogador):
    def __init__(self, nome: str, simbolo: str, estrategia: str) -> None:
        """inicializa jogador computador

        Args:
            nome (str): nome do computador
            simbolo (str): simbolo no jogo
            estrategia (str): estratégia aplicada
        """
        super().__init__(nome, simbolo)
        self.estrategia = estrategia
    
    def fazer_jogada(self, lista_jogadas: List[tuple]) -> tuple[int, int]:
        """Método que seleciona 2 coordenadas e as valida

        Args:
            lista_jogadas (List[tuple]): Lista com as jogadas até o momento

        Returns:
            tuple[int, int]: tupla com as coordenadas da jogada validada
        """
        if self.estrategia == "aleatoria":
            while True:
                # seleciona dois números para formar a coordenada
                numeros_aleatorios = np.random.randint(3, size=2)
                x, y = numeros_aleatorios[0], numeros_aleatorios[1]
                coordenada = (x, y)
                # valida a tupla, caso não seja válida, roda até ser válida
                if coordenada not in lista_jogadas:
                    return coordenada


class Tabuleiro:
    def __init__(self) -> None:
        """Inicializa um tabuleiro vazio
        """
        self.casas = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
    
    def pegar_tabuleiro(self) -> List[List[str]]:
        """devolve o tabuleiro

        Returns:
            List[List[str]]: o tabuleiro
        """
        return self.casas
    
    def marcar_casa(self, pos: tuple[int, int], valor: str) -> None:
        """marca o tabuleiro com o simbolo

        Args:
            pos (tuple[int, int]): posição para marcar
            valor (str): simbolo
        """
        self.casas[pos[0]][pos[1]] = valor

    def imprimir_tabuleiro(self) -> None:
        """Imprime o tabuleiro (estilizado)
        """
        print()
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(f" {self.casas[i][j]} |", end="")
            print("\n")


class JogoVelha:
    def __init__(self, jogador1: Jogador, jogador2: Jogador) -> None:
        """Inicializa um jogo e seleciona aleatoriamente quem começa

        Args:
            jogador1 (Jogador): jogador 1
            jogador2 (Jogador): jogador 2
        """
        if np.random.randint(2) == 0:
            self.jogadores = [jogador1, jogador2]
        else:
            self.jogadores = [jogador2, jogador1]
        self.tabuleiro = Tabuleiro()
        self.turno =  1
    
    def jogador_atual(self) -> Jogador:
        """Verifica, com base na rodada, qual o jogador atual

        Returns:
            Jogador: o jogador atual
        """
        if self.turno % 2 == 1:
            return self.jogadores[0]
        else:
            return self.jogadores[1]
    
    def checar_fim_de_jogo(self) -> Optional[str]:
        """Verifica se o jogo acabou (por vitória ou empate)

        Returns:
            Optional[str]: Caso termine, retorna a string com o resultado
        """
        empate = True
        vitoria = None
        tabuleiro_atual = self.tabuleiro.pegar_tabuleiro()

        # verificar vitória horizontal, caso haja, retorna o vencedor
        for i in range(3):
            vitoria = True
            for j in range(3):
                if tabuleiro_atual[i][j] != self.jogador_atual().simbolo:
                    vitoria = False
                    break
            if vitoria:
                return f"{self.jogador_atual().nome} GANHOU!!"
        
        # verificar vitória vertical, caso haja, retorna o vencedor
        for i in range(3):
            vitoria = True
            for j in range(3):
                if tabuleiro_atual[j][i] != self.jogador_atual().simbolo:
                    vitoria = False
                    break
            if vitoria:
                return f"{self.jogador_atual().nome} GANHOU!!"
        
        # checa a diagonal principal, caso acabe, retorna vencedor
        for i in range(3):
            vitoria = True
            if tabuleiro_atual[i][i] != self.jogador_atual().simbolo:
                vitoria = False
                break
        if vitoria:
            return f"{self.jogador_atual().nome} GANHOU!!"
        
        # checa a diagonal secundária, caso acabe, retorna vencedor
        for i in range(3):
            vitoria = True
            if tabuleiro_atual[i][2-i] != self.jogador_atual().simbolo:
                vitoria = False
                break
        if vitoria:
            return f"{self.jogador_atual().nome} GANHOU!!"
        
        # verifica se há empate (todas as casas preenchidas e nenhuma vitória)
        for i in range(3):
            for j in range(3):
                if tabuleiro_atual[i][j] == " ":
                    empate = False
        if empate:
            return "EMPATE!!!!!!!!"
    
    def jogar(self) -> None:
        """Começa o JOGO em si
        """
        lista_tuplas = []
        while True:
            print(f"RODADA: {self.turno}")
            self.tabuleiro.imprimir_tabuleiro()
            jogador_rodada = self.jogador_atual()
            print(f"Vez do {jogador_rodada.nome} ({jogador_rodada.simbolo})!")
            # pede jogada ao jogador, a adiciona na lista de posições jogadas 
            tupla_jogada = jogador_rodada.fazer_jogada(lista_tuplas)
            lista_tuplas.append(tupla_jogada)
            # marca casa, imprime o tabuleiro marcado e verifica acabou o jogo
            self.tabuleiro.marcar_casa(tupla_jogada, jogador_rodada.simbolo)
            self.tabuleiro.imprimir_tabuleiro()
            if self.checar_fim_de_jogo() != None:
               print(self.checar_fim_de_jogo())
               break
            self.turno += 1

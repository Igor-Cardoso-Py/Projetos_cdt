'''
  Primicias - Jogo de cartas viradas com Pygame
  
  '''

import pygame
#Biblioteca padrão
import random
#Biblioteca do sistema
import time
# Biblioteca do sistema - Contador
import os

def resolver_caminho_recurso(caminho_relativo):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    retorn os.path.join(base_path,caminho_relativo)

pygame.init()
LARGURA,ALTURA = 800,600
COR_FUNDO = (20,20,20)
COR_DE_TEXTO = (255,255,255)

caminho_imagens = "imagens"

NOMES_IMAGENS = 

VERSO_NOME = 


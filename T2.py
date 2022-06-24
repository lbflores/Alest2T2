#!/usr/bin/python3
#
# Trabalho 2 - Algoritmos e Estruturas de Dados
#
from time import process_time

import sys
sys.setrecursionlimit(1000000)

class Nodo:
    def __init__(self, tipo):
        self.tipo = tipo
        self.visitado = False
        self.disponivel = False
        self.aresta = []

        self.disponivel = self.status()
        
    def getTipo(self):
        return self.tipo 

    def status(self):    
        if self.tipo == '#':
            self.disponivel = False    
            return self.disponivel      
            
        if self.tipo == '.':
            self.disponivel = True
            return self.disponivel  
            
        if self.tipo.isnumeric():
            self.disponivel = True
            return self.disponivel  
           
        if self.tipo.isalpha() and self.tipo.isupper():
            self.disponivel = False
            return self.disponivel             
        else: 
            self.disponivel = True
            return self.disponivel  
              

    def visitado(self):
        return self.visitado

    def disponivel(self):
        return self.disponivel   

    def add_aresta(self, Node):
        self.aresta.append(Node)


    def get_aresta(self):
        return self.aresta      

    def __str__(self):
        toString = ""
        toString += "Nodo " + str(self.tipo) + " Visitado: " + str(self.visitado) + " Disponível: " + str(self.disponivel) + " Total de arestas: " + str(len(self.get_aresta())) + " Arestas: ["
        i = 0
        #imprimindo arestas
        while i < len(self.get_aresta()):
            toString += str((self.get_aresta()[i]).getTipo())
            if i < len(self.get_aresta()) - 1:
                toString += ", "
            i += 1
        toString += "]"
        return toString

def main ():
    with open("caso06.txt") as arquivo:
        mapa = arquivo.readlines()
            
    numLinhas=len(mapa) 
    numColunas= len(mapa[0])
    #print("linhas X colunas", numColunas*numLinhas)

    #cria matriz para guardar cada nodo
    valor_padrao=None
    matriz=[]
    jogadores = []
    chaves = []
    portas = []
    listaVisitados=[]
    chavesJogador=[]  
    for i in range(numLinhas):
            matriz.append([])
            for j in range(numColunas):
                matriz[i].append(valor_padrao)
	# guarda cada caracter como tipo Nodo na matriz
    for i in range (0,len(mapa)):
        for j in range (0,len(mapa[i])):
            aux = Nodo(mapa[i][j])
            matriz[i][j] = aux
            if (matriz[i][j].getTipo()).isnumeric():
                jogadores.append(matriz[i][j])    
            if (matriz[i][j].getTipo()).isalpha():
                if (matriz[i][j].getTipo().isupper()):
                    portas.append(matriz[i][j])
                if (matriz[i][j].getTipo()).islower():
                    chaves.append(matriz[i][j])    
             
        
    # Adicionando vértices de cada nodo
    listaAdj = []
    i = 2
    while i < numLinhas-1:
        j = 1
        while j < numColunas-1:
            nodoAtual = matriz[i][j]
            #print("Nodo atual: ", nodoAtual.getTipo())
            if not(nodoAtual.getTipo() == '#') and not(nodoAtual.getTipo() == None):
                listaAdj.append(nodoAtual)
                # para o direita [i][j+1]
                proximoNodo = matriz[i][j+1]
                if not(proximoNodo.getTipo() == '#') and not(proximoNodo.getTipo() == None):
                    #adiciona aresta entre os dois nodos (grafo não direcionado)
                    nodoAtual.add_aresta(proximoNodo)
                    proximoNodo.add_aresta(nodoAtual)
                   
                # para cima [i-1][j] 
                proximoNodo = matriz[i-1][j]
                if not(proximoNodo.getTipo() == '#') and not(proximoNodo.getTipo() == None):                    
                    nodoAtual.add_aresta(proximoNodo)
                    proximoNodo.add_aresta(nodoAtual)
            j+=1           
        i+=1
      
    def caminhamento(s):
        s.visitado = True
        if (s.disponivel):
            listaVisitados.append(s)
            if (s.getTipo()).islower():
                chavesJogador.append(s.getTipo())
                #print("Chave: ", s.getTipo())
            
            for v in s.get_aresta():
                if not v.visitado:
                    caminhamento(v)
        else:
            #print('Porta ' + str(s.getTipo()) + " liberada " + str(s.disponivel))
            if (s.getTipo()).isalpha() and (s.getTipo()).isupper():
                if ((s.getTipo()).lower() in chavesJogador):
                    #print('Possui chave!')
                    s.disponivel = True
                    #print('Porta ' + str(s.getTipo()) + " liberada " + str(s.disponivel))
                    caminhamento(s)

    def reinicia():
        for pos in listaAdj:
            pos.visitado = False
            for p in pos.get_aresta():
                p.visitado = False
            if (pos.getTipo()).isalpha() and (pos.getTipo()).isupper():
                pos.disponivel = False
        listaVisitados.clear()  
        chavesJogador.clear()       

    # localiza jogadores e chama as funções: reinicia e caminhamento 
    startdescomp = process_time()    
    for i in range (0,len(matriz)):
        for j in range (0,len(matriz[i])):
            try:
                if ((matriz[i][j].getTipo()).isdigit()):                
                    pos = matriz[i][j]
                    reinicia() 
                            
                    caminhamento(pos)

                    print('Player: ' + str(pos.getTipo()) + ' pode explorar '+ str(len(listaVisitados)) + ' casinhas')
            except (AttributeError):
                    pass                            
    enddescomp = process_time()
    tdescomp = (enddescomp-startdescomp)*1000
    print("tempo: ", tdescomp, "ms")    

if __name__ == "__main__":
    main()                
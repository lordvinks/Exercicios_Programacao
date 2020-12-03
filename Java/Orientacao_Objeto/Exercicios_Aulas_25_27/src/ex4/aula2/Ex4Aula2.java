package ex4.aula2;

import java.util.Scanner;


public class Ex4Aula2 {


    public static void main(String[] args) {
        //DeclarandoObejto
        Scanner in = new Scanner(System.in);
        jogoVelha jV = new jogoVelha();
        
        //Variáveis
        boolean repWhile=false;
        int calcJogador=0;
        int vez;
              
        //boas vinda
        System.out.printf("\n   \033[33;45m=|JOGO DA VELHA|=\033[m\n\n");
        
        //começo do programa
        while (!repWhile){
            jV.imprimeTabuleiro(); //Imprimir o Tabuleiro
            
            //Vez de qual Jogador
            vez = ((calcJogador%2)==0)?1:2;
            calcJogador = jV.jogador(vez, calcJogador);
            repWhile = jV.vericarGanhador(calcJogador-1);
        }
    }
    
}

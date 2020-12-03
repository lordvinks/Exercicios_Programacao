package ex4.aula2;

import java.util.Scanner;

public class jogoVelha {
    char jogoDaVelha[][] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ',' ',' '}};
    Scanner in = new Scanner(System.in);
    
    void imprimeTabuleiro(){
        System.out.printf("\033[33mL\n\033[33mI\n\033[33mN\n\033[33mH\n");
        System.out.println("\033[33mA\033[m|1||2||3|: \033[33mColuna\033[m");
        
        for (int i=0; i<jogoDaVelha.length;i++){
            System.out.print(i+1);
            for (int j=0;j<jogoDaVelha[i].length;j++){
                System.out.print("|");
                System.out.print(jogoDaVelha[i][j] + "|");
            }System.out.println("");        
        }}


    
    
        //jogador
        int jogador(int numJogador, int calcJogador){
            char simbol=(numJogador==1)?'X':'O';
            boolean repWhile=false;
            
            while(!repWhile){
                System.out.println("\n\033[33mVez do jogador " + numJogador);
                System.out.print("\nSelecione o número da linha: ");
                int linha = in.nextInt();
                System.out.print("Selecione o número da coluna: ");
                int coluna = in.nextInt();
                
                if (linha >=1 &&linha<=3){
                    linha--;coluna--;
                    if (jogoDaVelha[linha][coluna] == 'X' || jogoDaVelha[linha][coluna] == 'O'){
                        System.out.println("\nPosição está sendo utilizada!\n");
                    } else {
                        boolean repWhileOne=false;
                        while (!repWhileOne){
                            System.out.print("\nDeseja confirmar?(S/N): ");String escolha=in.next();
                            if (escolha.toLowerCase().equals("s")) {
                                jogoDaVelha[linha][coluna]=simbol;
                                repWhile=true;
                                repWhileOne=true;
                            } else if(escolha.toLowerCase().equals("n")) {
                                repWhileOne=true;
                            } else {System.out.println("\nValor inválido. Tente novamente!\n");}                           
                        }
                    }
                } else {System.out.println("\nO valor não corresponte a quantidade de linhas ou colunas!");}                                         
            }
        return calcJogador+=1;          
 }
        
        
        
        //Verificar ganhador
        boolean vericarGanhador(int jogada){
            boolean ganhador;
            if ((jogoDaVelha[0][0] == 'X' && jogoDaVelha[0][1] == 'X' && jogoDaVelha[0][2] == 'X') ||
                (jogoDaVelha[1][0] == 'X' && jogoDaVelha[1][1] == 'X' && jogoDaVelha[1][2] == 'X') ||
                (jogoDaVelha[2][0] == 'X' && jogoDaVelha[2][1] == 'X' && jogoDaVelha[2][2] == 'X') ||
                (jogoDaVelha[0][0] == 'X' && jogoDaVelha[1][0] == 'X' && jogoDaVelha[2][0] == 'X') ||
                (jogoDaVelha[0][1] == 'X' && jogoDaVelha[1][1] == 'X' && jogoDaVelha[2][1] == 'X') ||                    (jogoDaVelha[0][2] == 'X' && jogoDaVelha[1][2] == 'X' && jogoDaVelha[2][2] == 'X') ||
                (jogoDaVelha[0][0] == 'X' && jogoDaVelha[1][1] == 'X' && jogoDaVelha[2][2] == 'X')) {
                imprimeTabuleiro();
                System.out.println("\033[33mO jogador 1 ganhou!\n");
                return ganhador=true;
                
            } else if ((jogoDaVelha[0][0] == 'O' && jogoDaVelha[0][1] == 'O' && jogoDaVelha[0][2] == 'O') ||
                    (jogoDaVelha[1][0] == 'O' && jogoDaVelha[1][1] == 'O' && jogoDaVelha[1][2] == 'O') ||
                    (jogoDaVelha[2][0] == 'O' && jogoDaVelha[2][1] == 'O' && jogoDaVelha[2][2] == 'O') ||
                    (jogoDaVelha[0][0] == 'O' && jogoDaVelha[1][0] == 'O' && jogoDaVelha[2][0] == 'O') ||
                    (jogoDaVelha[0][1] == 'O' && jogoDaVelha[1][1] == 'O' && jogoDaVelha[2][1] == 'O') ||
                    (jogoDaVelha[0][2] == 'O' && jogoDaVelha[1][2] == 'O' && jogoDaVelha[2][2] == 'O') ||
                    (jogoDaVelha[0][0] == 'O' && jogoDaVelha[1][1] == 'O' && jogoDaVelha[2][2] == 'O')) {
                imprimeTabuleiro();
                System.out.println("\033[33mO jogador 2 ganhou!\n");
                return ganhador=true;
             } else if (jogada == 9) {
                 imprimeTabuleiro();
                 System.out.println("\033[33mHouve um empate!");
                 return ganhador=true;
             } else{return ganhador=false;}

        }

        
}

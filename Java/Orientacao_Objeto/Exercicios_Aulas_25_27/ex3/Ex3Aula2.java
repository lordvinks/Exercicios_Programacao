package ex3;

import java.util.Scanner;


public class Ex3Aula2 {


    public static void main(String[] args) {
        // Declarando objetos
        Scanner in = new Scanner(System.in);
        AlunoInfo alunoIn = new AlunoInfo();
        NotasAlunos notasAll = new NotasAlunos();
        
        // Declarando Variaveis pétreas
        boolean repWhile = false; int contAlunos=0, a=0;
        
        //Nome da escola
        System.out.println("\033[33m|-|-|-Escola Vizy-|-|-|\033[m");
        
        //Começo do programa
        while (!repWhile){
            //Print de escolhas 01
            System.out.printf("\n\033[32m O que deseja fazer?\033[m\n");
            System.out.println(" |1| PARA MATRICULAR UM ALUNO.");
            System.out.println(" |2| PARA ACESSAR INFORMAÇÕES DE UM ALUNO.");
            System.out.println(" |3| PARA SAIR.");
            System.out.printf("------------------------------------------\nR: ");
            byte escolha01 = in.nextByte(); // input escolha01
            
            System.out.println("");
            
            //Condição para as escolhas
            switch (escolha01) {
            
                case 1:
                    System.out.printf(" Matricular Aluno\n \n");
                    
                    //input das info
                    int posicaoAtual = alunoIn.inputInformacao(contAlunos);
                    contAlunos = posicaoAtual;
                    break;
                    
                case 2:
                    System.out.printf(" ACESSAR INFORMAÇÕES DE UM ALUNO\n \n");
     
                    //Verificar matricula do aluno
               
                    int posicaoAluno = alunoIn.verificarMatricula(a);
                    
                    
                    if (posicaoAluno != -1) {
                        //Opções
                        notasAll.escolhaAluno(posicaoAluno,
                            alunoIn.nomeAluno[posicaoAluno],
                            alunoIn.disciplinas[posicaoAluno][0],
                            alunoIn.disciplinas[posicaoAluno][1],
                            alunoIn.disciplinas[posicaoAluno][2],
                            alunoIn.curso[posicaoAluno]);
                        
                    }
                    a++;
                    break;
                    
                    
                case 3:
                    System.out.printf(" Saindo...\n");
                    repWhile=true;
                    break;
                    
                default:
                    System.out.printf("\nValor inválido. Tente novamente!\n");
                    break;
            }            
                                                                               
        }
        
        
    }
    
}

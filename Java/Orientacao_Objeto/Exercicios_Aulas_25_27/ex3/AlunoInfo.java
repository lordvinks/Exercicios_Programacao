package ex3;

import java.util.Scanner;

public class AlunoInfo {
    Scanner in = new Scanner(System.in);
    
    String nomeAluno[] = new String[10];
    int numMatricula[] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};       
    String curso[] = new String[10]; //Cursos
    String disciplinas[][] = new String[10][3]; //10 alunos/3 diciplina por aluno
    
    
    int inputInformacao(int posicao) {
        boolean repWhile=false; int numCont=0;
        
        while (!repWhile) {
            System.out.printf(" Número do aluno:\033[33m 0%d \033[m \n \n",(posicao+1));
            //nome do aluno
            System.out.print(" Digite o nome do aluno: ");
            nomeAluno[posicao] = in.nextLine();
            
            //Curso matriculado
            System.out.printf("\n Curso que está matriculado: ");
            curso[posicao] = in.nextLine();
            
            //Diciplinas
            for (int c=0; c<3; c++) {
                System.out.printf("\n Disciplina 0"+(c+1)+": ");
                disciplinas[posicao][c] = in.nextLine();
            }
          
            //Confirmar cadastro
            boolean repWhileCadastro = false;
            
            while (!repWhileCadastro) {
                System.out.printf("\n Deseja confirmar o cadastro? (S/N): ");
                String escolha02 = in.nextLine().toLowerCase();
                
                if (escolha02.toLowerCase().equals("s")) {
                    numMatricula[posicao] = posicao;
                    System.out.printf("\n Cadastro feito com sucesso! \n");
                    numCont=posicao+1;
                    repWhile=true; repWhileCadastro=true;}
                
                else if ("n".equals(escolha02)) {
                    
                    for (int i=0; i<1; i++) {
                        curso[posicao] = "";
                        nomeAluno[posicao] = "";
                        
                        for (int j=0; j<3;j++){
                            disciplinas[posicao][j] = "";}}
                    numCont=posicao;
                    System.out.printf("\n Cadastro Cancelado! \n");
                    repWhile=true; repWhileCadastro=true;
                    
                } else {System.out.printf("\n Valor inválido. Tente novamente\n");}
            }
        }
        return numCont;
    
    
    }
    
    //Vericar matricula
    int verificarMatricula(int a) {
        boolean repWhile=false;
        int n=-1;
        
        while(!repWhile) {
            System.out.print("Digite o número do aluno (0 para sair): ");
            byte escolha = in.nextByte();
            
            if (escolha==0){repWhile=true;}
            else if (escolha>0) {
                escolha -= 1;
                
                for (int i=0; i<numMatricula.length;i++){
                    if (numMatricula[i]==escolha){
                        n=i;
                        System.out.println(n);
                        break;
                    }
                }
                if (n!=-1) {repWhile=true;}
                else {System.out.printf("\nValor inválido!\n");}
            }else {System.out.printf("\nValor inválido!\n");}           
        }
        return n;               
    }
    
}

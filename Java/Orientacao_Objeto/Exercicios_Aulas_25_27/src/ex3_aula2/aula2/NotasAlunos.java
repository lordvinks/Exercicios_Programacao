package ex3.aula2;

import java.util.Scanner;


public class NotasAlunos {
    Scanner in = new Scanner(System.in);
    AlunoInfo allInfo = new AlunoInfo();
    
    float notasDisciplinas[][][] = new float[10][3][2];  //10 Alunos/3 diciplinas / 2 notas
    float media[][] = new float[10][3]; //10 alunos/ media das 3 diciplinas
    String aprovado[] = new String[10]; // verificar se o aluno foi aprovado
    
    
    

    
    
    //Painel de escolhas
    public void escolhaAluno(int posicao, String name, String disciplina01, String disciplina02, String disciplina03, String curso) {
        System.out.printf("\n Acesso a matricula de " + name + "\n");
        boolean repWhile=false;
        
        while (!repWhile) {
            //Escolha 01
            System.out.printf("\n O que deseja?\n");
            System.out.println(" |1| Editar as notas");
            System.out.println(" |2| Ver informações");
            System.out.printf(" |3| Sair\nR:");
            byte escolha01 = in.nextByte();
            
            switch (escolha01) {
                
                case 1: //Editar notas
                    editarNotas(posicao, disciplina01,disciplina02,disciplina03);
                    break;
                    
                case 2: // Ver informações
 
                    System.out.printf("\n Nome do aluno: " +name);
                    System.out.println("\n Número do aluno: 0" + posicao);
                    System.out.println(" Curso do aluno: "  + curso);
                    System.out.printf(" Disciplinas: %s, %s e %s", disciplina01, disciplina02, disciplina03);
                    System.out.printf("\n\n Médias\n");
                    System.out.printf("%s: %.2f\n",  disciplina01, media[posicao][0]);
                    System.out.printf("%s: %.2f\n",  disciplina02, media[posicao][1]);
                    System.out.printf("%s: %.2f\n",  disciplina03, media[posicao][2]);
                    
                   
                    if (media[posicao][0]<6 || media[posicao][1]<6 || media[posicao][2]<6) {
                        aprovado[posicao] = "Reprovado";                  
                    } else {aprovado[posicao] = "Aprovado";}
                    
                    System.out.println("Status: " + aprovado[posicao]);
                    break;
                    
                case 3: //Sair
                    repWhile=true;
                    break;
                    
                default:
                    System.out.printf("\n Valor inválido. Tente novamente!\n");
                    break;
            }
        }                       
    }
    
    void editarNotas(int posicao, String disciplina01, String disciplina02, String disciplina03){
        boolean repWhile=false;
        while (!repWhile){
            float nota1=0, nota2=0;
            int posicaoDisciplina;
            
            System.out.println(" Escolha uma das diciplinas");
            System.out.println(" |1| para " +disciplina01);
            System.out.println(" |2| para " +disciplina02);
            System.out.println(" |3| para " + disciplina01);
            System.out.printf(" |4| para sair\nR:");
            byte escolha01 = in.nextByte();
            
            switch (escolha01){
            
                case 1: //disciplina 1
                    posicaoDisciplina=0;
                    disciplina(posicao, posicaoDisciplina);
                    break;
                    
                case 2: //disciplina 2
                    posicaoDisciplina=1;
                    disciplina(posicao, posicaoDisciplina);
                    break;
                    
                case 3: //disciplina 3
                     posicaoDisciplina=2;
                    disciplina(posicao, posicaoDisciplina);
                    break;
                    
                case 4: //sair
                    repWhile=true;
                    break;
                    
                default:
                    System.out.printf("\n\n Valor inválido. Tente novamente!\n");
            
            }}}
    
    
    void disciplina(int posicao, int posiDisciplina) {
        boolean repWhile=false;
        float nota1;
        float nota2;
        
        while (!repWhile){
            System.out.println("");
            System.out.printf("\nNota 1: "+notasDisciplinas[posicao][posiDisciplina][0]);
            System.out.printf("\nNota 2: "+notasDisciplinas[posicao][posiDisciplina][1]+"\n\n");
            System.out.print("Digite a nota 1: ");
            nota1 = in.nextFloat();
            System.out.print("Digite a nota 2: ");
            nota2 = in.nextFloat();
            
            if (nota1<0 || nota2<0){
                System.out.println(" Valor inválido. Pois está negativo!");
            } else {
            
                boolean repWhileOne=false;
                while (!repWhileOne){
                    System.out.printf("\n\n Deseja confirmar as mudanças? (s/n): ");
                    String escolha = in.next();

                    if ("s".equals(escolha.toLowerCase())) {

                       notasDisciplinas[posicao][posiDisciplina][0]=nota1;
                       notasDisciplinas[posicao][posiDisciplina][1]=nota1;
                       repWhileOne=true; repWhile=true;
                       media[posicao][posiDisciplina] = (notasDisciplinas[posicao][posiDisciplina][0] + notasDisciplinas[posicao][posiDisciplina][1]) / 2;

                   } else if ("n".equals(escolha.toLowerCase())){repWhile=true;repWhileOne=true;}
                   else{System.out.printf("\n\nValor inválido\n");}}}
        
        
        } 
  
    }
    
}



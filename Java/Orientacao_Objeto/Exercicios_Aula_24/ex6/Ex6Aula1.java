package ex6;

import java.util.Scanner;


public class Ex6Aula1 {


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Agenda ag = new Agenda();
        
        boolean repWhile = false;
        int c=0;
        
        while (!repWhile) {
        
            System.out.println("|1|-Para add um contato");
            System.out.println("|2|-Para acessar os contatos");
            System.out.println("|3|-Para sair");
            System.out.print("R:");
            byte escolha1 = in.nextByte();
            
            
            System.out.println("");
            
            switch (escolha1) {
                case 3:
                    System.out.println("Encerrando...");
                    System.out.println("");
                    
                    repWhile=true;
                    break;
                    
                case 2:
                    for (int cc=0; cc<c; cc++) {
                        System.out.println("\033[33mContato " + (cc+1));
                        System.out.println("");
                        System.out.println("Nome: " + ag.nome[cc]);
                        System.out.println("Sobrenome: " + ag.sobrenome[cc]);
                        System.out.println("Empresa: " + ag.empresa[cc]);
                        System.out.println("Número: " + ag.numero[cc]);
                        System.out.println("Email: " + ag.email[cc]);
                        System.out.println("");
                        System.out.println("");
                    }
                    break;
                    
                case 1:
                    System.out.println("Caso não tenha alguma informação, aperte espaço!");
                    System.out.println("");
                    
                    System.out.print("Nome: ");
                    ag.nome[c] = in.next();
                    
                    System.out.print("Sobrenome: ");
                    ag.sobrenome[c] = in.next();
                    
                    System.out.print("Empresa: ");
                    ag.empresa[c] = in.next();
                    
                    System.out.print("Número: ");
                    ag.numero[c] = in.nextInt();
                    
                    System.out.print("Email: ");
                    ag.email[c] = in.next();
                    c++;
                    break;
                    
                default:
                    System.out.println("Valor inválido. Tente novamente!");
                    break;
            }
            
            System.out.println("");
        }
        
        
    }
    
}

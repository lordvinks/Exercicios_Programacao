package ex2.aula2;

import java.util.Scanner;

public class ContaBancaria {
    Scanner in = new Scanner(System.in);
    Seguranca seg = new Seguranca();

    boolean[] contaEspecial = new boolean[10];
    float limite[] = new float[10];  
    boolean[] usoChqEspecial = new boolean[10];
     
    //Conta especial e cheque especial
    void contaEspecial1(int a, int b){
        boolean especial=false;
        
        boolean repWhile=false;
        while (!repWhile) {
            String escolha = in.next();
            switch (escolha.toLowerCase()) {
                case "s":
                    especial = true;
                    repWhile=true;
                    break;
                case "n":
                    repWhile=true;
                    break;
                default:
                    System.out.println("");
                    System.out.println("Valor incorreto! Lembre-se, somente digite s ou n.");
                    break;}}    
        if (b==1) {contaEspecial[a] = especial;}
        else if(b==0) {usoChqEspecial[a] = especial;}
    }
    
    
    //limite
    void limiteConta(int a, float sal) {
        float s = (50*sal)/100;
        limite[a] = s;
    }
        void perguntasUser(int posicao, float limite2, int a) {
            boolean repWhile=false;
            
            while(!repWhile) {
                
                System.out.println("O que deseja fazer?");
                System.out.println("|1|Ver informações da conta");
                System.out.println("|2|Depositar dinheiro");
                System.out.println("|3|Sacar dinheiro");
                System.out.println("|4|Sair");
                System.out.print("R: ");
                int escolha = in.nextInt();
                System.out.println("");

            
                switch (escolha) {
                    case 1:
               
                        System.out.println("Número da conta: " + a);
                        System.out.println("Conta especial: " + contaEspecial[posicao]);
                        System.out.printf("Limite: R$%.2f\n", limite[posicao]);
                        System.out.println("Possui cheque especial: " + usoChqEspecial[posicao]);
                        System.out.printf("Saldo: R$%.2f\n", seg.saldo[posicao]);
                        break;
                        
                    case 2:
                        deposito(posicao);
                        break;
                        
                    case 3:
                        sacar(posicao, limite2);
                        break;
                        
                    case 4:
                        repWhile=true;
                        break;
                
                    default:
                        System.out.println("");
                        System.out.println("Valor inválido. Tente novamente!");
                        System.out.println("");
                        break;}System.out.println("");}
            
                        
        }
        //Depositar
        void deposito(int posi) {
            System.out.println("");
            boolean repWhile = false;
            float deposit=0;
            
            while(!repWhile) {
                System.out.print("Valor que será depositado (0 para sair): R$");
                deposit = in.nextFloat();
                
                if (deposit<0) {System.out.println("");System.out.println("Valor inválido!");System.out.println("");}
                else {repWhile = true;}
            }
            
            System.out.printf("O valor de R$%.2f foi depositado com sucesso!\n", deposit);
            seg.saldo[posi] += deposit;
            System.out.printf("Agora o seu saldo é de R$%.2f!\n", seg.saldo[posi]);
            
        }
        //sacar
        void sacar(int posi, float limite) {
            System.out.println("");
            boolean repWhile=false;
            float sacar=0;
            
            while (!repWhile) {
                System.out.print("Digite o valor que será sacado: (0 para sair): R$");
                sacar = in.nextFloat();
                
                if (sacar<seg.saldo[posi] && sacar <= limite && sacar > 0) {
                    seg.saldo[posi]-=sacar;
                    System.out.println("");
                    System.out.printf("Você sacou R$%.2f\n", sacar);
                    System.out.printf("Seu saldo agora é de R$%.2f\n", seg.saldo[posi]);
                    repWhile = true;
                } else if (sacar==0) {repWhile=true;}
                else if (sacar > limite){
                    System.out.println("");
                    System.out.printf("Valor inválido. Esses valor ultrapassa o limite de R$%.2f!\n", limite);
                    System.out.println("");}
                
            }
        }
        
}




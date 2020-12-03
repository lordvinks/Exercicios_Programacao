package ex5.aula1;

import java.util.Random;
import java.util.Scanner;


public class Ex5Aula1 {


    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ContaBancaria cB = new ContaBancaria();
        Random all = new Random();
        
        boolean alt = false;
        
        while (!alt) {
            System.out.println(":   O QUE DESEJA?  |");
            System.out.println("|1|: Acessar conta |");
            System.out.println("|2|:  Criar conta  |");
            System.out.println("|3|:      Sair     |");
            System.out.print("R: "); byte escolha = input.nextByte();
            
            System.out.println("");
            
            switch (escolha) {
                case 3:
                    alt = true;
                    break;
                case 2:
                    System.out.println("");
                    
                    cB.pinConta = all.nextInt(10000) + 10000;
                    System.out.println("=|CRIAR CONTA|=");
                    System.out.println("");
                    
                    System.out.println("PIN DO USER: " + cB.pinConta);
                    
                    System.out.print("Nome Completo: ");                
                    cB.nameUser = input.next();
                    
                    System.out.print("Criar senha: ");
                    cB.senhaConta = input.nextInt();
                    
                    System.out.print("Quantidade de dinheiro que será depositado: R$:");
                    cB.saldo = input.nextFloat();
                    
                    System.out.println("");
                    
                    break;
                case 1:
                    System.out.println("| Acessar Conta |");
                    boolean repWhile = false;
                    int pinUser, senha;
                    
                    while (!repWhile) {
                        System.out.print("Digite o PIN: ");
                        pinUser = input.nextInt();
                        
                        System.out.print("Digite a senha: ");
                        senha = input.nextInt();
                        
                        System.out.println("");
                        
                        if (pinUser==cB.pinConta && senha==cB.senhaConta) {
                            System.out.println("Nome: " + cB.nameUser);
                            System.out.println("PIN: " + cB.pinConta);
                            System.out.println("Saldo: R$:" + cB.saldo);
                            
                            System.out.println("");
                            
                            System.out.println("|Deseja depositar?(press 1)");
                            System.out.println("|Deseja Retirar dinheiro?(press 2)");
                            System.out.println("| Deseja sair (press 3)");
                            
                            System.out.print("R: "); byte escolhaTwo= input.nextByte();
                            
                            System.out.println("");
                            
                            switch (escolhaTwo) {
                                case 3:
                                    repWhile=true;
                                    break;
                                case 2:
                                    boolean repWhile2 = false;
                                    while (!repWhile2){
                                        System.out.println("");
                                        System.out.print("Quantidade de dinheiro que será retirado? (zero para sair) ");
                                        float qntRetirado = input.nextFloat();
                                        
                                        if (cB.saldo > qntRetirado) {
                                            cB.saldo -= qntRetirado;
                                            repWhile2 = true;} else{System.out.println("");
                                            System.out.println("Valor Maior que o saldo da conta!");System.out.println("");}
                                    }   break;
                                case 1:
                                    System.out.println("Depositar Dinheiro");
                                    boolean repWhile4 = false;
                                    while (!repWhile4) {
                                        System.out.print("Valor que será depositado: R$:");
                                        float valorDep = input.nextFloat();
                                        
                                        if (valorDep >=0) {
                                            cB.saldo += valorDep;
                                            repWhile4 = true;
                                        } else {
                                            System.out.println("");
                                            System.out.println("Valor Inválido!");
                                            System.out.println("");}}
                                    break;
                                default:
                                    break;
                            }
                            } else {System.out.println("");System.out.println("Valor Inválido");System.out.println("");}
                    }
                    break;
                    
                default:
                    System.out.println("");
                    System.out.println("Valor inválido");
                    System.out.println("");
            }
            
            System.out.println("2");            
        }
        

        
    }
    
}

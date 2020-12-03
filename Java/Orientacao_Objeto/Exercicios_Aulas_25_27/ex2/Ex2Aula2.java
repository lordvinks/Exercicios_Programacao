
package ex2;

import java.util.Scanner;

public class Ex2Aula2 {
    
   
    static void inEscolha() {
        System.out.println("");
        System.out.println("|1| Para criar uma conta");
        System.out.println("|2| Para acessar uma conta");
        System.out.println("|3| Para sair");
        System.out.print("R:");}
       
    public static void main(String[] args) {
        //imports
        Seguranca Seg = new Seguranca();
        Scanner in = new Scanner(System.in);
        ContaBancaria cB = new ContaBancaria();
        
         
        int numDeContas=0;
        
        System.out.println("\033[33m ||||Vizy Bank||||");
        boolean repWhile=false;
        while (!repWhile) {
            
            //print escolhas
            inEscolha();
            byte escolha1 = in.nextByte();
            System.out.println("");
            
            switch (escolha1) {
                case 1:
                    //Primeira conta
                    System.out.println("|Criando conta|");

                    //Número da conta
                    int numCont = Seg.validarConta(numDeContas);
                    System.out.println(" Número da conta: \033[32m" +numCont + "\033[m");

                    //senha
                    Seg.validarSenha(numDeContas);

                    //renda total por mês
                    boolean repWhileTwo = false;
                    while (!repWhileTwo) {
                        System.out.print("Digite a renda total por mês: R$");
                        float salMes = in.nextFloat();
                        
                        if (salMes>0) {
                            cB.limiteConta(numDeContas, salMes);
                            repWhileTwo= true;}
                        else if (salMes==0){cB.limiteConta(numDeContas, 1000); repWhileTwo = true;}
                        else {System.out.println("");
                            System.out.println("Valor inválido. Tente novamente!");
                            System.out.println("");}
                    
                    }
                    
                    

                    //Conta especial
                    System.out.print("A conta é especial?(S/N): ");
                    cB.contaEspecial1(numDeContas, 1);

                    //Cheque especial
                    System.out.print("Possui cheque especial?(S/N): ");
                    cB.contaEspecial1(numDeContas, 0);
            
                    //limite
                    System.out.printf("Limite: R$%.2f por mês!", cB.limite[numDeContas]);
                    System.out.println("");
                    numDeContas++;
                    break;
                    
                    //Acessar conta
                case 2:
                    System.out.println("Acessar Conta");
                    System.out.println("");
                    boolean repWhileOne= false;
                    while (!repWhileOne) {
                        
                        //Procurando posicao da conta
                        System.out.print(" Digite o número da conta: (0 para sair): ");
                        int numCont2 = in.nextInt();
                        int posicaoConta = Seg.acharUser(numCont2);
                        
                        if (posicaoConta==-2) {repWhileOne= true;}
                        
                        else if (posicaoConta >=0) {
                            int numPerdido=numCont2;
                            //senha
                            System.out.print("Digite a senha: ");
                            String senhaCont = in.next();
                            
                                //Acesso Autorizado
                            if (senhaCont.equals(Seg.senha[posicaoConta])) {
                                System.out.println("");
                                System.out.println("Acesso autorizado!");
                                System.out.println("");
                                
                                // ver o que o usúario quer fazer
                                cB.perguntasUser(posicaoConta, cB.limite[posicaoConta], numPerdido);
                            
                            }}}
                    break;
                
                case 3:
                    System.out.println("");
                    System.out.println("Saindo!");
                    System.out.println("");
                    repWhile = true;
                    break;
                    
                default:
                    System.out.println("");
                    System.out.println("Valor inválido!");
                    System.out.println("");
                    break;}}
        
          
    

    }
    
}

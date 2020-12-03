package ex1.aula2;

import java.util.Scanner;


public class Lampada {
    Scanner in = new Scanner(System.in);
    String modelo;
    int tensao;
    int potencia;
    String cor;
    int garantia;
    boolean tipoAbajur;
    boolean ligada;
    
    boolean verificarBoolean(){
        boolean repWhile=false;
        boolean sN=false;
        
        while(!repWhile){        
        String tipo = in.next();
        
            switch (tipo.toLowerCase()) {
                case "s":
                    sN=true;
                    repWhile=true;
                    break;
                case "n":
                    repWhile=true;
                    break;
                default:
                    System.out.println("Valor incorreto. Tente novamente!");
                    break;
            }
        }        
        return sN;
    }
    
    String verificarString() {
        String a = in.next();
        return a;
    }
    
    int verificarInt() {
        int a = in.nextInt();
        return a;
    }
    
    void inputLamp() {
        System.out.println("");
        System.out.println("O modelo é: " + modelo);
        System.out.println("Com uma tensão de: " +  tensao + "V");
        System.out.println("E uma potência de: " + potencia + "W");
        System.out.println("Cor: " + cor);
        System.out.println("Garantia de " + garantia + " meses");
        System.out.println("É do tipo abajur? " + tipoAbajur);
        System.out.println("Está ligada? " + ligada);
        System.out.println("");
    }
}

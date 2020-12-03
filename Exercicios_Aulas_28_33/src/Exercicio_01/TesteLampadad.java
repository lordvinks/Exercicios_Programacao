package Exercicio_01;

import java.util.Scanner;


public class TesteLampadad {
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in); //imports
        Lampada lamp = new Lampada(); // chamando a classe
        
        lamp.setLigarLampada(false); // desligando a lampada
        
        // REPECIÇÃO BASE DO SCRIPT
        boolean repWhile = false;
        while(!repWhile){
        
            System.out.print("\033[33m A lampada está " + lamp.statusLampada(0) + ". Deseja " + lamp.statusLampada(1)+ "?\033[m");
            
            //ESCOLHA DO USER
            lamp.painelEscolha();
            byte escolha = in.nextByte();
            
            switch (escolha) { //CONDIÇÃO DE ESCOLHA DO USER
            
                case 1 -> {
                    lamp.setLigarLampada(!lamp.getStatusLampada());
                    System.out.println("\033[33m A lampada foi " + lamp.statusLampada(0) + "\n");
                }
                    
                case 2 -> System.out.println("\033[33m A lampada está " + lamp.statusLampada(0) + "\n");
                
                case 3 -> {
                    System.out.println("\n SAINDO...");
                    repWhile = true;
                }
                    
                default -> System.out.println("\033[33m Valor inválido. Tente novamente \033[m");
            }
            
        }
               
        
    }
}

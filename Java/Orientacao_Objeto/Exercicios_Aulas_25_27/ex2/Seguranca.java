package ex2;

import java.util.Random;
import java.util.Scanner;


public class Seguranca {
    Random all = new Random();
    Scanner in = new Scanner(System.in);
    
    int numConta[] = new int[10];
    String senha[] = new String[10];
    float saldo[] = new float[10];
    
    //Validar conta
    int validarConta(int a) {
        int pin=0;
        int cont=-1;
        
        boolean repWhile=false;
        while (!repWhile) {
            pin = all.nextInt(90000)+10000;
        
            for (int c=0; c<numConta.length; c++) {
                if (pin == numConta[c]) {cont++;}}
        
           if (cont==-1) {repWhile=true;} 
        }
        numConta[a] = pin;
        return pin;
    }
    
    //ADD SENHA
    void validarSenha(int a) {
        boolean repWhile = false;
        
        while (!repWhile) {
            System.out.println("");
            System.out.println("Deve conter no minimo 8 caracteres e não deve ter espaços!");
            
            System.out.print("Crie uma senha: ");
            String senhaConta = in.nextLine();
            
            if (senhaConta.length() >= 8) {
                senha[a] = senhaConta;
                repWhile=true;
            } else{
                System.out.println("");
                System.out.println("Essa senha possui apenas "+senhaConta.length()+" caracteres!");
                System.out.println("Ela deve possuir no minimo 8 caracteres!");}
        }
    }
    
    //Acessar conta
    
        //achar user
    int acharUser(int pin){
        boolean repWhile=false;
        int posicaoDaConta = -1;
        if (pin==0) {repWhile=true; posicaoDaConta=-2;}
        
        while (!repWhile) {
            
            for (int c=0; c<numConta.length; c++) {
                if (numConta[c] == pin ) {posicaoDaConta=c; repWhile=true;}
            }

            if (posicaoDaConta==-1) {
                System.out.println("");
                System.out.println("Essa conta não existe. Tente Novamente!");
                System.out.println("");
                repWhile=true;}}
        
            return posicaoDaConta;
    }
    
}

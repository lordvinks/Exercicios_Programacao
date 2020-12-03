
package ex2;

import java.util.Scanner;


public class Ex2_Aula1 {


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Livro book = new Livro();
        
        System.out.print("Nome do Livro: ");
        book.nome = in.nextLine();
        
        System.out.print("Autor: ");
        book.autor = in.nextLine();
        
        System.out.print("Editora: ");
        book.editora = in.nextLine();
        
        System.out.print("Gênero: ");
        book.genero = in.nextLine();
        
        System.out.print("Quantidade de páginas: ");
        book.quantPag = in.nextInt();
        
        System.out.print("Idioma: ");
        book.idioma = in.next();
        
        System.out.println("");
        
        System.out.println("Nome do livro: " + book.autor);
        System.out.println("Autor: " + book.autor);
        System.out.println("Editora: " + book.editora);
        System.out.println("Gênero: " + book.genero);
        System.out.println("Quant. de páginas: " + book.quantPag);
        System.out.println("Idioma: " + book.idioma);
    }
    
}

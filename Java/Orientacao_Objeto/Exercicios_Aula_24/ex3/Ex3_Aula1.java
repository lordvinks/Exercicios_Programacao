package ex3;

import java.util.Scanner;


public class Ex3_Aula1 {


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Livraria book = new Livraria();
        
        System.out.print("Nome do Livro: ");
        book.nome = in.next();
        
        System.out.print("Autor: ");
        book.autor = in.next();
        
        System.out.print("Preço: R$");
        book.preco = in.nextFloat();
        
        System.out.print("Editora: ");
        book.editora = in.next();
        
        System.out.print("Gênero: ");
        book.genero = in.next();
        
        System.out.print("Quantidade de páginas: ");
        book.quantPag = in.nextInt();
        
        System.out.print("Idioma: ");
        book.idioma = in.next();
        
        System.out.println("");
        
        System.out.println("Nome do livro: " + book.autor);
        System.out.println("Autor: " + book.autor);
        System.out.println("Preço: " + book.preco);
        System.out.println("Editora: " + book.editora);
        System.out.println("Gênero: " + book.genero);
        System.out.println("Quant. de páginas: " + book.quantPag);
        System.out.println("Idioma: " + book.idioma);        
    }
    
}

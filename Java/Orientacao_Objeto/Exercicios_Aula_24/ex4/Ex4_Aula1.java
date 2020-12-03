package ex4;

import java.util.Date;
import java.util.Scanner;


public class Ex4_Aula1 {


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Biblioteca book = new Biblioteca();
        
        book.name = "O Hobbit";
        book.autor = "J.R.R Tolkien";
        book.anoLancamento = 1937;
        book.emprestado = true;
        book.dataEntrega = new Date();
        book.emprestadoA = "Sushi";
        
        System.out.println("Nome do livro: " + book.name);
        System.out.println(book.dataEntrega);
        
    }
    
}

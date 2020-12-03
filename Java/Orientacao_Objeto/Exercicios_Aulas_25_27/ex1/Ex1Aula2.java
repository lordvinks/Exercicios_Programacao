package ex1;


public class Ex1Aula2 {

    
    public static void main(String[] args) {
        Lampada lamp = new Lampada();
        
        //modelo
        System.out.print("Qual é o modelo? ");
        lamp.modelo = lamp.verificarString();
        
        //Tensão
        System.out.print("Qual é a tensão? ");
        lamp.tensao = lamp.verificarInt();
        
        //potencia
        System.out.print("Qual é a potencia? ");
        lamp.potencia = lamp.verificarInt();
        
        //Cor
        System.out.print("Qual é a cor? ");
        lamp.cor = lamp.verificarString();
        
        //garantia
        System.out.print("Tempo de garantia: (em meses) ");
        lamp.garantia = lamp.verificarInt();

        //Tipo abajur
        System.out.print("É uma lampada do tipo abajur?(S/N) ");
        lamp.tipoAbajur = lamp.verificarBoolean();
        
        //Verificar se a Lampada está ligada
        System.out.print("Ela está ligada? (S/N): ");
        lamp.ligada = lamp.verificarBoolean();
        
        //Escrever tudo na tela
        lamp.inputLamp();
    }
    
}

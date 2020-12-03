package ex1_aula1;


public class Ex1_Aula1 {


    public static void main(String[] args) {
        
        lampada a60 = new lampada();
        
        a60.tipoAbajur = true;
        System.out.println("Modelo: "+ (a60.modelo="A60"));
        System.out.println("Tensão: "+ (a60.tensao="Bivolt"));
        System.out.println("Potencia: "+ (a60.potencia=7) +'W');
        System.out.println("Cor: "+ (a60.cor="Amarela"));
        System.out.println("Garantia: "+ (a60.garantia=36));
        
        
        
    }
    
}

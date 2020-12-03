
package Exercicio_01;


public class Lampada {
    private boolean statusLampada;
    
    
    public void setLigarLampada(boolean status){
        statusLampada = status;
        }
    
    public boolean getStatusLampada(){
        return statusLampada;
    }
    
    public String statusLampada(int a){ //TRATAMENTO DE TEXTO
        if (a==0){
            return (statusLampada)?"ligada":"desligada";
        } else {
            return (!statusLampada)?"liga-la":"desliga-la";
        }
    }
    
    public void painelEscolha() { // TRATAMENTO DE TEXTO
        String status;
        
        if (statusLampada){status = "DESLIGAR";}
        else {status = "LIGAR";}
        
        System.out.printf("\n 1: " + status + " \n 2: STATUS \n 3: SAIR \n R: ");
    }
    
}

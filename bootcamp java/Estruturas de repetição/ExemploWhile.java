import java.util.concurrent.ThreadLocalRandom;

public class ExemploWhile {
    public static void main(String[] args) {
        double mesada = 50.0;
        while(mesada > 0) {
            double valorDoce = valorAleatorio();
            if(valorDoce > mesada)
            valorDoce = mesada;
            System.out.println("Docedo valor: " + valorDoce + "Adicionar ao carrinho");
              mesada = mesada - valorDoce;
         }
         System.out.println("mesada" + mesada);
         System.out.println("joaozinho gastou toda sua mesada em doce");
    }
    private static double valorAleatorio(){
        return ThreadLocalRandom.current().nextDouble(2, 15);  
  }
}

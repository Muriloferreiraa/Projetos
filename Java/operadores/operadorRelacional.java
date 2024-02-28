public class operadorRelacional {
    public static void main(String[] args) {
     String nomeUm ="gabriel";
     String nomeDois="murilo";
     System.out.println(nomeUm==nomeDois);

     String nomeQuadro ="murilo";
     String nomeTres= new String("murilo");
     System.out.println(nomeTres.equals(nomeQuadro));



        int numero1=1;
        int numero2=2;

        boolean simNao= numero1 == numero2;  
       
        if(numero1<numero2){
            System.out.println("a nossa condicao e verdadeira");
        }
    
        simNao = numero1 != numero2;
        System.out.println("numeroUm diferente de numeroDois?"+simNao);

        simNao = numero1 > numero2;
        System.out.println("numeroUm maior que numeroDois?"+simNao);

        simNao = numero1<numero2;
        System.out.println("numeroUm menor que numeroDois?"+simNao);
    }
}

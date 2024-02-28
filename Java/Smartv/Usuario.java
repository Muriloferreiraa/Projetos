public class Usuario {
    public static void main(String[] args)throws Exception {
             
        Controle controle = new Controle();
       
        controle.diminuirVolume();
        controle.diminuirVolume();
        controle.diminuirVolume();
        controle.aumentarVolume();

        controle.mudarCanal();
        controle.mudarCanal();
        controle.voltarCanal();
        controle.mudarCanal();

        controle.verificaTv();
        controle.verificaCanal();
        controle.verificaVolume();
        controle.ligarDesligar();
        controle.ligarDesligar();
        controle.ligarDesligar();


    }
}

public class Controle {
    Smartv smartv;
    public Controle() {
       smartv = new Smartv();
    }
    public void diminuirVolume() {
        smartv.diminuirVolume();
    }
    public void aumentarVolume() {
        smartv.aumentarVolume();
    }
    public void mudarCanal() {
        smartv.mudarCanal();
    }
    public void voltarCanal() {
        smartv.voltarCanal();
    }
    public void ligarDesligar() {
        smartv.ligarDesligar();
        System.out.println("novo status-> TV ligada ?"+ smartv.ligada);
    }
    public void verificaTv() {
        System.out.println("Tv ligada ?"+smartv.ligada);
    }
    public void verificaCanal() {
        System.out.println("canal atual :"+smartv.canal);
    }
    public void verificaVolume() {
        System.out.println("volume atual:"+smartv.volume);
    }
}

public class Smartv {
  boolean ligada = false;
  int canal = 1;
  int volume = 34;

  public void mudarCanal() {
    if(ligada) {
      canal++;
    }
  }
  public void voltarCanal() {
    if (ligada) {
      canal--;
    }
  }

  public void aumentarVolume() {
   if(ligada) {
    volume++;
   }
  }
  public void diminuirVolume() {
    if(ligada) {
      volume--;
    }else{
      System.out.println("erro");
    }
  }
   public void ligarDesligar() {
    if(ligada) {
      ligada = false;
    } else {
      ligada = true;
    }
   }
}
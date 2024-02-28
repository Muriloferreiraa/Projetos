public class operadorLogico {
    public static void main(String[] args) {
        boolean condicao1=false;
        boolean condicao2=false;

        if(condicao1 && condicao2) {
            System.out.println("as condicoes sao verdadeiras");
        }
        else if(condicao1 || condicao2){
            System.out.println("Uma das duas condicoes e verdadeira");
        }
        else
        System.out.println("as duas sao falsas");
    }
    
}

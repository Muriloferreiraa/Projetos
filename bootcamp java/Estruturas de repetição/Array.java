public class Array {
    public static void main(String[] args) {
        String alunos [] = {"murilo","fabio","gabriel","vitoria","fabricia"};
    //     for(int x=0; x < alunos.length; x++) {
    //         System.out.println("o Aluno no indice x: " + alunos[4]);
    //  }
    for(String aluno : alunos) {
        System.err.println("nome do aluno :" + aluno);

    }
  }   
}

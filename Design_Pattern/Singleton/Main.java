public class Main{
        public static void main(String[] arg){
            System.out.println("Start.");
            Singleton obj1 = Singleton.getInstance();
            Singleton obj2 = Singleton.getInstance();
        
            if(obj1 == obj2) {
                System.out.println("same");
            } else {
                System.out.println("diff");
            }

            return 0;
        }
}
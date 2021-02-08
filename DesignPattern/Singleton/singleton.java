public calss Singleton{
    private static Singleton singleton = new singleton();
    private Singleton(){
        System.out.println("Instance create");
    }
    public static Singleton getInstance(){
        return singleton;
    }
}
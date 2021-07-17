//define a class that has only one instance and provides a global point of access to it

//Advantage of Singleton design pattern
// Saves memory because object is not created at each request. Only single instance is reused again and again.


// Usage of Singleton design pattern
// Singleton pattern is mostly used in multi-threaded and database applications. It is used in logging,
//          caching, thread pools, configuration settings etc.

package patterns;

class Singleton {

    private static Singleton instance = new Singleton();

    private Singleton(){}

    public static Singleton getInstance(){
        return instance;
    }
}

public class PatternSingleton {

    public static void main(String[] args) {
        Singleton singleton = Singleton.getInstance();

        System.out.println(singleton);

        Singleton singleton1 = Singleton.getInstance();

        System.out.println(singleton1);

    }

}

//refer singleton
package patterns;

class ThreadSafeSingleton {

    private static ThreadSafeSingleton instance;
    private static Object mutex = new Object();

    private ThreadSafeSingleton(){}

    public static ThreadSafeSingleton getInstance(){
        ThreadSafeSingleton result = instance;
        if (result == null) {
            synchronized (mutex) {
                result = instance;
                if (result == null)
                    instance = result = new ThreadSafeSingleton();
            }
        }
        return result;
    }


}

class MultithreadingDemo implements Runnable {
    ThreadSafeSingleton threadSafeSingleton;
    MultithreadingDemo(ThreadSafeSingleton threadSafeSingleton){
        this.threadSafeSingleton = threadSafeSingleton;
    }
    public void run()
    {
        try {
            System.out.println(
                    "Thread " + Thread.currentThread().getId()
                            + " is running and instances addr"+threadSafeSingleton);
        }
        catch (Exception e) {
            System.out.println("Exception is caught");
        }
    }
}

public class PatternSingeltonThreadSafe extends Thread {

    public static void main(String[] args) {
        for (int i = 0; i < 4; i++) {
            Thread thread = new Thread(new MultithreadingDemo(ThreadSafeSingleton.getInstance()));
            thread.start();
        }
    }
}

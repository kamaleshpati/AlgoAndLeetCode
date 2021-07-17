//defines a family of functionality, encapsulate each one, and make them interchangeable

//Benefits:
// It provides a substitute to subclassing.
// It defines each behavior within its own class, eliminating the need for conditional statements.
// It makes it easier to extend and incorporate new behavior without changing the application.


//Usage:
// When the multiple classes differ only in their behaviors.e.g. Servlet API.
// It is used when you need different variations of an algorithm.


package patterns;

interface Strategy {
    public int doOperation(int num1, int num2);
}

class OperationAdd implements Strategy{
    @Override
    public int doOperation(int num1, int num2) {
        return num1 + num2;
    }
}

class OperationSubstract implements Strategy{
    @Override
    public int doOperation(int num1, int num2) {
        return num1 - num2;
    }
}

class ContextOps {
    private Strategy strategy;

    public ContextOps(Strategy strategy){
        this.strategy = strategy;
    }

    public int executeStrategy(int num1, int num2){
        return strategy.doOperation(num1, num2);
    }
}



public class PatternStrategy {

    public static void main(String[] args) {
        ContextOps context = new ContextOps(new OperationAdd());
        System.out.println("10 + 5 = " + context.executeStrategy(10, 5));

        context = new ContextOps(new OperationSubstract());
        System.out.println("10 - 5 = " + context.executeStrategy(10, 5));

    }
}

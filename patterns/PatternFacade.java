//just provide a unified and simplified interface to a set of interfaces in a subsystem,
// therefore it hides the complexities of the subsystem from the client


//Advantage of Facade Pattern
// It shields the clients from the complexities of the sub-system components.
// It promotes loose coupling between subsystems and its clients.

//Usage of Facade Pattern:
// When you want to provide simple interface to a complex sub-system.
// When several dependencies exist between clients and the implementation classes of an abstraction.
package patterns;

interface FacadeInterface {
    void draw();
}

class FacadeInterfaceExtend1 implements FacadeInterface {

    @Override
    public void draw() {
        System.out.println("Shape: FacadeInterfaceExtend1");
    }
}

class FacadeInterfaceExtend2 implements FacadeInterface {

    @Override
    public void draw() {
        System.out.println("Shape: FacadeInterfaceExtend2");
    }
}

class FacadeObj {
    private FacadeInterface facadeInterface1;
    private FacadeInterface facadeInterface2;

    public FacadeObj() {
        facadeInterface1 =  new FacadeInterfaceExtend1();
        facadeInterface2 = new FacadeInterfaceExtend2();
    }

    public void draw(){
        facadeInterface1.draw();
        facadeInterface2.draw();
    }
}


public class PatternFacade {
    public static void main(String[] args) {
        FacadeObj facadeObj = new FacadeObj();
        facadeObj.draw();
    }
}

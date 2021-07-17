//define an interface or abstract class for creating an object but let the subclasses decide which class to instantiate.

//Advantage of Factory Design Pattern
//Factory Method Pattern allows the sub-classes to choose the type of objects to create.
//It promotes the loose-coupling by eliminating the need to bind application-specific classes into the code. That means the code interacts solely with the resultant interface or abstract class, so that it will work with any classes that implement that interface or that extends that abstract class.


//Usage of Factory Design Pattern
//When a class doesn't know what sub-classes will be required to create
//When a class wants that its sub-classes specify the objects to be created.
//When the parent classes choose the creation of objects to its sub-classes

package patterns;

interface FactoryInterface{
    void draw();
}

class FactoryExtend1 implements FactoryInterface {
    int value1;
    public FactoryExtend1(int val){
        this.value1 = val;
    }
    @Override
    public void draw() {
        System.out.println("Inside FactoryExtend1::draw() method. "+this.value1);
    }
}



class FactoryExtend2 implements FactoryInterface {
    int value1,value2;
    public FactoryExtend2(int val1,int val2){
        this.value1 = val1;
        this.value2 = val2;
    }
    @Override
    public void draw() {
        System.out.println("Inside FactoryExtend2::draw() method. "+this.value1+" "+this.value2);
    }
}


public class PatternFactory {
    public static void main(String[] args) {
        FactoryInterface factoryExtend1 = new FactoryExtend1(1);
        factoryExtend1.draw();

        FactoryInterface factoryExtend2 = new FactoryExtend2(1,2);
        factoryExtend2.draw();
    }
}

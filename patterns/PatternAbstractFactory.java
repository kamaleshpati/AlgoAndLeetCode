//define an interface or abstract class for creating families of related (or dependent) objects but without specifying their concrete sub-classes.


//Advantage of Abstract Factory Pattern
// Abstract Factory Pattern isolates the client code from concrete (implementation) classes.
// It eases the exchanging of object families.
// It promotes consistency among objects.


// Usage of Abstract Factory Pattern
// When the system needs to be independent of how its object are created, composed, and represented.
// When the family of related objects has to be used together, then this constraint needs to be enforced.
// When you want to provide a library of objects that does not show implementations and only reveals interfaces.
// When the system needs to be configured with one of a multiple family of objects.

package patterns;

interface AbstractFactoryInterface{
    void draw();
}

class AbstractFactoryExtend1 implements AbstractFactoryInterface {
    int value1;
    public AbstractFactoryExtend1(int val){
        this.value1 = val;
    }
    @Override
    public void draw() {
        System.out.println("Inside FactoryExtend1::draw() method. "+this.value1);
    }
}



class AbstractFactoryExtend2 implements AbstractFactoryInterface {
    int value1;
    public AbstractFactoryExtend2(int val){
        this.value1 = val;
    }
    @Override
    public void draw() {
        System.out.println("Inside FactoryExtend2::draw() method. "+this.value1);
    }
}


interface AbstractFactoryProduce {
    AbstractFactoryInterface getShape(String shapeType) ;
}

class AbstractFactoryProduceExtend1 implements AbstractFactoryProduce {
    @Override
    public AbstractFactoryInterface getShape(String shapeType) {
        AbstractFactoryInterface abstractFactoryInterface = null;
        if(shapeType.equalsIgnoreCase("RECTANGLE")){
            abstractFactoryInterface = new AbstractFactoryExtend1(1);
        }else if(shapeType.equalsIgnoreCase("SQUARE")){
            abstractFactoryInterface = new AbstractFactoryExtend2(2);
        }
        return abstractFactoryInterface;
    }
}




public class PatternAbstractFactory {

    public static void main(String[] args) {
        AbstractFactoryProduce abstractFactoryProduce = new AbstractFactoryProduceExtend1();
        abstractFactoryProduce.getShape("RECTANGLE").draw();
        abstractFactoryProduce.getShape("SQUARE").draw();

    }
}

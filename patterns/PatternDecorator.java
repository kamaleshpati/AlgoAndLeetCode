//attach a flexible additional responsibilities to an object dynamically

//Advantage of Decorator Pattern
// It provides greater flexibility than static inheritance.
// It enhances the extensibility of the object, because changes are made by coding new classes.
// It simplifies the coding by allowing you to develop a series of functionality from targeted classes
//          instead of coding all of the behavior into the object.

//Usage of Decorator Pattern
// When you want to transparently and dynamically add responsibilities to objects without affecting other objects.
// When you want to add responsibilities to an object that you may want to change in future.
// Extending functionality by sub-classing is no longer practical.
package patterns;

interface DecoratorInterface {
    void draw();
}

class DecoratorInterfaceExtend1 implements DecoratorInterface {

    @Override
    public void draw() {
        System.out.println("Shape: DecoratorInterfaceExtend1");
    }
}

class DecoratorInterfaceExtend2 implements DecoratorInterface {

    @Override
    public void draw() {
        System.out.println("Shape: DecoratorInterfaceExtend2");
    }
}

abstract class DecoratorInterfaceAbstract implements DecoratorInterface {
    protected DecoratorInterface decoratorInterface;

    public DecoratorInterfaceAbstract(DecoratorInterface decoratorInterface){
        this.decoratorInterface = decoratorInterface;
    }

    public void draw(){
        decoratorInterface.draw();
    }
}

class DecoratorInterfaceAbstractExtend extends DecoratorInterfaceAbstract {

    public DecoratorInterfaceAbstractExtend(DecoratorInterface decoratorInterface) {
        super(decoratorInterface);
    }

    @Override
    public void draw() {
        decoratorInterface.draw();
        setRedBorder(decoratorInterface);
    }

    private void setRedBorder(DecoratorInterface decoratorInterface){
        System.out.println("Border Color: Red");
    }
}



public class PatternDecorator {
    public static void main(String[] args) {

        DecoratorInterface circle = new DecoratorInterfaceExtend1();

        DecoratorInterface redCircle = new DecoratorInterfaceAbstractExtend(new DecoratorInterfaceExtend1());

        DecoratorInterface redRectangle = new DecoratorInterfaceAbstractExtend(new DecoratorInterfaceExtend2());

        System.out.println("Circle with normal border");
        circle.draw();

        System.out.println("\nCircle of red border");
        redCircle.draw();

        System.out.println("\nRectangle of red border");
        redRectangle.draw();
    }
}

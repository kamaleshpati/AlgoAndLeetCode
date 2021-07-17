//cloning of an existing object instead of creating new one and can also be customized as per the requirement

//Advantage
// It reduces the need of sub-classing.
// It hides complexities of creating objects.
// The clients can get new objects without knowing which type of object it will be.
// It lets you add or remove objects at runtime.


//Usage of Prototype Pattern
// When the classes are instantiated at runtime.
// When the cost of creating an object is expensive or complicated.
// When you want to keep the number of classes in an application minimum.
// When the client application needs to be unaware of object creation and representation.
package patterns;

import java.util.Hashtable;

abstract class PrototypeAbstract implements Cloneable {

    private String id;
    protected String type;

    abstract void draw();

    public String getType(){
        return type;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Object clone() {
        Object clone = null;

        try {
            clone = super.clone();

        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }

        return clone;
    }
}


class PrototypeAbstractExtend1 extends PrototypeAbstract {

    public PrototypeAbstractExtend1(){
        type = "PrototypeAbstractExtend1";
    }

    @Override
    public void draw() {
        System.out.println("Inside PrototypeAbstractExtend1::draw() method.");
    }
}

class PrototypeAbstractExtend2 extends PrototypeAbstract {

    public PrototypeAbstractExtend2(){
        type = "PrototypeAbstractExtend2";
    }

    @Override
    public void draw() {
        System.out.println("Inside PrototypeAbstractExtend2::draw() method.");
    }
}

class PrototypeAbstractExtend3 extends PrototypeAbstract {

    public PrototypeAbstractExtend3(){
        type = "PrototypeAbstractExtend3";
    }

    @Override
    public void draw() {
        System.out.println("Inside PrototypeAbstractExtend3::draw() method.");
    }
}


class PrototypeAbstractCache {

    private static Hashtable<String, PrototypeAbstract> prototypeAbstractMap  = new Hashtable<>();

    public static PrototypeAbstract getShape(String shapeId) {
        PrototypeAbstract cached = prototypeAbstractMap.get(shapeId);
        return (PrototypeAbstract) cached.clone();
    }


    public static void loadCache() {
        PrototypeAbstractExtend1 extend1 = new PrototypeAbstractExtend1();
        extend1.setId("1");
        prototypeAbstractMap.put(extend1.getId(),extend1);

        PrototypeAbstractExtend2 extend2 = new PrototypeAbstractExtend2();
        extend2.setId("2");
        prototypeAbstractMap.put(extend2.getId(),extend2);

        PrototypeAbstractExtend3 extend3 = new PrototypeAbstractExtend3();
        extend3.setId("3");
        prototypeAbstractMap.put(extend3.getId(),extend3);

    }
}

public class PatternPrototype {

    public static void main(String[] args) {
        PrototypeAbstractCache.loadCache();

        PrototypeAbstract cloned = PrototypeAbstractCache.getShape("1");
        System.out.println("clone : " + cloned.getType());

        cloned = PrototypeAbstractCache.getShape("2");
        System.out.println("clone : " + cloned.getType());

        cloned = PrototypeAbstractCache.getShape("3");
        System.out.println("clone : " + cloned.getType());
    }
}

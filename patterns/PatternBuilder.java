//construct a complex object from simple objects using step-by-step approach

//Advantages
//It provides clear separation between the construction and representation of an object.
//It provides better control over construction process.
//It supports to change the internal representation of objects.

package patterns;

import java.util.ArrayList;
import java.util.List;

interface BuilderInterface {
    public String name();
    public BuilderInterfacePart showing();
}

interface BuilderInterfacePart {
    public String show();
}

class BuilderInterfacePartExtend1 implements BuilderInterfacePart {

    @Override
    public String show() {
        return "BuilderInterfacePartExtend1";
    }
}

class BuilderInterfacePartExtend2 implements BuilderInterfacePart {

    @Override
    public String show() {
        return "BuilderInterfacePartExtend2";
    }
}

abstract class BuilderInterfaceAbstract1 implements BuilderInterface {
//    @Override
//    public abstract String name();

    public BuilderInterfacePart showing(){
        return new BuilderInterfacePartExtend1();
    }

}


abstract class BuilderInterfaceAbstract2 implements BuilderInterface {
//    @Override
//    public abstract String name();

    public BuilderInterfacePart showing(){
        return new BuilderInterfacePartExtend2();
    }

}


class BuilderInterfaceAbstract1Extend extends BuilderInterfaceAbstract1{

    @Override
    public String name() {
        return "BuilderInterfaceAbstract1Extend";
    }
}


class BuilderInterfaceAbstract2Extend extends BuilderInterfaceAbstract2{

    @Override
    public String name() {
        return "BuilderInterfaceAbstract2Extend";
    }
}


class BuilderObject{
    private List<BuilderInterface> items = new ArrayList<>();

    public void addItem(BuilderInterface builderInterface){
        items.add(builderInterface);
    }

    public void showItems(){

        for (BuilderInterface item : items) {
            System.out.print("Item : " + item.name());
            System.out.print(", showing : " + item.showing().show());
        }
    }
}



public class PatternBuilder {

    public static void main(String[] args) {
        BuilderObject builderObject = new BuilderObject();
        builderObject.addItem(new BuilderInterfaceAbstract1Extend());
        builderObject.addItem(new BuilderInterfaceAbstract2Extend());

        builderObject.showItems();

    }


}

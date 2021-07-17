//decouple the functional abstraction from the implementation so that the two can vary independently


//Advantage of Bridge Pattern
// It enables the separation of implementation from the interface.
// It improves the extensibility.
// It allows the hiding of implementation details from the client.


// Usage of Bridge Pattern
// When you don't want a permanent binding between the functional abstraction and its implementation.
// When both the functional abstraction and its implementation need to extended using sub-classes.
// It is mostly used in those places where changes are made in the implementation does not affect the clients.

package patterns;


interface BridgeInterface {
    void draw(int radius, int x, int y);
}

class BridgeInterfaceExtend1 implements BridgeInterface {
    @Override
    public void draw(int radius, int x, int y) {
        System.out.println("Drawing shape[ color: red, radius: " + radius + ", x: " + x + ", " + y + "]");
    }
}


class BridgeInterfaceExtend2 implements BridgeInterface {
    @Override
    public void draw(int radius, int x, int y) {
        System.out.println("Drawing shape[ color: blue, radius: " + radius + ", x: " + x + ", " + y + "]");
    }
}

abstract class BridgeAbstract {
    protected BridgeInterface bridgeInterface;

    protected BridgeAbstract(BridgeInterface bridgeInterface){
        this.bridgeInterface = bridgeInterface;
    }
    public abstract void drawAbstract();
}

class BridgeAbstractExtend extends BridgeAbstract {
    private int x, y, radius;

    public BridgeAbstractExtend(int x, int y, int radius, BridgeInterface bridgeInterface) {
        super(bridgeInterface);
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    @Override
    public void drawAbstract() {
        bridgeInterface.draw(radius,x,y);
    }
}

public class PatternBridge {

    public static void main(String[] args) {
        BridgeAbstract bridgeAbstract1 = new BridgeAbstractExtend(100,100, 10, new BridgeInterfaceExtend1());
        BridgeAbstract bridgeAbstract2 = new BridgeAbstractExtend(100,100, 10, new BridgeInterfaceExtend2());
        bridgeAbstract1.drawAbstract();
        bridgeAbstract2.drawAbstract();
    }
}

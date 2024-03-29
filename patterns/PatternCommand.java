//encapsulate a request under an object as a command and pass it to invoker object.
// Invoker object looks for the appropriate object which can handle this command and pass the command to
// the corresponding object and that object executes the command


//Advantage of command pattern
// It separates the object that invokes the operation from the object that actually performs the operation.
// It makes easy to add new commands, because existing classes remain unchanged.


//usage
//When you need parameterize objects according to an action perform.
// When you need to create and execute requests at different times.
// When you need to support rollback, logging or transaction functionality
package patterns;


import java.util.ArrayList;
import java.util.List;

interface Order {
    void execute();
}

class Stock {

    private String name = "ABC";
    private int quantity = 10;

    public void buy(){
        System.out.println("Stock [ Name: "+name+", Quantity: " + quantity +" ] bought");
    }
    public void sell(){
        System.out.println("Stock [ Name: "+name+", Quantity: " + quantity +" ] sold");
    }
}

class BuyStock implements Order {
    private Stock abcStock;

    public BuyStock(Stock abcStock){
        this.abcStock = abcStock;
    }

    public void execute() {
        abcStock.buy();
    }
}

class SellStock implements Order {
    private Stock abcStock;

    public SellStock(Stock abcStock){
        this.abcStock = abcStock;
    }

    public void execute() {
        abcStock.sell();
    }
}

class Broker {
    private List<Order> orderList = new ArrayList<Order>();

    public void takeOrder(Order order){
        orderList.add(order);
    }

    public void placeOrders(){

        for (Order order : orderList) {
            order.execute();
        }
        orderList.clear();
    }
}



public class PatternCommand {
    public static void main(String[] args) {
        Stock abcStock = new Stock();

        BuyStock buyStockOrder = new BuyStock(abcStock);
        SellStock sellStockOrder = new SellStock(abcStock);

        Broker broker = new Broker();
        broker.takeOrder(buyStockOrder);
        broker.takeOrder(sellStockOrder);

        broker.placeOrders();
    }
}

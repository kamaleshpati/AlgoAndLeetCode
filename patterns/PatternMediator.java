//to define an object that encapsulates how a set of objects interact

//Benefits:
// It decouples the number of classes.
// It simplifies object protocols.
// It centralizes the control.
// The individual components become simpler and much easier to deal with because they don't need to pass messages to one another.
// The components don't need to contain logic to deal with their intercommunication and therefore, they are more generic.

//Usage
//It is commonly used in message-based systems likewise chat applications.
// When the set of objects communicate in complex but in well-defined ways.
package patterns;

import java.util.Date;

class ChatRoom {
    public static void showMessage(User user, String message){
        System.out.println(new Date().toString() + " [" + user.getName() + "] : " + message);
    }
}

class User {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public User(String name){
        this.name  = name;
    }

    public void sendMessage(String message){
        ChatRoom.showMessage(this,message);
    }
}

public class PatternMediator {
    public static void main(String[] args) {
        User robert = new User("Robert");
        User john = new User("John");

        robert.sendMessage("Hi! John!");
        john.sendMessage("Hello! Robert!");
    }
}

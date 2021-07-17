package patterns;

class EmailService {

    public void sendEmail(String message, String receiver){
        //logic to send email
        System.out.println("Email sent to "+receiver+ " with Message="+message);
    }
}

class MyApplication {

    private EmailService email = new EmailService();

    public void processMessages(String msg, String rec){
        //do some msg validation, manipulation logic etc
        this.email.sendEmail(msg, rec);
    }
}

class MyApplicationUpgrade1 {

    private EmailService email = null;

    public MyApplicationUpgrade1(EmailService svc){
        this.email=svc;
    }

    public void processMessages(String msg, String rec){
        //do some msg validation, manipulation logic etc
        this.email.sendEmail(msg, rec);
    }
}

interface MessageService {

    void sendMessage(String msg, String rec);
}

class EmailServiceImpl implements MessageService {

    @Override
    public void sendMessage(String msg, String rec) {
        //logic to send email
        System.out.println("Email sent to "+rec+ " with Message="+msg);
    }

}

class SMSServiceImpl implements MessageService {

    @Override
    public void sendMessage(String msg, String rec) {
        //logic to send SMS
        System.out.println("SMS sent to "+rec+ " with Message="+msg);
    }

}

interface Consumer {

    void processMessages(String msg, String rec);
}

class MyDIApplication implements Consumer{

    private MessageService service;

    public MyDIApplication(MessageService svc){
        this.service=svc;
    }

    @Override
    public void processMessages(String msg, String rec){
        //do some msg validation, manipulation logic etc
        this.service.sendMessage(msg, rec);
    }

}

interface MessageServiceInjector {

    public Consumer getConsumer();
}

class EmailServiceInjector implements MessageServiceInjector {

    @Override
    public Consumer getConsumer() {
        return new MyDIApplication(new EmailServiceImpl());
    }

}


class SMSServiceInjector implements MessageServiceInjector {

    @Override
    public Consumer getConsumer() {
        return new MyDIApplication(new SMSServiceImpl());
    }

}




public class PatternDependencyInjection {
    public static void main(String[] args) {
        MyApplication app = new MyApplication();
        app.processMessages("Hi Pankaj", "pankaj@abc.com");


        String msg = "Hi Pankaj";
        String email = "pankaj@abc.com";
        String phone = "4088888888";
        MessageServiceInjector injector = null;
        Consumer capp = null;

        //Send email
        injector = new EmailServiceInjector();
        capp = injector.getConsumer();
        capp.processMessages(msg, email);

        //Send SMS
        injector = new SMSServiceInjector();
        capp = injector.getConsumer();
        capp.processMessages(msg, phone);
    }
}

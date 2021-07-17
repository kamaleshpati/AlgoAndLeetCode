//decouple presentation tier and business tier. It is basically use to reduce communication or remote lookup
// functionality to business tier code in presentation tier code
package patterns;


interface BusinessService {
    public void doProcessing();
}

class EJBService implements BusinessService {

    @Override
    public void doProcessing() {
        System.out.println("Processing task by invoking EJB Service");
    }
}

class JMSService implements BusinessService {

    @Override
    public void doProcessing() {
        System.out.println("Processing task by invoking JMS Service");
    }
}

class BusinessLookUp {
    public BusinessService getBusinessService(String serviceType){

        if(serviceType.equalsIgnoreCase("EJB")){
            return new EJBService();
        }
        else {
            return new JMSService();
        }
    }
}

class BusinessDelegate {
    private BusinessLookUp lookupService = new BusinessLookUp();
    private BusinessService businessService;
    private String serviceType;

    public void setServiceType(String serviceType){
        this.serviceType = serviceType;
    }

    public void doTask(){
        businessService = lookupService.getBusinessService(serviceType);
        businessService.doProcessing();
    }
}

class ClientBusinessDelegate {

    BusinessDelegate businessService;

    public ClientBusinessDelegate(BusinessDelegate businessService){
        this.businessService  = businessService;
    }

    public void doTask(){
        businessService.doTask();
    }
}
public class PatternBusinnesDelegate {
    public static void main(String[] args) {

        BusinessDelegate businessDelegate = new BusinessDelegate();
        businessDelegate.setServiceType("EJB");

        ClientBusinessDelegate client = new ClientBusinessDelegate(businessDelegate);
        client.doTask();

        businessDelegate.setServiceType("JMS");
        client.doTask();
    }
}

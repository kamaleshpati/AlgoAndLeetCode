//provides the control for accessing the original object

//Advantage of Proxy Pattern
// It provides the protection to the original object from the outside world.

//Usage of Proxy Pattern:
// It can be used in Virtual Proxy scenario---Consider a situation where there is multiple
//          database call to extract huge size image. Since this is an expensive operation
//          so here we can use the proxy pattern which would create multiple proxies and point to
//          the huge size memory consuming object for further processing. The real object gets created
//          only when a client first requests/accesses the object and after that we can just refer to the proxy
//          to reuse the object. This avoids duplication of the object and hence saving memory.
// It can be used in Protective Proxy scenario---It acts as an authorization layer to verify that whether the actual
//          user has access the appropriate content or not. For example, a proxy server which provides restriction on
//          internet access in office. Only the websites and contents which are valid will be allowed and the remaining ones will be blocked.
// It can be used in Remote Proxy scenario---A remote proxy can be thought about the stub in the RPC call. The remote
//          proxy provides a local representation of the object which is present in the different address location.
//          Another example can be providing interface for remote resources such as web service or REST resources.
// It can be used in Smart Proxy scenario---A smart proxy provides additional layer of security by interposing
//          specific actions when the object is accessed. For example, to check whether the real object is locked or
//          not before accessing it so that no other objects can change it.
package patterns;

interface ProxyInterface {
    void display();
}

class ProxyInterfaceExtend implements ProxyInterface {

    private String fileName;

    public ProxyInterfaceExtend(String fileName){
        this.fileName = fileName;
        loadFromDisk(fileName);
    }

    @Override
    public void display() {
        System.out.println("Displaying " + fileName);
    }

    private void loadFromDisk(String fileName){
        System.out.println("Loading " + fileName);
    }
}


class ProxyInterfaceExtender implements ProxyInterface{

    private ProxyInterfaceExtend proxyInterfaceExtend;
    private String fileName;

    public ProxyInterfaceExtender(String fileName){
        this.fileName = fileName;
    }

    @Override
    public void display() {
        if(proxyInterfaceExtend == null){
            proxyInterfaceExtend = new ProxyInterfaceExtend(fileName);
        }
        proxyInterfaceExtend.display();
    }
}

public class PatternProxy {

    public static void main(String[] args) {
        ProxyInterface image = new ProxyInterfaceExtender("test_10mb.jpg");

        //image will be loaded from disk
        image.display();
        System.out.println("");

        //image will not be loaded from disk
        image.display();
    }
}

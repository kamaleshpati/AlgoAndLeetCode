//converts the interface of a class into another interface that a client wants
//to provide the interface according to client requirement while using the services of a class with a different interface

//Advantage of Adapter Pattern
// It allows two or more previously incompatible objects to interact.
// It allows reusability of existing functionality.


// Usage of Adapter pattern:
// When an object needs to utilize an existing class with an incompatible interface.
// When you want to create a reusable class that cooperates with classes which don't have compatible interfaces.
// When you want to create a reusable class that cooperates with classes which don't have compatible interfaces.
package patterns;

interface AdapterInterface {
    public void play(String type, String fileName);
}

interface AdvancedAdapterInterface {
    public void playCustom1(String fileName);
    public void playCustom2(String fileName);
}

class AdvancedAdapterInterfaceExtend1 implements AdvancedAdapterInterface{
    @Override
    public void playCustom1(String fileName) {
        System.out.println("Playing custom1 file. Name: "+ fileName);
    }

    @Override
    public void playCustom2(String fileName) {
        System.out.println("Playing custom2 file. Name: does nothing says "+ fileName);
    }
}


class AdvancedAdapterInterfaceExtend2 implements AdvancedAdapterInterface{
    @Override
    public void playCustom1(String fileName) {
        System.out.println("Playing custom2 file. Name: does nothing says "+ fileName);
    }

    @Override
    public void playCustom2(String fileName) {
        System.out.println("Playing custom1 file. Name: "+ fileName);

    }
}


class AdapterInterfaceExtend implements AdapterInterface {

    AdvancedAdapterInterface advancedAdapterInterface;

    public AdapterInterfaceExtend(String audioType){

        if(audioType.equalsIgnoreCase("FILE1") ){
            advancedAdapterInterface = new AdvancedAdapterInterfaceExtend1();

        }else if (audioType.equalsIgnoreCase("FILE2")){
            advancedAdapterInterface = new AdvancedAdapterInterfaceExtend2();
        }
    }

    @Override
    public void play(String audioType, String fileName) {

        if(audioType.equalsIgnoreCase("FILE1")){
            advancedAdapterInterface.playCustom1(fileName);
        }
        else if(audioType.equalsIgnoreCase("FILE2")){
            advancedAdapterInterface.playCustom2(fileName);
        }
    }
}


class AdapterInterfaceExtendCustomer implements AdapterInterface {
    AdapterInterfaceExtend adapterInterfaceExtend;

    @Override
    public void play(String audioType, String fileName) {
        if(audioType.equalsIgnoreCase("FILE@")){
            System.out.println("Playing  file Support. Name: " + fileName);
        }

        //mediaAdapter is providing support to play other file formats
        else if(audioType.equalsIgnoreCase("FILE1") || audioType.equalsIgnoreCase("FILE2")){
            adapterInterfaceExtend = new AdapterInterfaceExtend(audioType);
            adapterInterfaceExtend.play(audioType, fileName);
        }

        else{
            System.out.println("Invalid media. " + audioType + " format not supported");
        }
    }
}


public class PatternAdapter {
    public static void main(String[] args) {
        AdapterInterfaceExtendCustomer adapterInterfaceExtendCustomer =
                new AdapterInterfaceExtendCustomer();

        adapterInterfaceExtendCustomer.play("FILE1", "beyond the horizon.mp3");
        adapterInterfaceExtendCustomer.play("FILE2", "alone.mp4");
        adapterInterfaceExtendCustomer.play("FILE3", "far far away.vlc");
        adapterInterfaceExtendCustomer.play("FILE@", "mind me.avi");
    }
}

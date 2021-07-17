//to access the elements of an aggregate object sequentially without exposing its underlying implementation

//Advantage of Iterator Pattern
// It supports variations in the traversal of a collection.
// It simplifies the interface to the collection.

//Usage of Iterator Pattern:
// When you want to access a collection of objects without exposing its internal representation.
// When there are multiple traversals of objects need to be supported in the collection.
package patterns;

interface Iterator {
    public boolean hasNext();
    public Object next();
}

interface Container {
    public Iterator getIterator();
}

class NameRepository implements Container {
    public String names[] = {"Robert" , "John" ,"Julie" , "Lora"};

    @Override
    public Iterator getIterator() {
        return new NameIterator();
    }

    private class NameIterator implements Iterator {

        int index;

        @Override
        public boolean hasNext() {

            if(index < names.length){
                return true;
            }
            return false;
        }

        @Override
        public Object next() {

            if(this.hasNext()){
                return names[index++];
            }
            return null;
        }
    }
}

public class PatternIterator {
    public static void main(String[] args) {
        NameRepository namesRepository = new NameRepository();

        for(Iterator iter = namesRepository.getIterator(); iter.hasNext();){
            String name = (String)iter.next();
            System.out.println("Name : " + name);
        }
    }
}

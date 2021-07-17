//enables developers to filter a set of objects using different criteria and chaining them in a decoupled way through logical operations

package patterns;

import java.util.ArrayList;
import java.util.List;

class FilterRootObj {

    private String name;
    private String gender;
    private String maritalStatus;

    public FilterRootObj(String name, String gender, String maritalStatus){
        this.name = name;
        this.gender = gender;
        this.maritalStatus = maritalStatus;
    }

    public String getName() {
        return name;
    }
    public String getGender() {
        return gender;
    }
    public String getMaritalStatus() {
        return maritalStatus;
    }
}

interface Criteria {
    public List<FilterRootObj> meetCriteria(List<FilterRootObj> filterRootObjList);
}

class CriteriaMale implements Criteria {

    @Override
    public List<FilterRootObj> meetCriteria(List<FilterRootObj> filterRootObjList) {
        List<FilterRootObj> malePersons = new ArrayList<>();

        for (FilterRootObj person : filterRootObjList) {
            if(person.getGender().equalsIgnoreCase("MALE")){
                malePersons.add(person);
            }
        }
        return malePersons;
    }
}

class CriteriaFemale implements Criteria {

    @Override
    public List<FilterRootObj> meetCriteria(List<FilterRootObj> filterRootObjList) {
        List<FilterRootObj> femalePersons = new ArrayList<>();

        for (FilterRootObj person : filterRootObjList) {
            if(person.getGender().equalsIgnoreCase("FEMALE")){
                femalePersons.add(person);
            }
        }
        return femalePersons;
    }
}

class CriteriaSingle implements Criteria {

    @Override
    public List<FilterRootObj> meetCriteria(List<FilterRootObj> filterRootObjList) {
        List<FilterRootObj> singlePersons = new ArrayList<>();

        for (FilterRootObj person : filterRootObjList) {
            if(person.getMaritalStatus().equalsIgnoreCase("SINGLE")){
                singlePersons.add(person);
            }
        }
        return singlePersons;
    }
}


public class PatternFilter {
    public static void main(String[] args) {
        List<FilterRootObj> persons = new ArrayList<>();

        persons.add(new FilterRootObj("Robert","Male", "Single"));
        persons.add(new FilterRootObj("John", "Male", "Married"));
        persons.add(new FilterRootObj("Laura", "Female", "Married"));
        persons.add(new FilterRootObj("Diana", "Female", "Single"));
        persons.add(new FilterRootObj("Mike", "Male", "Single"));
        persons.add(new FilterRootObj("Bobby", "Male", "Single"));

        Criteria male = new CriteriaMale();
        Criteria female = new CriteriaFemale();
        Criteria single = new CriteriaSingle();


        System.out.println("Males: ");
        printPersons(male.meetCriteria(persons));

        System.out.println("\nFemales: ");
        printPersons(female.meetCriteria(persons));

        System.out.println("\nSingle: ");
        printPersons(single.meetCriteria(persons));


    }

    public static void printPersons(List<FilterRootObj> persons){

        for (FilterRootObj person : persons) {
            System.out.println("Person : [ Name : " + person.getName() + ", Gender : " + person.getGender() + ", Marital Status : " + person.getMaritalStatus() + " ]");
        }
    }
}

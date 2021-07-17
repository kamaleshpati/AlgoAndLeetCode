package patterns;


import java.util.ArrayList;
import java.util.List;

class StudentObj {
    private String name;
    private int rollNo;

    StudentObj(String name, int rollNo){
        this.name = name;
        this.rollNo = rollNo;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getRollNo() {
        return rollNo;
    }

    public void setRollNo(int rollNo) {
        this.rollNo = rollNo;
    }
}

interface StudentDao {
    public List<StudentObj> getAllStudents();
    public StudentObj getStudent(int rollNo);
    public void updateStudent(StudentObj student);
    public void deleteStudent(StudentObj student);
}

class StudentDaoImpl implements StudentDao {

    //list is working as a database
    List<StudentObj> students;

    public StudentDaoImpl(){
        students = new ArrayList<>();
        StudentObj student1 = new StudentObj("Robert",0);
        StudentObj student2 = new StudentObj("John",1);
        students.add(student1);
        students.add(student2);
    }
    @Override
    public void deleteStudent(StudentObj student) {
        students.remove(student.getRollNo());
        System.out.println("Student: Roll No " + student.getRollNo() + ", deleted from database");
    }

    //retrive list of students from the database
    @Override
    public List<StudentObj> getAllStudents() {
        return students;
    }

    @Override
    public StudentObj getStudent(int rollNo) {
        return students.get(rollNo);
    }

    @Override
    public void updateStudent(StudentObj student) {
        students.get(student.getRollNo()).setName(student.getName());
        System.out.println("Student: Roll No " + student.getRollNo() + ", updated in the database");
    }

}

public class PatternDAO {
    public static void main(String[] args) {
        StudentDao studentDao = new StudentDaoImpl();

        //print all students
        for (StudentObj student : studentDao.getAllStudents()) {
            System.out.println("Student: [RollNo : " + student.getRollNo() + ", Name : " + student.getName() + " ]");
        }


        //update student
        StudentObj student =studentDao.getAllStudents().get(0);
        student.setName("Michael");
        studentDao.updateStudent(student);

        //get the student
        studentDao.getStudent(0);
        System.out.println("Student: [RollNo : " + student.getRollNo() + ", Name : " + student.getName() + " ]");
    }
}

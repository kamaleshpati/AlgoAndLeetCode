// to reuse the object that are expensive to create
//an Object pool is a container which contains a specified amount of objects.
// When an object is taken from the pool, it is not available in the pool until it is put back.
// Objects in the pool have a lifecycle: creation, validation and destroy.



//Advantage of Object Pool design pattern
// It boosts the performance of the application significantly.
// It is most effective in a situation where the rate of initializing a class instance is high.
// It manages the connections and provides a way to reuse and share them.
// It can also provide the limit for the maximum number of objects that can be created.

// Usage:
// When an application requires objects which are expensive to create.
//          Eg: there is a need of opening too many connections for the database then it takes too longer to create a
//          new one and the database server will be overloaded.
// When there are several clients who need the same resource at different times.

package patterns;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Enumeration;
import java.util.Hashtable;

abstract class ObjectPool<T> {
    long deadTime;

    Hashtable<T, Long> lock, unlock;

    ObjectPool()
    {
        deadTime = 50000;
        lock = new Hashtable<>();
        unlock = new Hashtable<>();
    }

    abstract T create();

    abstract boolean validate(T o);

    abstract void dead(T o);

    synchronized T takeOut()
    {
        long now = System.currentTimeMillis();
        T t;
        if (unlock.size() > 0) {
            Enumeration<T> e = unlock.keys();
            while (e.hasMoreElements()) {
                t = e.nextElement();
                if ((now - unlock.get(t)) > deadTime) {
                    // object has dead
                    unlock.remove(t);
                    dead(t);
                    t = null;
                }
                else {
                    if (validate(t)) {
                        unlock.remove(t);
                        lock.put(t, now);
                        return (t);
                    }
                    else {
                        // object failed validation
                        unlock.remove(t);
                        dead(t);
                        t = null;
                    }
                }
            }
        }
        // no objects available, create a new one
        t = create();
        lock.put(t, now);
        return (t);
    }
    synchronized void takeIn(T t)
    {
        lock.remove(t);
        unlock.put(t, System.currentTimeMillis());
    }
}


class JDBCConnectionPool extends ObjectPool<Connection> {
    String dsn, usr, pwd;

    JDBCConnectionPool(String driver, String dsn, String usr, String pwd)
    {
        super();
        try {
            Class.forName(driver).newInstance();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        this.dsn = dsn;
        this.usr = usr;
        this.pwd = pwd;
    }

    Connection create()
    {
        try {
            return (DriverManager.getConnection(dsn, usr, pwd));
        }
        catch (SQLException e) {
            e.printStackTrace();
            return (null);
        }
    }

    void dead(Connection o)
    {
        try {
            ((Connection)o).close();
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }

    boolean validate(Connection o)
    {
        try {
            return (!((Connection)o).isClosed());
        }
        catch (SQLException e) {
            e.printStackTrace();
            return (false);
        }
    }
}

public class PatternObjectPool {

    public static void main(String[] args)
    {
        JDBCConnectionPool pool = new JDBCConnectionPool(
                "org.hsqldb.jdbcDriver", "jdbc:hsqldb: //localhost/mydb",
                "sa", "password");

        Connection con = pool.takeOut();
        pool.takeIn(con);
    }
}

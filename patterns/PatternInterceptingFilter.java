//used when we want to do some pre-processing / post-processing with request or response of the application
package patterns;

import java.util.ArrayList;
import java.util.List;

interface InterceptingFilterInterface {
    public void execute(String request);
}

class AuthenticationFilter implements InterceptingFilterInterface {
    public void execute(String request){
        System.out.println("Authenticating request: " + request);
    }
}

class DebugFilter implements InterceptingFilterInterface {
    public void execute(String request){
        System.out.println("request log: " + request);
    }
}

class Target {
    public void execute(String request){
        System.out.println("Executing request: " + request);
    }
}

class FilterChain {
    private List<InterceptingFilterInterface> filters = new ArrayList<>();
    private Target target;

    public void addFilter(InterceptingFilterInterface filter){
        filters.add(filter);
    }

    public void execute(String request){
        for (InterceptingFilterInterface filter : filters) {
            filter.execute(request);
        }
        target.execute(request);
    }

    public void setTarget(Target target){
        this.target = target;
    }
}

class FilterManager {
    FilterChain filterChain;

    public FilterManager(Target target){
        filterChain = new FilterChain();
        filterChain.setTarget(target);
    }
    public void setFilter(InterceptingFilterInterface filter){
        filterChain.addFilter(filter);
    }

    public void filterRequest(String request){
        filterChain.execute(request);
    }
}

class Client {
    FilterManager filterManager;

    public void setFilterManager(FilterManager filterManager){
        this.filterManager = filterManager;
    }

    public void sendRequest(String request){
        filterManager.filterRequest(request);
    }
}



public class PatternInterceptingFilter{

    public static void main(String[] args) {
        FilterManager filterManager = new FilterManager(new Target());
        filterManager.setFilter(new AuthenticationFilter());
        filterManager.setFilter(new DebugFilter());

        Client client = new Client();
        client.setFilterManager(filterManager);
        client.sendRequest("HOME");
    }

}
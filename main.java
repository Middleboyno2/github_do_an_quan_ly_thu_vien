package dem4;
import java.util.*;
public class main {
	public static void main(String[] args) {
		List <diem> mylist = new ArrayList<diem>();
		diem a = new diem(1,1);
		mylist.add(a);
		diem b = new diem(2,2);
		mylist.add(b);for(diem x:mylist)x.output();
		diem c = new diem(3,3);
		mylist.add(c);
		mylist.forEach(x->{x.output();});
		
	    Map <String, Integer> map = new HashMap<String, Integer>();
	    map.put("MyString1", 1);
	    map.put("MyString1", 2);
	    
	    for(String key : map.keySet()) {
	    	System.out.println("key: "+key + ";value: "+ map.get(key));
	    }
	}
}

/*class diem{
	float x, y;
	public diem(float a, float b) {x=a;y=b;}
	public void output() {System.out.println("("+x+", "+y+")");}} */

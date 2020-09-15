/**
 * @(#)NO1Final.java
 *
 * NO1Final application
 *
 * @author
 * @version 1.00 2020/4/28
 */

public class NO1Final {
	public boolean newDelete(String item){
    		int match = -1;
    		for(int loc = 0; loc < numItems; loc++){
    			if (item.compareTo(list[loc]) == 0)
    				match = loc;
    			if (match == -1)
    				return false;
    			else{
    				list[match] = list[numItems - 1];
    				numberItems--;
    				return true;
    			}
    		}
   public static void main(String[] args) {
    	}
    }
}
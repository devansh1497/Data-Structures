import java.util.*;

public class Check {
	
	Hashtable<Character,Integer> hash = new Hashtable<Character,Integer>();
	
	boolean checkPerm(String s1,String s2) {
		
		if(s1.length() != s2.length()) {
			return false;
		}
		
		for(int i = 0 ; i < s1.length() ; i++) {
			char c = s1.charAt(i);
			if(!hash.containsKey(c)) {
				hash.put(c, 1);
			}
			else {
				int count = hash.get(c);
				hash.put(c, count+1);
			}
		}
		for(int i = 0 ; i < s2.length() ; i++) {
			char c =s2.charAt(i);
			if(!hash.containsKey(c)) {
				return false;
			}
			int count = hash.get(c);
			hash.put(c , count-1);
		}
	
		ArrayList<Integer> list = new ArrayList<Integer>(hash.values());
		boolean flag = true;;
		for(int x : list) {
			flag = true;
			if(x != 0) {
				flag = !flag;
			}
		}
		if(!flag) {
			return false;
		}
		
		return true;
	}
	
	public static void main(String args[]) {
		
		Check c = new Check();
		System.out.println(c.checkPerm("abcdef", "bacfeh"));
		
	}

}

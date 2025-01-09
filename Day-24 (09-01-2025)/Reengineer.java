package reflection;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class Reengineer {
	private String name = "java.lang.String";

	public Reengineer() {
		try {
			Class obj = Class.forName(name);
			Field[] f = obj.getDeclaredFields();
			Constructor[] c = obj.getDeclaredConstructors();
			Method[] m = obj.getDeclaredMethods();
			
			System.out.println(name);
			for(int i=0; i<name.length(); i++)
				System.out.print("-");
			System.out.println();

			if(f.length>0) {
				System.out.println("FIELDS:");
				for(int i=0; i<f.length; i++) {
					System.out.println((i+1)+": "+nopackage(f[i].toString()));
				}
			}
			
			if(c.length>0) {
				System.out.println("CONSTRUCTORS:");
				for(int i=0; i<c.length; i++) {
					System.out.println((i+1)+": "+nopackage(c[i].toString()));
				}
			}

			if(m.length>0) {
				System.out.println("METHODS:");
				for(int i=0; i<m.length; i++) {
					System.out.println((i+1)+": "+nopackage(m[i].toString()));
				}
			}

		} catch(ClassNotFoundException e) {
			
		}
	}

	private String nopackage(String line) {
		StringBuffer buf = new StringBuffer();
		char c;
		boolean take = true;
		for(int i=line.length()-1; i>=0; i--) {
			c = line.charAt(i);
			switch(c) {
			case '.': take = false; break;
			case ' ': take = true; break;
			case ',': take = true; break;
			case '[': take = true; break;
			case ']': take = true; break;
			case '(': take = true; break;
			case ')': take = true; break;
			}
			
			if(take) {
				buf.insert(0, c);
			}
		}
		return buf.toString();
	}
	
	public static void main(String[] args) {
		new Reengineer();
	}

}

class Human{
	int a;
	int b;
	public int get(int a, int b) {
		this.a=a;
		this.b=b;
		return a*b;
	}
}

public class Addition {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
     Human hum=new Human();
    int res= hum.get(20, 10);
    System.out.println("The result of a and b is : "+ res);
	}

}

import java.util.LinkedList;
public class sumn {
    private static LinkedList<Integer> list = new LinkedList<Integer>();
    public static void findSum(int sum, int n)
{
        if ( n < 1 || sum < 1)
            return;
        if (sum > n)
        {
            list.add(n);
            findSum(sum - n, n - 1);// n加入，取n=n-1,m=m-n
            list.pop();
            findSum(sum, n - 1);    // n没有加入，取n=n-1,m=m
        }
        else
        {
            System.out.print(sum);  //  sum < n ,直接输出n就可以满足了
            for (int i = 0; i < list.size(); i ++)
                System.out.print("  "+ list.get(i));
            System.out.println();
        }
    }
    /**
     * @param args
     */
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int sum = 10;
        int n = 6;
        findSum(sum,n);
    }
}

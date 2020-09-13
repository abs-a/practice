public class hw11 {
    public static void main(String[] args) {
        // 输出语句
        System.out.println("start!");
        System.out.println("==============");
        // 基本变量赋值
        int num1 = 1;
        int num3 = 3;
        // 引用变量赋值
        int[] arrayA = new int[] { 1,2,3 };
        int[] arrayB = new int[] { 3,4,5 };
        // if 语句应用
        System.out.println("num2 is the max!");
        System.out.println("==============");
        // 循环语句应用
        for (int j : arrayA) {
            System.out.println("arrayA的值为：" + j);
        }
        System.out.println("==============");
        for (int i : arrayB) {
            System.out.println("arrayB的值为：" + i);
        }
        System.out.println("==============");
        // 方法的使用
        System.out.println( sum( num1,num3 ) );
        System.out.println("==============");
        System.out.println("finish!");
    }

    // 方法的定义
    public static int sum( int num1,int num2 ) {
        return num1 + num2;
    }
}

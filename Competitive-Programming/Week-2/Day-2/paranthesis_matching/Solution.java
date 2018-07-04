import java.util.*;


public class Solution {

    public static int getClosingParen(String sentence, int openingParenIndex) {

        // find the position of the matching closing parenthesis
        Stack<Integer> stk = new Stack<>();
        for(int i = 0; i < sentence.length(); i++)
        {
            if (sentence.charAt(i)=='('){
                stk.push(i);
            }
            if (sentence.charAt(i)==')'){
                int temp  =  stk.pop();
                if (temp == openingParenIndex){
                    return i;
                }
            }
        }

        return -1;
    }


    // tests

    public static void main(String[] args) {
        int expected = 7;
        int actual = getClosingParen("((((()))))", 2);
        if(expected==actual){
            System.out.println("Passed");
        }
        else{
            System.out.println("Failed");
        }
        expected = 10;
        actual = getClosingParen("()()((()()))", 5);
        if(expected==actual){
            System.out.println("Passed");
        }
        else{
            System.out.println("Failed");
        }
        expected = -1;
        actual = getClosingParen("()(()", 2);
        if(expected==actual){
            System.out.println("Passed");
        }
        else{
            System.out.println("Failed");
        }
    }
}

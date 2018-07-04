import java.util.*;


public class Solution {

    public static boolean isValid(String code) {

        // determine if the input code is valid
        Stack<Character> stk = new Stack<>();
        
        for(int i = 0; i < code.length(); i++){
            if(code.charAt(i)=='(' || code.charAt(i)=='{' || code.charAt(i)=='['){
                stk.push(code.charAt(i));
            }
            else{
                if (stk.empty()){
                    return false;
                }
                char temp = stk.pop();
                if (temp == '('){
                    if (code.charAt(i)!=')'){
                        return false;
                    }
                }
                else if(temp == '{'){
                    if (code.charAt(i)!='}'){
                        return false;
                    }
                }
                else{
                    if (code.charAt(i)!=']'){
                        return false;
                    }
                }
            }
        }
        if (stk.empty()){
            return true;
        }
        
        
        
        
        return false;
    }


    // tests

    public static void main(String[] args) {
        boolean result = isValid("()");
        if(result!=true){
            System.out.println("TestCase 1 Failed");
        }
        else{
            System.out.println("Passed");
        }
        result = isValid("([]{[]})[]{{}()}");
        if(result!=true){
            System.out.println("TestCase 2 Failed");
        }else{
            System.out.println("Passed");
        }
        result = isValid("([][]}");
        if(result!=false){
            System.out.println("TestCase 3 Failed");
        }else{
            System.out.println("Passed");
        }
        result = isValid("[[]()");
        if(result!=false){
            System.out.println("TestCase 4 Failed");
        }else{
            System.out.println("Passed");
        }
        result = isValid("[[]]())");
        if(result!=false){
            System.out.println("TestCase 5 Failed");
        }else{
            System.out.println("Passed");
        }
        result = isValid("");
        if(result!=true){
            System.out.println("TestCase 6 Failed");
        }else{
            System.out.println("Passed");
        }
    }
}
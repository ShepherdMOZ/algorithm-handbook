package app;
import java.util.Arrays;



public class App {
    public static void main(String[] args) throws Exception {

        String main = "The quick brown fox jumps over a lazy dog";
        String sub = "lazy dog";
        int[] pattern = buildPattern(sub);

        System.out.println(Arrays.toString(buildPattern(sub)));
        System.out.println(checkPattern(main,sub,pattern));
    }

    public static int[] buildPattern(String substring){
        int[] pattern = new int[substring.length()];

        // Init the array to -1 for the convience of string indexing
        Arrays.fill(pattern, -1);
        int i = 1; // Starting point of a pre/suffix match
        int j = 0; // Length of a matched pre/suffix string
        while (i<substring.length()){
            
            // Check whether the prefix string are same with the suffix string
            if (substring.charAt(i) == substring.charAt(j)){
                pattern[i] = j;
                i++;
                j++;
            } else if (j > 0){
                // reset the length to the last matched point. 
                j = pattern[j-1] + 1; // Remember to plus one and turn it to normal string index
            } else {
                i++;
            }
        }
        return pattern;

    }

    public static boolean checkPattern(String mainString, String subString, int[] pattern){
        int i = 0; // This is different from buildPattern(), because now we want a full match
        int j = 0;
        while (i + subString.length() - j <= mainString.length()){
            if (mainString.charAt(i) == subString.charAt(j)){
                if (j == subString.length() - 1) return true; // This means we get substring fully matched to the main
                i++;
                j++;
            } else if (j > 0){
                // reset the length to the last matched point. 
                j = pattern[j-1] + 1; // Remember to plus one and turn it to normal string index
            } else {
                i++;
            }
        }
        return false;
    }
}
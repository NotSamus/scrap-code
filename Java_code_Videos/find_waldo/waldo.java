import java.util.Scanner;
import java.io.File;
import java.io.IOException;

public class waldo{
    public static void main(String[] args) throws IOException{
        Scanner file_input = new Scanner(new File("Waldo.txt"));

        while(file_input.hasNextLine()){
            System.out.println(file_input.nextLine());
        }

        file_input.close();
    }

    public static Boolean BinarySearch(){
        

        return false;
    }
}
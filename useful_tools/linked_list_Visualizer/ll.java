import java.util.Scanner;

/**
 * Author: Jesus Lopez
 * Date: 23/10/2024
 */
public class ll{
    public static void main(String[] args){
        myLinkedList list = new myLinkedList();
        System.out.println("############################");
        System.out.println("## Welcome to Linked List ##");
        System.out.println("############################\n\n\n");
        char menu= ' ';
        Scanner input = new Scanner(System.in);
        while(menu != 'e'){
            System.out.println("Make a selection:");
            System.out.println("(a) Add element");
            System.out.println("(p) Print Linked List");
            System.out.println("(d) delete from linked list");
            System.out.print("(e) Exit\n\n> ");
            menu = input.next().charAt(0);
            

            switch (menu) {
                case 'a':
                    System.out.print("Please enter character to add to the list: \n> ");
                    try{
                        char holder = input.next().charAt(0);
                        list.add(holder);
                        System.out.println("Item added!!!\n\n\n");
                        System.out.flush();
                    }catch( Exception e){
                        System.out.print(e);
                    }        

                    break;
                case 'd':
                    //TODO: implement the deletion from the list
                    break;

                case 'p':
                    System.out.print("\n");
                    System.out.print("Your current Linked List: \n\n");
                    list.print();
                    System.out.print("\n");
                    break;
                default:
                    if(menu != 'e'){
                        System.out.print("\n\nPlease enter a valid option!!!!!\n\n");
                    }else{
                        System.out.print("\n\nThankyou for using the program!!\n\n");
                    }
                    break;
                
            }
        }
        input.close();


        
    }
}

/***
 * 
 * list.add('a');
        list.add('b');
        list.add('c');
        list.print();
 */
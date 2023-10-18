//this is basically a carbon copy of my python text adventure, just put into java
//import scanner for user input
import java.util.Scanner;
//main class
public class Main {
	//main method to start it all
	public static void main(String[] args) 
	{
		//calling the first decision method
		FirstDecisionWhereToGo();
	}
    public static void FirstDecisionWhereToGo() 
    {
    	//sysout exposition dump
    	System.out.println("I've made some changes to the plot that this was based on in the interest of time\n"
    			+ "So if anything seems weird or contrived just go with it \n"
    			+ "Because it's probably easier than explaining all of the lore of the world outside of Megaton");
    	System.out.println("");
    	System.out.println("Welcome to Megaton");
    	System.out.println("Megaton is a city built around a crater with an undetonated nuclear bomb");
    	System.out.println("from a bygone war in the center; after which the town is named.");
    	System.out.println("The undetonated nuclear weapon has become a monument to the city.");
    	System.out.println("It's been around so long that people don't even realise its a threat anymore.");
    	System.out.println("The towns leadership hasn't bothered to hire someone to disarm the bomb either.");
    	System.out.println("You just so happen to be a retired explosives expert who is making your way into town.");
    	// Initialize the scanner
        Scanner input = new Scanner(System.in);
        // initialize the choice
        String choice;
        System.out.println("Type 1 and press enter to ask around about the undetonated nuclear bomb in the middle of the city.");
        // taking the input from the next line
        choice = input.nextLine();
        //if else if and else statements to handle input 1 2 and any invalid inputs
        if (choice.equals("1")) 
        {
        	//initialises the next part/branch of the airport
        	AskAboutTheBomb();
        } 
        else if (choice.equals("2")) 
        {
        	//initialises the next part/branch of the airport
        	IgnoreTheBomb();
        } 
        else 
        {
        	//invalid/exception handling
            System.out.println("That's not a valid choice. Try again.");
            FirstDecisionWhereToGo();
        }
        
    }
    public static void AskAboutTheBomb() 
    {
        Scanner input = new Scanner(System.in);
        String choice;
        System.out.println("You ask about the nuclear bomb and eventualy you encounter the town sheriff");
        System.out.println("\"I'm going to have to ask you to stop asking around about the bomb\" The sheriff says");
        System.out.println("\"It makes people nervous, especialy because of that rumor thats been going around\"");
        System.out.println("Type 1 and press enter to ask about the rumor");
        System.out.println("Type 2 and press enter to ignore the rumor and offer to disarm the bomb");
        choice = input.nextLine();
        if (choice.equals("1")) 
        {
        	RumorExplination();
        } 
        else if (choice.equals("2")) 
        {
        	Ending1();
        } 
        else 
        {
            System.out.println("That's not a valid choice. Try again.");
            AskAboutTheBomb();
        }
    }
    public static void RumorExplination() 
    {
        Scanner input = new Scanner(System.in);
        String choice;
        System.out.println("\"Theres been this guy, Burke");
        System.out.println("\"He's dresed like he's here for buisness but hangs around doing basicaly nothing.\"");
        System.out.println("\"I've heard people say he has his eye set on that monument");
        System.out.println("\"Some even say he wants to detonate it\"");
        System.out.println("\"Regardless of whether these claims are true I can't have you going around worying the people"); 
        System.out.println("\"People are already paranoid enough that something dangerous is going to happen\"");
        System.out.println("Type 1 and press enter to offer to find Burke and ask what his deal is");
        System.out.println("Type 2 and press enter to ignore the rumor and offer to disarm the bomb");
        choice = input.nextLine();
        if (choice.equals("1")) 
        {
        	FindBurke();
        } 
        else if (choice.equals("2")) 
        {
        	Ending1();
        } 
        else 
        {
            System.out.println("That's not a valid choice. Try again.");
            RumorExplination();
        }
    }
    public static void FindBurke() 
    {
        System.out.println("\"Thanks, thats one less thing for me to worry about\" the sheriff says");
        System.out.println("As you encounter Burke he introduces himself");
        FoundBurke();
    }
    public static void IgnoreTheBomb() 
    {
       System.out.println("As you make your way to the shop you're aproached by a strange man"); 
       System.out.println("He introduces himself as Br. Burke");
       FoundBurke();
    }
    public static void FoundBurke() 
    {
    	System.out.println("Mr. Burke is dressed in very formal buisness atire and is carrying around a breifcase");
    	System.out.println("\"I understand you're an explosives expert. Yes?\" Mr. Burke says");
    	System.out.println("\"Well then in that case I have a buisness proposition for you\"");
    	System.out.println("He opens his briefcase and pulls out a small device");
    	System.out.println("\"Take this and place it on the monument in the center of the city\" he says");
    	System.out.println("\"It's magnetic so it schould stick to the surphase of it prettey easily\"");
    	System.out.println("\"I'd do it myself but can't get anywhere near that bomb with the sheriff already on my case\"");
    	System.out.println("\"After that meet me outside of Megaton and you'll be rewarded with $30,000\"");
    	Ending23Choice();
    }
    public static void Ending23Choice() 
    {
        Scanner input = new Scanner(System.in);
        String choice;
        System.out.println("Type 1 and press enter to take the device and use it as evidince to turn Burke in to the sheriff and \ndisarm the bomb after Burke is arested");
        System.out.println("Type 2 to place the device on the bomb and detonate it from a safe distance for the $30,000 reward \nfrom burke");
        choice = input.nextLine();
        if (choice.equals("1")) 
        {
            System.out.println("Congratulations! you got Ending 2 (the best outcome for this text adventure)! Burke is Now in jail \nand the bomb is now disarmed! Play again and make different decisions to see the different endings");
        } 
        else if (choice.equals("2")) 
        {
            System.out.println("Congratulations! you got Ending 3 (the most evil outcome for this text adventure)! The town of \nMegaton is now dead because of you, but youre richer because of it! Play again and make different decisions to see the different endings");
        } 
        else 
        {
            System.out.println("That's not a valid choice. Try again.");
            Ending23Choice() ;
        }
    }
    public static void Ending1() 
    {
        System.out.println("\"You'd actually do that for me? ... Thanks!\"");
        System.out.println("\"Thats one less headache for me to worry about!");
        System.out.println("You difuse the bomb and the whole town becomes just a little bit safer");
        System.out.println("Congratulations! You got Ending 1 (the easiest and by far the least interesting ending)! The town of \nMegaton is now safe! Play again and make different decisions to see the different endings");
       }
    }
/*
    public static void NAMEHERE() 
    {
        Scanner input = new Scanner(System.in);
        String choice;
        
        System.out.println("CHOICE TEXT HERE");
        choice = input.nextLine();
        
        if (choice.equals("1")) {
            Branch1();
        } else if (choice.equals("2")) {
            BRANCH2();
        } else {
            System.out.println("That's not a valid choice. Try again.");
            restart code
        }
    }    
*/
import java.util.*;
public class tikTak 
// Stella Ava Ted
// My comments were kinda long 
// So if you see"(next line)" that means its the same comment continuing on the next line
// I just do this cause my code viewport is kinda thin and that way I can see all the text at once
// The reason I'm explaining this at the top instead of just leaving it as-is is because (newline)
// I had comments next to comments with (newline) and it was hard to tell where (newline)
// one comment started and another one ended
	{
		// Defines the global variables I need for the rest of the program
		static String[] board;
		static String turn;
		// Sets a dictionary to assign a number to each of the nine squares
		static void printBoard()
		{
			System.out.println("|---|---|---|");
			System.out.println("| "+board[0]+" | "+board[1]+" | "+board[2]+" |");
			System.out.println("|---|---|---|");
			System.out.println("| "+board[3]+" | "+board[4]+" | "+board[5]+" |");
			System.out.println("|---|---|---|");
			System.out.println("| "+board[6]+" | "+board[7]+" | "+board[8]+" |");
			System.out.println("|---|---|---|");
			/*
			|---|---|---|
			| 0 | 1 | 2 |
			|---|---|---|
			| 3 | 4 | 5 |
			|---|---|---|
			| 6 | 7 | 8 |
			|---|---|---|
			*/
		}
		// CheckWinner method will decide the combination of three box given below.
		static String checkWinner()
		{
			// For loop that repeats 8 times to check all 8 winning conditions
			for (int a = 0; a < 8; a++) 
			{
				//sets a null string for checking the win positions
				//setting it to null creates a variable for it to use but it doesn't
				String line = null;
				// switch sets line to each iteration to allow us to check for a winer 
				// uses switch (a) so it does a different case each time (next line)
				// and doesn't re-check the same thing twice each turn
				switch (a) 
				{
					case 0:
						line = board[0] + board[1] + board[2];
						break;
					case 1:
						line = board[3] + board[4] + board[5];
						break;
					case 2:
						line = board[6] + board[7] + board[8];
						break;
					case 3:
						line = board[0] + board[3] + board[6];
						break;
					case 4:
						line = board[1] + board[4] + board[7];
						break;
					case 5:
						line = board[2] + board[5] + board[8];
						break;
					case 6:
						line = board[0] + board[4] + board[8];
						break;
					case 7:
						line = board[2] + board[4] + board[6];
						break;
				}
				// For X winner
				// Sees if line = XXX if it doesn't have 3 X's 
				// than it checks for O's and then goes through each winning iteration
				if (line.equals("XXX")) 
				{
					return "X";
				}
				// For O winner
				else if (line.equals("OOO")) 
				{
					return "O";
				}
			}         
			// For loop that says if its been nine turns than its a draw
			for (int a = 0; a < 9; a++) 
			{
				if (Arrays.asList(board).contains(String.valueOf(a + 1))) 
				{
					break;
				}
				else if (a == 8) 
				{
					return "draw";
				}
			}
		// To enter the X Or O at the exact place on board.
        System.out.println(turn+"'s turn; enter a slot number to place "+turn+" in:");
        return null;
    }
	public static void main(String[] args) 	   
    {
		//initiates the scanner
        Scanner in = new Scanner(System.in);
        board = new String[9];
        //starts with X's turn
        turn = "X";
        //initiates winner variable
        String winner = null;
        
        //comment explaining it is below
        for (int a = 0; a < 9; a++) 
        {
            board[a] = String.valueOf(a + 1);
        }
		/*
		Got rid of the weird error message from earlier but also (next line)
		Makes the board go from this
		|---|---|---|
		| 0 | 1 | 2 |
		|---|---|---|
		| 3 | 4 | 5 |
		|---|---|---|
		| 6 | 7 | 8 |
		|---|---|---|
		To this
		|---|---|---|
		| 1 | 2 | 3 |
		|---|---|---|
		| 4 | 5 | 6 |
		|---|---|---|
		| 7 | 8 | 9 |
		|---|---|---|
		Because when I had my parents play-test it, (next line)
		they got confused about how there are 9 squares, (next line)
		but the highest number was 8.
		
		*/
        
        // prints the welcome massage and board 
        System.out.println("Welcome to 3x3 Tic Tac Toe.");
        printBoard();
        System.out.println("X will play first. Enter a slot number to place X in:");
        
        //only runs exception handling when there's no winner
        while (winner == null) 
        {
           int numInput;
           // Exception handling.
           // numInput will take input from user like from 1 to 9.
           // If it is not in range from 1 to 9.
           // then it will show you an error "Invalid input."
            try 
            {
                numInput = in.nextInt();
                if (!(numInput > 0 && numInput <= 9)) 
                {
                    System.out.println("Invalid input; re-enter slot number:");
                    continue;
                }
            }
            catch (InputMismatchException e) 
            {
                System.out.println("Invalid input; re-enter slot number:");
                continue;
            }
            // This game has two player x and O.
            // Here is the logic to decide the turn.
            if (board[numInput - 1].equals(String.valueOf(numInput))) 
            {
                board[numInput - 1] = turn;
                if (turn.equals("X")) 
                {
                    turn = "O";
                }
                else {
                    turn = "X";
                }
                printBoard();
                //sets a winner
                winner = checkWinner();
            }
            else 
            {
                System.out.println("Slot already taken; re-enter slot number:");
            }
        }
        // If no one win or lose then print draw message
        if (winner.equalsIgnoreCase("draw")) 
        {
            System.out.println("It's a draw! Thanks for playing.");
        }
       
        // You win message
        else 
        {
            System.out.println("Congratulations! "+winner+"'s have won! Thanks for playing.");
        }
        in.close();
    }
}

import java.util.Scanner;


public class Main 
{
	private static Scanner scan;
	
	public static void main(String[] args)
	{
		int numNodes = 0, startPos = 0;
		int caseCount = 1;
		
		scan = new Scanner(System.in);
		
		numNodes = getNumNodes();
		
		while(numNodes != 0)
		{
			System.out.print("Case " + caseCount + ": ");
			startPos = getStartPos();
			
			calcLongestPath(numNodes, startPos-1);
			
			caseCount++;
			
			numNodes = getNumNodes();
		}
	
		scan.close();
	}
	
	public static int getNumNodes()
	{
		int numCases = Integer.parseInt(scan.nextLine());
		
		return numCases;
	}
	
	public static int getStartPos()
	{
		int startPos = Integer.parseInt(scan.nextLine());
		
		return startPos;
	}
	
	public static void calcLongestPath(int numNodes, int startPos)
	{
		int[][] adjMat = new int[numNodes][numNodes];
		String input = scan.nextLine();
		String[] parsed;
		int start, stop;
		int longest, end = startPos;
		
		for(int i = 0; i < adjMat.length; i++)
		{
			for(int j = 0; j < adjMat[i].length; j++)
			{
				if(i == j)
				{
					adjMat[i][j] = 0;
				}
				else
				{
					adjMat[i][j] = Integer.MAX_VALUE;
				}
			}
		}
					
		
		while(!input.equals("0 0"))
		{
			parsed = input.split("\\s+");
			
			start = Integer.parseInt(parsed[0]) - 1;
			stop = Integer.parseInt(parsed[1]) - 1;
			
			if(start != stop)
				adjMat[start][stop] = -1;
			
			input = scan.nextLine();
		}
		
		
		for(int j = 0; j < numNodes; j++)
		{
			for(int row = 0; row < numNodes; row++)
			{
				for(int col = 0; col < numNodes; col++)
				{
					if(adjMat[row][j] != Integer.MAX_VALUE && adjMat[j][col] != Integer.MAX_VALUE)
						adjMat[row][col] = Math.min(adjMat[row][col], adjMat[row][j] + adjMat[j][col]);
				}
			}
		}
		
		longest = 0;
		
		for(int col = 0; col < numNodes; col++)
		{
			if(-adjMat[startPos][col] > longest)
			{
				longest = -adjMat[startPos][col];
				end = col;
			}
		}
		
		System.out.println("The longest path from " + (startPos + 1) + " has length " + longest + ", finishing at " + (end + 1) + ".\n");
	}
}

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import junit.framework.TestCase;


public class TestMain extends TestCase
{
	private static Process proc;
	private static InputStream in;
	private static OutputStream out;
	
	public void setUp()
	{
		try
		{
			proc = Runtime.getRuntime().exec("java Main");
			in = proc.getInputStream();
			out = proc.getOutputStream();
		}
		catch(IOException ioe)
		{
			ioe.printStackTrace();
		}
	}
	
	public void tearDown()
	{
		try
		{
			in.close();
			out.close();
		}
		catch(IOException ioe)
		{
			ioe.printStackTrace();
		}
		
		proc.destroy();
		proc = null;
	}
	
	public void test1()
	{
		byte[] toWrite = new byte[2];
		
		toWrite[0] = 1;
		toWrite[1] = 0x0A;
		
		try
		{
			out.write(toWrite);
			
		}
		catch(IOException ioe)
		{
			ioe.printStackTrace();
		}
		
		System.out.println("Test testNumCases succeeded.");
	}
}

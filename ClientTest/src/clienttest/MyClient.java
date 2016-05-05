 import java.io.*;  
    import java.net.*; 
    public class MyClient {
    public static void main(String[] args) {  

    try{      
    Socket soc=new Socket("localhost", 2004);  
    DataOutputStream dout=new DataOutputStream(soc.getOutputStream());  
    dout.writeUTF("Hello");
    dout.flush();
    dout.close();  
    soc.close();
    }catch(Exception e){
        e.printStackTrace();}  
    }  
  }
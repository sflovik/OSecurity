    import java.io.*;  
    import java.net.*; 
    public class MyClient {
    private static boolean mute = true;
    private static final String sendMute = "mute";
    private static final String sendActive = "active"; 
    private static final String sendArming = "arming";
    public static void main(String[] args) {  
    mute = false;
    setArming();
    
    }
    public static void setArming() {
        try{      
          
            Socket soc=new Socket("25.95.63.199", 2004);  
            PrintWriter out = new PrintWriter(soc.getOutputStream(), true);

            BufferedReader in = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
            System.out.println(sendArming);
            out.print(sendArming);
            out.close();
            in.close();
            soc.close();
            }catch(UnknownHostException e){
                System.err.println("Unknown Host.");
            }catch (IOException e) {
                System.err.println("Couldn't get I/O for connection");
                
            }
    }
    public static void setMute(){
        if (mute) {
        try{      
          
            Socket soc=new Socket("25.95.63.199", 2004);  
            PrintWriter out = new PrintWriter(soc.getOutputStream(), true);

            BufferedReader in = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
            System.out.println(sendMute);
            out.print(sendMute);
            out.close();
            in.close();
            soc.close();
            }catch(UnknownHostException e){
                System.err.println("Unknown Host.");
            }catch (IOException e) {
                System.err.println("Couldn't get I/O for connection");
                
            }
        }
        else {
         try{      
   
            Socket soc=new Socket("25.95.63.199", 2004);  
            PrintWriter out = new PrintWriter(soc.getOutputStream(), true);

            BufferedReader in = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
            System.out.println(sendActive);
            out.print(sendActive);
            out.close();
            in.close();
            soc.close();
            }catch(UnknownHostException e){
                System.err.println("Unknown Host.");
            }catch (IOException e) {
                System.err.println("Couldn't get I/O for connection");
                 System.out.println(sendMute);
                 System.out.println(sendActive);
            }   
            
    }
    }
    }
    
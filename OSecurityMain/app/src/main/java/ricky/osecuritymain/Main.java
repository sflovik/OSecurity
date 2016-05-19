/**
 * Main class for GruppeX's OSecurity android application
 * Contains all java logic to be executed.
 * @authors Sondre Flovik, Ricky Omland, Christian Fredrik Thorne
 * @date May 2016
 */
package ricky.osecuritymain;
/**
 * All imports for the project
 */
import android.Manifest;
import android.app.Activity;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.os.StrictMode;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.ToggleButton;
import java.io.*;
import java.net.*;

/**
 * Start of main class, set all variables
 */
public class Main extends AppCompatActivity {
    private static boolean mute = false;
    int counter = 1;
    private static final String sendMute = "mute";
    private static final String sendActive = "active";
    private static final String sendArming = "arming";
    private static final String sendDisarm = "disarming";
  //  private static final int REQUEST_EXTERNAL_STORAGE = 1; unused
  //  private static String[] PERMISSIONS_STORAGE = { unused
    //        Manifest.permission.READ_EXTERNAL_STORAGE, unused
      //      Manifest.permission.WRITE_EXTERNAL_STORAGE }; unused

    ToggleButton toggle;
    EditText ed;

    /**
     * When the UI is drawn / created on application start
     * @param savedInstanceState instance state
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        View view = new View(this);
        // Not good practice, but a temporary solution to allow networking to be executed
        // in the GUI thread of the application. Forces permission, as opposed to
        // the good practice of multi-threading in these situations
        // Can potentially cause instability and application crashes
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        getSupportActionBar().setTitle("  Home");
        setSupportActionBar(toolbar);
        getSupportActionBar().setDisplayShowHomeEnabled(true);
        toggle = (ToggleButton)findViewById(R.id.toggBtn);

        getSupportActionBar().setIcon(R.drawable.home);
        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.	make(view, "Settings", Snackbar.LENGTH_INDEFINITE)
                        .setAction("Action", null).show();
            }
        });
    }
    /**
     * Teimporarily unused - alternative way of granting the application writing permissions
     * in runtime environment
    public static void verifyStoragePermissions(Activity activity) {
        int permission = ActivityCompat.checkSelfPermission(activity, Manifest.permission.WRITE_EXTERNAL_STORAGE);

        if (permission != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(
                    activity,
                    PERMISSIONS_STORAGE,
                    REQUEST_EXTERNAL_STORAGE);
        }
    }
     */
    /**
     * Method to arm the system, sends the static sendArming variable to the terminal
     */
    public static void setArming() {
        try {
            // Connects to the terminals socket connection
            // Could / should have made the variables static and global
            // to prevent code duplication on several methods
            Socket soc = new Socket("25.95.63.199", 2004);
            PrintWriter out = new PrintWriter(soc.getOutputStream(), true);
            // Sets up a BufferedReader to get input and send data to socket host
            BufferedReader in = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
            System.out.println(sendArming);
            out.print(sendArming);
            out.close();
            in.close();
            soc.close();
        } catch (UnknownHostException e) {
            System.err.println("Unknown Host.");
        } catch (IOException e) {
            e.printStackTrace();

        }
    }

    /**
     * Method to disarm the system
     * Same functionality as in setArming(), except another variable is sent to the socket host
     */
    public static void setDisarming() {
        try{

            Socket soc=new Socket("25.95.63.199", 2004);
            PrintWriter out = new PrintWriter(soc.getOutputStream(), true);

            BufferedReader in = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
            System.out.println(sendDisarm);
            out.print(sendDisarm);
            out.close();
            in.close();
            soc.close();
        }catch(UnknownHostException e){
            System.err.println("Unknown Host.");
        }catch (IOException e) {
            System.err.println("Couldn't get I/O for connection");

        }
    }

    /**
     * Method to set wether buzzer should be active or not on the terminal
     * Sends either sendMute variable or sendActive variable, depending on the state
     * of the global "mute" variable, true/false
     * Functionality same as in previous methods
     */
    public static void setMute() {
        if (mute) {
            try {

                Socket soc = new Socket("25.95.63.199", 2004);
                PrintWriter out = new PrintWriter(soc.getOutputStream(), true);

                BufferedReader in = new BufferedReader(new InputStreamReader(soc.getInputStream()));
                BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
                System.out.println(sendMute);
                out.print(sendMute);
                out.close();
                in.close();
                soc.close();
            } catch (UnknownHostException e) {
                System.err.println("Unknown Host.");
            } catch (IOException e) {
                System.err.println("Couldn't get I/O for connection");

            }
        } else {
            try {

                Socket soc = new Socket("25.95.63.199", 2004);
                PrintWriter out = new PrintWriter(soc.getOutputStream(), true);

                BufferedReader in = new BufferedReader(new InputStreamReader(soc.getInputStream()));
                BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
                System.out.println(sendActive);
                out.print(sendActive);
                out.close();
                in.close();
                soc.close();
            } catch (UnknownHostException e) {
                System.err.println("Unknown Host.");
            } catch (IOException e) {
                System.err.println("Couldn't get I/O for connection");
                System.out.println(sendMute);
                System.out.println(sendActive);
            }

        }
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    /**
     * Method belonging to the xml-button for the buzzer, sets global variable
     * depending on click / state in XML
     * @param v
     */
        public void muteClick(View v) {
            if (mute) {
                mute = false;
            }
            else {
                mute = true;
            }
        }

    /**
     * Method belonging to the xml-button for arming/disarming
     * Counter variable starts at 1, which is an unarmed system
     * Tries to arm the system as long as variable is 1, and sets counter ++ (counter=2)
     * then sleeps for 1,5 seconds to wait for terminal to perform script startup, before
     * it calls setMute() to complete initializing the terminal script
     *
     * If the system is active, the counter equals 2, and the setDisarming() method is called
     * to send a KeyboardInterrupt to the terminal's terminal window to disarm the system
     * Counter is set back to 1, so that the next click will activate the system again.
     * @param v
     */
        public void onClick(View v) {
        long millis = 1500;

            if (counter == 1) {
                setArming();
                counter++;
                try {
                    Thread.sleep(millis); //
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
                setMute();
            }
            else if (counter==2) {
                setDisarming();
                counter = 1;

            }





        }
}


package ricky.osecuritymain;

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

public class Main extends AppCompatActivity {
    private static boolean mute = true;
    int counter = 1;
    private static final String sendMute = "mute";
    private static final String sendActive = "active";
    private static final String sendArming = "arming";
    private static final String sendDisarm = "disarming";
  //  private static final int REQUEST_EXTERNAL_STORAGE = 1;
  //  private static String[] PERMISSIONS_STORAGE = {
    //        Manifest.permission.READ_EXTERNAL_STORAGE,
      //      Manifest.permission.WRITE_EXTERNAL_STORAGE };

    ToggleButton toggle;
    EditText ed;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        View view = new View(this);
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
    public static void setArming() {
        try {

            Socket soc = new Socket("25.95.63.199", 2004);
            PrintWriter out = new PrintWriter(soc.getOutputStream(), true);

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


        public void onClick(View v) {
        long millis = 4000;

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
                try {
                    Thread.sleep(millis); //
                } catch (InterruptedException ex) {
                    ex.printStackTrace();
                }
                setMute();
            }





        }
}


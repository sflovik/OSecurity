package ricky.osecuritymain;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.ToggleButton;
import java.io.*;
import java.net.*;

public class Main extends AppCompatActivity {
    private static boolean mute = true;
    private static final String sendMute = "mute";
    private static final String sendActive = "active";
    private static final String sendArming = "arming";
    private static final String sendDisarm = "disarming";
    ToggleButton toggle;
    EditText ed;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
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
            System.err.println("Couldn't get I/O for connection");

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
            // TODO Auto-generated method stub
            //toggle.toggle();
            if ( ed.getText().toString().equalsIgnoreCase("1")) {
                setArming();
                toggle.setTextOff("TOGGLE ON");
                toggle.setChecked(true);
            } else if ( ed.getText().toString().equalsIgnoreCase("0")) {
                setDisarming();
                toggle.setTextOn("TOGGLE OFF");
                toggle.setChecked(false);

            }
        }
    }

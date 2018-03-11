package com.example.jordi.adidasprototype1;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.res.Resources;
import android.os.Bundle;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Gravity;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    private Interest interest;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Resources res = getResources();

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        final Button enter = findViewById(R.id.enter);
        final Button comprar = findViewById(R.id.comprar);
        final Button interes = findViewById(R.id.interes);


        enter.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                launchSecondActivity();
            }
        });

        comprar.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                create_input();
            }
        });
        interes.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                launchInfoActivity();
                //cargarDatos("Ruben");
            }
        });
    }

    public void launchInfoActivity() {

        Intent intent = new Intent(this, infoActivity.class);
        startActivity(intent);
    }

    public void launchSecondActivity() {

        Intent intent = new Intent(this, ProductsActivity.class);
        startActivity(intent);
    }

    public void create_input() {

        final EditText txt = new EditText(this);
        new AlertDialog.Builder(this)
                .setTitle("COMPRA")
                .setMessage("Introdueix codi producte comprat")
                .setView(txt)
                .setPositiveButton("COMPRAR", new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int whichButton) {

                        String codi = txt.getText().toString();
                        sendJSON(codi, "Ruben");//ENVIAR JSON con el codigo del objeto comprado

                        //launchExpActivity();
                    }
                })
                .setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                    public void onClick(DialogInterface dialog, int whichButton) {
                    }
                })
                .show();
    }


    private void sendJSON(String codi, String name) {

        HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
// set your desired log level
        logging.setLevel(HttpLoggingInterceptor.Level.BODY);
        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();
// add your other interceptors …
// add logging as last interceptor
        httpClient.addInterceptor(logging);  // <-- this is the important line!
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://46.101.12.106:5000/")
                .addConverterFactory(GsonConverterFactory.create())
                .client(httpClient.build())
                .build();

        ServiceConnexion service = retrofit.create(ServiceConnexion.class);

        service.getInterest("3", name).enqueue(new Callback<Interest>() {
            @Override
            public void onResponse(Call<Interest> call, Response<Interest> response) {
                    System.out.print("RUBEN "+response.raw());
                if (response.isSuccessful()) {
                    interest = response.body();

                    System.out.print("--------------------->"+interest );

                    //mostrar imatge

                    System.out.print("TODATODATODA ---------------->" + interest.geturlPhoto() + "\n");
                    Exp.getInstance().setInterest(interest);

                    launchInfoActivity();

                }
                else {
                    Toast toast1 = Toast.makeText(getApplicationContext(), "Fallo del servidor", Toast.LENGTH_SHORT);
                    toast1.setGravity(Gravity.CENTER, 0, 0);
                    toast1.show();
                }

            }

            @Override
            public void onFailure(Call<Interest> call, Throwable t) {
                t.printStackTrace();
            }
        });
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
}

package com.example.jordi.adidasprototype1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import java.util.LinkedList;
import java.util.List;

import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ExperienceActivity extends AppCompatActivity {

    private Interest product;
    private ListView lista;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_experience);

        Toast toast1 = Toast.makeText(getApplicationContext(), "Deben salir las experiencias\nin work progress...", Toast.LENGTH_SHORT);
        toast1.setGravity(Gravity.CENTER,0  ,0 );
        toast1.show();

        //cargarDatos(getIntent().getExtras().getString("parametro"));
    }

    private void cargarDatos(String name) {

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

        service.getInterest(name," ").enqueue(new Callback<Interest>() {
            @Override
            public void onResponse(Call<Interest> call, Response<Interest> response) {

                if (response.isSuccessful()) product = response.body();
                else{
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

}



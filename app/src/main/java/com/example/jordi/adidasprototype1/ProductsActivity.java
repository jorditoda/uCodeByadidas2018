package com.example.jordi.adidasprototype1;

import android.content.Context;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

public class ProductsActivity extends AppCompatActivity {

    private String type[] = new String[]{"Bañadores", "Gorras", "Pantalones", "Ropa Interior", "Sudaderas"
            , "Zapatos"};
    private String exp[] = new String[]{"Moda de verano", "Nueva temporada", "Outlet invierno", "Stock",
            "Ultimas unidades", "Nuevos modelos"};

    private Integer[] imgid = {
            R.drawable.banador,
            R.drawable.gorra,
            R.drawable.pantalon,
            R.drawable.ropainterior,
            R.drawable.sudadera,
            R.drawable.zapato,
    };

    private ListView lista;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_products);

        ListAdapter adapter = new ListAdapter(this, type, imgid, exp);
        lista = (ListView) findViewById(R.id.mi_lista);
        lista.setAdapter(adapter);
        lista.setClickable(true);
        lista.setOnItemClickListener(new AdapterView.OnItemClickListener() {

            @Override
            public void onItemClick(AdapterView<?> arg0, View arg1, int position, long arg3) {

                Object o = lista.getItemAtPosition(position);

            }
        });
    }

}


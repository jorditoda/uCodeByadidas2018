package com.example.jordi.adidasprototype1;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.LinkedList;

/**
 * Created by jordi on 10/03/2018.
 */

public class ListAdapter extends ArrayAdapter<String> {

    private final Activity context;
    private final String[] itemname;
    private String[] exp;
    private final Integer[] integers;

    public ListAdapter(Activity context, String[] itemname, Integer[] integers, String[] exp) {
        super(context, R.layout.list, itemname);
        // TODO Auto-generated constructor stub

        this.context = context;
        this.itemname = itemname;
        this.exp = exp;
        this.integers = integers;
    }

    public View getView(int posicion, View view, ViewGroup parent) {

        LayoutInflater inflater = context.getLayoutInflater();
        View rowView = inflater.inflate(R.layout.list, null, true);

        TextView txtTitle = (TextView) rowView.findViewById(R.id.texto_principal);
        ImageView imageView = (ImageView) rowView.findViewById(R.id.icon);
        TextView etxDescripcion = (TextView) rowView.findViewById(R.id.texto_secundario);

        txtTitle.setText(itemname[posicion]);
        imageView.setImageResource(integers[posicion]);
        if (exp != null) etxDescripcion.setText("Description " + exp[posicion]);

        return rowView;
    }


}
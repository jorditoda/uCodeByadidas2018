package com.example.jordi.adidasprototype1;

import android.graphics.drawable.Drawable;

import java.io.Serializable;

/**
 * Created by jordi on 10/03/2018.
 */

public class Product implements Serializable {

    private String name;
    private String imagen;
    private int precio;

    public Product(String name, String imagen, int precio) {

        this.imagen = imagen;
        this.name = name;
        this.precio = precio;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getImagen() {
        return imagen;
    }

    public void setImagen(String imagen) {
        this.imagen = imagen;
    }

    public int getPrecio() {
        return precio;
    }

    public void setPrecio(int precio) {
        this.precio = precio;
    }

    @Override
    public String toString() {
        return "name= " + name + imagen;
    }
}

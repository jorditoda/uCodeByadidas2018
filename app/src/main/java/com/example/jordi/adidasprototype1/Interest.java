package com.example.jordi.adidasprototype1;

/**
 * Created by jordi on 10/03/2018.
 */

public class Interest {

    private String urlPhoto;
    private int idProduct;
    private int price;

    public Interest(String urlPhoto, int idProduct, int price) {
        this.urlPhoto = urlPhoto;
        this.idProduct = idProduct;
        this.price = price;
    }
    public Interest() {

    }

    public String geturlPhoto(){
        return urlPhoto;
    }

    public void seturlPhoto(String urlPhoto) {
        this.urlPhoto = urlPhoto;
    }

    public int getiD() {
        return idProduct;
    }

    public void setiD(int iD) {
        this.idProduct = iD;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Interest{" +
                "urlPhoto='" + urlPhoto + '\'' +
                ", iD=" + idProduct +
                ", price=" + price +
                '}';
    }
}

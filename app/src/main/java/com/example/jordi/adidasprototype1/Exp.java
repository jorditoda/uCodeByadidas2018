package com.example.jordi.adidasprototype1;

/**
 * Created by jordi on 11/03/2018.
 */

class Exp {

    private static final Exp ourInstance = new Exp();
    private Interest ourInterest;
    public static Exp getInstance() {
        return ourInstance;
    }
    private Exp() {
    }
    public Interest getInterest() {
        return this.ourInterest;
    }
    public void setInterest(Interest its) {
        this.ourInterest = its;
    }

}

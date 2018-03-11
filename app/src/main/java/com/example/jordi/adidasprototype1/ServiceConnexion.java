package com.example.jordi.adidasprototype1;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

/**
 * Created by jordi on 10/03/2018.
 */

public interface ServiceConnexion {

    @GET("GET/INTEREST")
    Call<Interest> getProd(@Query("idProduct") String user, @Query("urlPhoto") String url, @Query("price") String price);

    @GET("GET/INTEREST")
    Call<Interest> getInterest(@Query("idProduct") String productId, @Query("username") String user);


}

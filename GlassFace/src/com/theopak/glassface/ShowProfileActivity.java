package com.theopak.glassface;


import android.app.Activity;
import android.os.Bundle;


public class ShowProfileActivity extends Activity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState); 
        setContentView(R.layout.profile_card);
    }
    
    @Override
    public void onStart()
    {
    	super.onStart();
        //Refresh data
        //getDataAndPutToUI();
    }
    
    @Override     
    public void onDestroy() {   
       super.onDestroy();  
    }   
}
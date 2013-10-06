package com.theopak.glassface;


import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;


public class ShowProfileActivity extends Activity {
	
	private TextView mUserName;
	private TextView mUserTagline;
	
    @Override
    public void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState); 
        setContentView(R.layout.profile_card);
        mUserName = (TextView) findViewById(R.id.user_name);
        mUserTagline = (TextView) findViewById(R.id.user_tagline);
    }
    
    @Override
    public void onStart()
    {
    	super.onStart();  // Why is this line necessary !?
        // Refresh data
    	mUserName.setText(R.string.default_user_name);
    	//mUserTagline.setText(R.string.default_user_name);
    }
    
    @Override     
    public void onDestroy() {   
       super.onDestroy();  
    }   
}
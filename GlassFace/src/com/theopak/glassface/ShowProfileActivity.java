package com.theopak.glassface;


import java.io.InputStream;
import java.net.URL;

import android.app.Activity;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.KeyEvent;
import android.widget.ImageView;
import android.widget.TextView;


public class ShowProfileActivity extends Activity {
	
	private TextView mUserName;
	private TextView mUserTagline;
	private ImageView mUserPicture;
	
	public static Drawable LoadImageFromWeb(String url) {
	    try {
	        InputStream is = (InputStream) new URL(url).getContent();
	        Drawable d = Drawable.createFromStream(is, "src name");
	        return d;
	    } catch (Exception e) {
	    	System.out.println("Exc="+e);
	        return null;
	    }
	}
	
    @Override
    public void onCreate(Bundle savedInstanceState) {
    	super.onCreate(savedInstanceState); 
        setContentView(R.layout.profile_card);
        mUserName = (TextView) findViewById(R.id.user_name);
        mUserTagline = (TextView) findViewById(R.id.user_tagline);
        
        // Ignore common sense and permit NetworkOnMainThreadException no big deal
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
		StrictMode.setThreadPolicy(policy);
    }
    
    @Override
    public void onStart()
    {
    	super.onStart();  // Why is this line necessary !?
    	mUserName.setText(R.string.default_user_name);
    	//mUserTagline.setText(R.string.default_user_name);
    	ImageView mUserPicture =(ImageView)findViewById(R.id.user_picture);
        Drawable drawable = LoadImageFromWeb("http://www.google.com/images/srpr/logo6w.png");
        //mUserPicture.setImageDrawable(drawable);
    }
    
    @Override     
    public void onDestroy() {   
       super.onDestroy();  
    }
    
    /**
     * Handle the tap event from the touchpad.
     */
    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
      switch (keyCode) {
      // Handle tap events.
      case KeyEvent.KEYCODE_DPAD_CENTER:
      case KeyEvent.KEYCODE_ENTER:
        finish();
        return true;
      default:
        return super.onKeyDown(keyCode, event);
      }
    }
}
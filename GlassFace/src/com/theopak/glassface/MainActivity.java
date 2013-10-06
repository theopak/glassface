/**
 * MainActivity.java
 * AUTH: Theo Pak <mail@theopak.com>
 * URL:  https://github.com/theopak/glassface
 */


package com.theopak.glassface;


import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.IntBuffer;
import java.util.ArrayList;
import java.util.List;
import java.util.TimeZone;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Typeface;
import android.os.Bundle;
import android.os.SystemClock;
import android.provider.MediaStore;
import android.text.format.DateFormat;
import android.util.Base64;
import android.util.Log;
import android.view.KeyEvent;
import android.widget.Chronometer;
import android.widget.TextView;
import android.speech.SpeechRecognizer;
import android.speech.RecognizerIntent;


/**
 * StopWatch sample's main activity.
 */
public class MainActivity extends Activity {
	
  private TextView mPrompt;
  private TextView mHint;
  private Chronometer mClock;
  private boolean mRecognizing = false;
  static final int RECOGNIZE_SPEECH_REQUEST = 51413;
  static final int CAPTURE_IMAGE_REQUEST = 31415;
  static final int SHOW_PROFILE_REQUEST = 22293;
  
  // Arbitrarily important IP for ~~localhost~~ Derek.
  private String server = "http://18.111.86.219:8032";

  @Override
  protected void onCreate(Bundle savedInstanceState) {
	Log.e("LETS GET STARTED!", "wooo");
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_meet);
    
    mPrompt = (TextView) findViewById(R.id.prompt);
    Typeface robo = Typeface.createFromAsset(this.getAssets(), "Roboto-Thin.ttf");
    mHint = (TextView) findViewById(R.id.hint);
    mHint.setTypeface(robo);
    
    /*
    HttpClient httpclient = new DefaultHttpClient();
    HttpPost httppost = new HttpPost(server+"/app_login/");
    
    try {
    	Log.e("requesting", "r");
	    List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(2);
        nameValuePairs.add(new BasicNameValuePair("username", "drock"));
        nameValuePairs.add(new BasicNameValuePair("password", "boop boop"));
        httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));
        Log.e("presend", "p");
        // Execute HTTP Post Request
        HttpResponse response = httpclient.execute(httppost);
        Log.e("response", response.toString());
    } catch (ClientProtocolException e) {
        Log.e("err", e.toString());
    } catch (IOException e) {
        Log.e("oherr", e.toString());
    }
    */
    
    // The actual time must be displayed (live) so that the device
    //   can be "locked" into the app for repeated demonstration.
    //   Code partially via <stackoverflow.com/a/17183740>
    mClock = (Chronometer) findViewById(R.id.chrono);
    mClock.setTypeface(robo);
    mClock.setOnChronometerTickListener(new Chronometer.OnChronometerTickListener(){
        @Override
        public void onChronometerTick(Chronometer cArg) {
            long time = System.currentTimeMillis();
            java.text.DateFormat df = DateFormat.getTimeFormat(getApplicationContext());
            df.setTimeZone(TimeZone.getTimeZone("GMT-4:00"));
            String woo = df.format(time);
            woo = woo.substring(0, woo.length() - 2);
            cArg.setText(woo);
        }
    });
    mClock.setBase(SystemClock.elapsedRealtime());
    mClock.start();
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
      toggleSpeech();
      return true;
    default:
      return super.onKeyDown(keyCode, event);
    }
  }

  @Override
  public void onDestroy() {
	if (mRecognizing) {
		mRecognizing = false;
	}
    super.onDestroy();
  }

  /**
   * Toggle the Speech states.
   */
  private void toggleSpeech() {
	mRecognizing = !mRecognizing;
    if (mRecognizing) {
      mPrompt.setText(R.string.prompt_text);
      mHint.setText(R.string.blank_text);
      mClock.setTextColor(getResources().getColor(R.color.transparent));
      recognizeSpeech();
    } else {
      mPrompt.setText(R.string.blank_text);
      mHint.setText(R.string.hint_text);
      mClock.setTextColor(getResources().getColor(R.color.white));
    }
  }
  
  /** 
   * Return data.
   */
  private void recognizeSpeech() {
    Intent recognizeSpeechIntent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
  	startActivityForResult(recognizeSpeechIntent, RECOGNIZE_SPEECH_REQUEST);
  }
  
  /**
   * Capture a picture and then return to the base state.
   */
  private void captureImage() {
    Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
    startActivityForResult(takePictureIntent, CAPTURE_IMAGE_REQUEST);
    //finish();
  }
  
  /**
   * Handle activity result(s).
   * Refer to the docs at: 
   * http://developer.android.com/reference/android/app/Activity.html#onActivityResult(int, int, android.content.Intent)
   */
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if (requestCode == RECOGNIZE_SPEECH_REQUEST && resultCode == RESULT_OK) {
      captureImage();
      Log.e("wu", data.toString());
    }
    else if (requestCode == CAPTURE_IMAGE_REQUEST && resultCode == RESULT_OK) {
    	/*
    	Bundle extras = data.getExtras();
        Bitmap mImageBitmap = (Bitmap) extras.get("data");
        int[] pixels = null;
        mImageBitmap.getPixels(pixels, 0, mImageBitmap.getWidth(), 0, 0, mImageBitmap.getWidth(), mImageBitmap.getHeight());
              
        ByteBuffer byteBuffer = ByteBuffer.allocate(pixels.length * 4);        
        IntBuffer intBuffer = byteBuffer.asIntBuffer();
        intBuffer.put(pixels);

        byte[] pixBytes = byteBuffer.array();

        Base64.encodeToString(pixBytes, Base64.DEFAULT);
              
        HttpClient httpclient = new DefaultHttpClient();
        HttpPost httppost = new HttpPost(server+"/recognize/");
                
        try {
          List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(2);
          nameValuePairs.add(new BasicNameValuePair("id", "12345"));
          nameValuePairs.add(new BasicNameValuePair("stringdata", "AndDev is Cool!"));
          httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));

          // Execute HTTP Post Request
          HttpResponse response = httpclient.execute(httppost);
        } catch (ClientProtocolException e) {
        return;
          // TODO Auto-generated catch block
        } catch (IOException e) {
         return;
          // TODO Auto-generated catch block
        }
        */
    	toggleSpeech();
    	Intent showProfileIntent = new Intent(this, ShowProfileActivity.class);
        startActivity(showProfileIntent);
    }
  }

}
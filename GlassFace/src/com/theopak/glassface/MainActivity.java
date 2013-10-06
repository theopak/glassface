/**
 * MainActivity.java
 * AUTH: Theo Pak <mail@theopak.com>
 * URL:  https://github.com/theopak/glassface
 */


package com.theopak.glassface;


import java.util.TimeZone;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Typeface;
import android.os.Bundle;
import android.os.SystemClock;
import android.provider.MediaStore;
import android.text.format.DateFormat;
import android.util.Log;
import android.view.KeyEvent;
import android.widget.Chronometer;
import android.widget.TextView;
//import android.os.SystemClock;
//import android.text.format.Time;
//android.speech.SpeechRecognizer


/**
 * StopWatch sample's main activity.
 */
public class MainActivity extends Activity {
	
  private TextView mPrompt;
  private TextView mHint;
  private Chronometer mClock;
  private boolean mRecognizing = false;
  private boolean mCapturing = false;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
	Log.e("LETS GET STARTED!", "wooo");
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_meet);
    
    mPrompt = (TextView) findViewById(R.id.prompt);
    Typeface robo = Typeface.createFromAsset(this.getAssets(), "Roboto-Thin.ttf");
    mHint = (TextView) findViewById(R.id.hint);
    mHint.setTypeface(robo);

    
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
    if (mRecognizing) {
      mPrompt.setText(R.string.prompt_text);
      mHint.setText(R.string.blank_text);
    } else {
      mPrompt.setText(R.string.blank_text);
      mHint.setText(R.string.hint_text);
    }
    mRecognizing = !mRecognizing;
    captureImage();
  }
  
  /**
   * Capture a picture and then return to the base state.
   */
  private void captureImage() {
	    Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
	    startActivityForResult(takePictureIntent, 0);
	    finish();
  }

}
/**
 * MeetActivity.java
 * AUTH: Theo Pak <mail@theopak.com>
 * URL:  https://github.com/theopak/glassface
 */


package com.theopak.glassface;


import android.app.Activity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.widget.TextView;
import android.widget.Chronometer;
//import android.os.SystemClock;
//import android.os.SystemClock;
//android.speech.SpeechRecognizer


/**
 * StopWatch sample's main activity.
 */
public class MeetActivity extends Activity {
	
  private TextView mPrompt;
  private TextView mHint;
  private Chronometer mClock;
  private boolean mStarted = false;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_meet);
    
    mClock = (Chronometer) findViewById(R.id.clock);
    mPrompt = (TextView) findViewById(R.id.prompt);
    mHint = (TextView) findViewById(R.id.hint);
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
	if (mStarted) {
	  mStarted = false;
	}
    super.onDestroy();
  }

  /**
   * Toggle the Speech states.
   */
  private void toggleSpeech() {
    if (mStarted) {
      mPrompt.setText(R.string.prompt_text);
      mHint.setText(R.string.blank_text);
    } else {
      mPrompt.setText(R.string.blank_text);
      mHint.setText(R.string.hint_text);
    }
    mStarted = !mStarted;
  }

}
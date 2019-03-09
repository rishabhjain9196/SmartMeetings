package com.example.sanjai.codiecon;

import android.content.Context;
import android.content.Intent;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.Toast;
import android.widget.VideoView;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;

public class MainActivity extends AppCompatActivity {

    private final int REQUEST_VIDEO_CODE = 1;
    VideoView resultVideo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
        Button recordButton = (Button) findViewById(R.id.recordButton);
        resultVideo = (VideoView) findViewById(R.id.videoView);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    public void dispatchTakeVideoIntent(View view) {
        Intent takeVideoIntent = new Intent(MediaStore.ACTION_VIDEO_CAPTURE);
        Log.e("Sanket", "test1");
        // Uri uri = Uri.fromFile(getFile());
        Log.e("Sanket", "test2");
        // takeVideoIntent.putExtra(MediaStore.EXTRA_OUTPUT, uri);
        if (takeVideoIntent.resolveActivity(getPackageManager()) != null) {
            startActivityForResult(takeVideoIntent, REQUEST_VIDEO_CODE);
        }
    }


//    public void recordVideo(View v) {
//        // open camera app (Build-in)
//        Intent intent = new Intent(MediaStore.ACTION_VIDEO_CAPTURE);
//
//        File videoFile = getFile();
//
//        Uri uri = Uri.fromFile(videoFile);
//
//        intent.putExtra(MediaStore.EXTRA_OUTPUT, uri);
//        intent.putExtra(MediaStore.EXTRA_VIDEO_QUALITY, 1);
//
//        startActivityForResult(intent, REQUEST_CODE);
//
//    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        Log.e("Sanket", "test3 "+requestCode+" "+resultCode);
        if (requestCode == REQUEST_VIDEO_CODE) {
            if (resultCode == RESULT_OK) {
                Uri videoUri = data.getData();
                //resultVideo.setVideoURI(videoUri);
                //resultVideo.start();
                MediaPlayer cheer = MediaPlayer.create(MainActivity.this, videoUri);
                cheer.start();
                Toast.makeText(getApplicationContext(), "Video has been saved", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(getApplicationContext(), "Error: video not saved", Toast.LENGTH_LONG).show();
            }
        }
    }

    public void playVideo(View view) {
        Log.e("Sanket", "File Directory : " + getFilesDir());
        Log.e("Sanket", "Test Start");
        String filename = "myfile";
        String outputString = "Hello world!";

        Log.e("Sanket", "Test End");
        Log.e("Sanket", "test 90");
        resultVideo.setVideoPath("/Internal/Storage/DCIM/Camera/test_video_play.mp4");
        Log.e("Sanket", "Test7 "+resultVideo);
        resultVideo.start();
    }

    // to create folder and file
    public File getFile() {
        File folder = new File("sanket12334");
        if (!folder.exists()) {
            folder.mkdir();
        }

        File videoFile = new File(folder, "myrecording.mp4");
        return videoFile;
    }

}

package com.example.sanjai.codieconmeeting;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.v4.app.Fragment;
import android.util.Base64;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;
import android.widget.VideoView;

import org.apache.commons.io.FileUtils;

import java.io.File;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * to handle interaction events.
 * create an instance of this fragment.
 */
public class MeetingFragment extends Fragment {

    private final int REQUEST_VIDEO_CODE = 1;
    VideoView resultVideo;
    Intent takeVideoIntent;

    public MeetingFragment() {
        // Required empty public constructor
    }

    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View view = inflater.inflate(R.layout.fragment_meeting, container, false);
        Button recordButton = (Button) view.findViewById(R.id.recordButton);
        resultVideo = (VideoView) view.findViewById(R.id.videoView);
        recordButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dispatchTakeVideoIntent(view);
            }
        });
        return view;
    }


    public void dispatchTakeVideoIntent(View view) {
        File mediaFile = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM).toString() + "/Camera/test_video_play.mp4");
        takeVideoIntent = new Intent(MediaStore.ACTION_VIDEO_CAPTURE);
        Uri videoUri = Uri.fromFile(mediaFile);
        takeVideoIntent.putExtra(MediaStore.EXTRA_OUTPUT, videoUri);
        takeVideoIntent.putExtra(MediaStore.EXTRA_VIDEO_QUALITY, 1);
        Log.e("Sanket", "test2");
        startActivityForResult(takeVideoIntent, REQUEST_VIDEO_CODE);
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) { Log.e("Sanket", "test3 "+requestCode+" "+resultCode);
        if (requestCode == REQUEST_VIDEO_CODE) {
            if (resultCode == Activity.RESULT_OK) {
                //Uri videoUri = data.getData();
                //resultVideo.setVideoURI(videoUri);
                //resultVideo.start();
                //MediaPlayer cheer = MediaPlayer.create(MainActivity.this, videoUri);
                //cheer.start();
                String videoFile = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM).toString() + "/Camera/test_video_play.mp4";
                String originalAudio = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM).toString() + "/Camera/test_audio_play.mp3";
                try {
                    new AudioExtractor().genVideoUsingMuxer(videoFile, originalAudio, -1, -1, true, false);
                    File file = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM).toString() + "/Camera/test_audio_play.mp3");
                    byte[] bytes = FileUtils.readFileToByteArray(file);
                    String encoded = Base64.encodeToString(bytes, 0);
                    Log.e("Sanket", "Start Data Transmission");
                    String str = new HandlingData().execute(encoded).get();
                    Log.e("Sanket", "Result "+str);
                } catch (Exception e) {
                    Log.e("Sanket", e.getMessage());
                }
                Toast.makeText(getActivity().getApplicationContext(), "Video has been saved", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(getActivity().getApplicationContext(), "Error: video not saved", Toast.LENGTH_LONG).show();
            }
        }
    }
}

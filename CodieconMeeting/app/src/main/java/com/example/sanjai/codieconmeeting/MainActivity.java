package com.example.sanjai.codieconmeeting;

import android.net.Uri;
import android.os.StrictMode;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.widget.FrameLayout;

import java.net.URI;

public class MainActivity extends AppCompatActivity {

    private BottomNavigationView mMainNav;
    private FrameLayout mMainFrame;
    private HistoryFragment historyFragment;
    private MeetingFragment meetingFragment;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        StrictMode.VmPolicy.Builder builder = new StrictMode.VmPolicy.Builder();
        StrictMode.setVmPolicy(builder.build());

        setContentView(R.layout.activity_main);

        mMainNav = (BottomNavigationView) findViewById(R.id.bottom_nav);
        mMainFrame = (FrameLayout) findViewById(R.id.main_frame);

        historyFragment = new HistoryFragment();
        meetingFragment = new MeetingFragment();

        setFragment(meetingFragment);

        mMainNav.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
                switch (menuItem.getItemId()) {
                    case R.id.meeting_tab:
                        mMainNav.setItemBackgroundResource(R.color.design_default_color_primary);
                        setFragment(meetingFragment);
                        return true;
                    case R.id.meeting_history:
                        mMainNav.setItemBackgroundResource(R.color.colorAccent);
                        setFragment(historyFragment);
                        return true;
                }
                return false;
            }
        });
    }

    private void setFragment(Fragment fragment) {
       FragmentTransaction fragmentTransaction = getSupportFragmentManager().beginTransaction();
       fragmentTransaction.replace(R.id.main_frame, fragment);
       fragmentTransaction.commit();
    }
}

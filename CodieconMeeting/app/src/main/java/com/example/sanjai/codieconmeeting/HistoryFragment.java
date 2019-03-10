package com.example.sanjai.codieconmeeting;

import android.content.Context;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v7.widget.DefaultItemAnimator;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;


/**
 * A simple {@link Fragment} subclass.
 * Activities that contain this fragment must implement the
 * create an instance of this fragment.
 */
public class HistoryFragment extends Fragment {

    RecyclerView recyclerView;
    String items[] = {"item1", "item2","item3","item4","item5","item6","item7","item8","item9","item10","item11"};

    public HistoryFragment() {
        // Required empty public constructor
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_history, container, false);
        recyclerView = (RecyclerView) view.findViewById(R.id.recycleview);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));
        MeetingHistoryAdapter meetingHistoryAdapter = new MeetingHistoryAdapter(getActivity(), items);
        recyclerView.setAdapter(meetingHistoryAdapter);
        recyclerView.setItemAnimator(new DefaultItemAnimator());
        return view;
    }


}

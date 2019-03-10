package com.example.sanjai.codieconmeeting;


import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import android.os.AsyncTask;
import android.util.Log;


class HandlingData extends AsyncTask<String , Void, String> {
    private Exception exception;
    protected String doInBackground(String... arr) {
        URL url = null;
        HttpURLConnection urlConnection = null;
        Log.d("Hello", "1");
        try {
            Log.d("Sanket 122 ", arr[0]);
            url = new URL("http://192.168.43.140:8080/AudioProcessor/send_audio");
            urlConnection = (HttpURLConnection) url.openConnection();
            urlConnection.setRequestMethod("POST");
            urlConnection.setConnectTimeout(200000);
            urlConnection.setReadTimeout(200000);
            urlConnection.setDoOutput(true);
            urlConnection.setRequestProperty("Content-Type", "application/json");
            urlConnection.setRequestProperty("charset", "utf-8");

            arr[0] = arr[0].replace("\n", "");
            String json = "{ \"key\": \"" + arr[0] + "\"}";
            Log.d("Sanket", "12445" + arr[0]);
            try (DataOutputStream wr = new DataOutputStream(urlConnection.getOutputStream())) {
                wr.write(json.getBytes("UTF-8"));
            } catch (Exception e) {
                Log.d("Sanket Error ", e.toString());
            };

            // Log.d("Sanket ", urlConnection.getInputStream()+" ");
            InputStream in = new BufferedInputStream(urlConnection.getInputStream());
            Log.d("Sanket", "4");
            String s = readStream(in);
            in.close();
            Log.d("Sanket Resp", s);
            return s;
        } catch (Exception e) {
            Log.d("Sanket", "Exception");
            e.printStackTrace();
        } finally {
            Log.d("Sanket", "Finally");
            if (urlConnection != null) urlConnection.disconnect();
        }
        Log.d("Sanket", "Return Null");
        return "";
    }

    private String readStream(InputStream in) {
        try {
            ByteArrayOutputStream result = new ByteArrayOutputStream();
            byte[] buffer = new byte[1024];
            int length;
            while ((length = in.read(buffer)) != -1) {
                result.write(buffer, 0, length);
            }
// StandardCharsets.UTF_8.name() > JDK 7

            return result.toString("UTF-8");
        } catch (Exception e) {
            return "";
        }

    }

}
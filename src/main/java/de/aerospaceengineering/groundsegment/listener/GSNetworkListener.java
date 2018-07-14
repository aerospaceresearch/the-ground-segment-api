package de.aerospaceengineering.groundsegment.listener;

import de.aerospaceengineering.groundsegment.GSExecutor;
import de.aerospaceengineering.groundsegment.exception.GSException;
import de.aerospaceengineering.groundsegment.logging.GSLoggable;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class GSNetworkListener implements GSListener {

    private Integer p;
    private GSExecutor exec;

    public GSNetworkListener(Integer port, GSExecutor cmd){
        p = port;
        exec = cmd;
    }

    @Override
    public void run(){
        try {
            ServerSocket sock = new ServerSocket(p);
            Socket conn = sock.accept();
            BufferedReader in =
                    new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String inp;
            String json = "";
            while ((inp = in.readLine()) != null) {
                json += inp;
            }
            try {
                exec.process(new JSONObject(json));
            } catch (GSException e){
                return;
            }
        } catch (IOException e) {
            new GSException("Unable to read from Socket");
            return;
        }
    }
}

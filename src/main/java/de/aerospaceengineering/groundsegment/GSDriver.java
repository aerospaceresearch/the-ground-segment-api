package de.aerospaceengineering.groundsegment;

import de.aerospaceengineering.groundsegment.exception.GSException;
import de.aerospaceengineering.groundsegment.listener.GSHotFolderListener;
import de.aerospaceengineering.groundsegment.listener.GSNetworkListener;
import de.aerospaceengineering.groundsegment.logging.GSLoggable;
import org.apache.commons.io.FileUtils;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class GSDriver implements GSLoggable {

    private List<Thread> listeners = new ArrayList<>();

    private void startUp(JSONObject config) throws GSException {
        if (!config.has("commanddir"))
            throw new GSException("No command directory specified");
        if (!config.has("listeners"))
            throw new GSException("No listeners specified");
        GSExecutor exec = new GSExecutor(new File(config.getString("commanddir")).toPath());
        JSONArray lis = config.getJSONArray("listeners");
        for (int i = 0; i < lis.length(); i++) {
            JSONObject l = lis.getJSONObject(i);
            if (l.has("hotfolder"))
                listeners.add(new Thread(new GSHotFolderListener(new File(l.getString("hotfolder")).toPath(), exec)));
            else if (l.has("network"))
                listeners.add(new Thread(new GSNetworkListener(l.getInt("network"), exec)));
            else
                throw new GSException("Invalid listener type in " + l.toString());
        }
        for (Thread i : listeners) {
            i.start();
        }
    }

    public void interrupt() {
        for (Thread i : listeners) {
            i.interrupt();
        }
    }

    public GSDriver(JSONObject obj) throws GSException {
        startUp(obj);
    }

    public GSDriver(String s) throws GSException {
        this(new JSONObject(s));
    }

    public GSDriver(Path p) throws GSException {
        if (!p.toFile().isFile())
            throw new GSException("Provided configuration Path does not refer to a File");
        String string = "";
        try {
            string = FileUtils.readFileToString(new File(p.toString()), Charset.defaultCharset());
        } catch (IOException e) {
            throw new GSException("Unable to read from configuration file");
        }
        startUp(new JSONObject(string));
    }
}

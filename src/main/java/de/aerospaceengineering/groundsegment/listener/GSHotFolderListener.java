package de.aerospaceengineering.groundsegment.listener;

import de.aerospaceengineering.groundsegment.GSExecutor;
import de.aerospaceengineering.groundsegment.exception.GSException;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class GSHotFolderListener implements GSListener {
    private GSExecutor cmd;
    private Path hf;

    public GSHotFolderListener(Path hotfolder, GSExecutor exec) {
        hf = hotfolder;
        cmd = exec;
    }

    private void handleDirectory(Path dir) throws GSException{
        File f = new File(dir.toUri());
        String text;
        if (f.isFile()) {
            try {
                text = new String(Files.readAllBytes(Paths.get(f.toURI())));
            } catch (IOException e){
                throw new GSException("Unable to read from File " + f.toString());
            }
            JSONObject obj ;
            try {
                obj = new JSONObject(text);
            } catch (JSONException e){
                throw new GSException("Unable to create json from file " + f.toString());
            }
            cmd.process(obj);
            if (!f.delete()) {
                throw new GSException("Unable to delete file " + f.toString());
            }
        } else if (f.isDirectory()) {
            File[] listing = f.listFiles();
            if (listing != null) {
                for (File child : listing) {
                    handleDirectory(child.toPath());
                }
            }
            if (!f.toPath().toString().equals(hf.toString())) {
                if (!f.delete()) {
                    throw new GSException("Unable to remove directory " + f.toString());
                }
            }
        } else {
            throw new GSException("Unknown or invalid file type " + f.toString());
        }
    }
    @Override
    public void run(){
        while(true){
            try {
                handleDirectory(hf);
                Thread.sleep(10000);
            } catch (InterruptedException | GSException e) {
                return;
            }
        }
    }
}

package de.aerospaceengineering.groundsegment;

import de.aerospaceengineering.groundsegment.exception.GSException;
import de.aerospaceengineering.groundsegment.logging.GSLoggable;
import org.json.JSONObject;

import java.io.File;
import java.nio.file.Path;

public class GSExecutor implements GSLoggable {
    private Path cmdpath;

    public JSONObject process(JSONObject obj) throws GSException {
        if(! obj.has("command")){
            throw new GSException("Provided command has no command : " + obj.toString());
        } else if (! obj.has("args")){
            throw new GSException("Provided command has no arguments : " + obj.toString());
        } else if (! obj.has("name")){
            throw new GSException("Provided command has no name : " + obj.toString());
        }
        return obj;
    }

    public GSExecutor(Path p) throws GSException{
        cmdpath = p;
        if(! new File(cmdpath.toString()).isDirectory()){
            throw new GSException("Provided cmdpath is not a directory");
        }
    }
}

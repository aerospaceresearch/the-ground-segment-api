package de.aerospaceengineering.groundsegment.exception;

import de.aerospaceengineering.groundsegment.logging.GSLoggable;

public class GSException extends Exception implements GSLoggable {
    public GSException(String description){
        this(LogLevel.FATAL, description);
    }

    public GSException(LogLevel l, String description){
        GSLoggable.log(l, description);
    }
}

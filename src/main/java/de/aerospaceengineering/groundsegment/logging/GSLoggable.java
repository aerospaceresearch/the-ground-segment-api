package de.aerospaceengineering.groundsegment.logging;

import java.util.Date;

public interface GSLoggable {

    enum LogLevel {
        INFO, WARN, ERROR, FATAL
    }

    static void log(String s) {
        log(LogLevel.FATAL, s);
    }

    static void log(LogLevel l, String s) {
        Date t = new Date();
        GSLogPool.add(new GSLogMessage(l,s,t));
    }
}

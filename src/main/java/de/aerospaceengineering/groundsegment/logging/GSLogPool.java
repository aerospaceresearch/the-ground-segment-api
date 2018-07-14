package de.aerospaceengineering.groundsegment.logging;

import java.util.ArrayList;
import java.util.List;

public final class GSLogPool {
    private static boolean failed = false;
    private static boolean stdout = false;

    private static List<GSLogMessage> log = new ArrayList<>();

    public static void clear() {
        log = new ArrayList<>();
        failed = false;
    }

    public static GSLogMessage get(int i) {
        return log.get(i);
    }

    public static GSLogMessage getLast() {
        return log.get(log.size() - 1);
    }

    public static int length() {
        return log.size();
    }

    public static boolean isFailed() {
        return failed;
    }

    public static void enableStdoutLogging(boolean b) {
        stdout = b;
    }

    public static void add(GSLogMessage m) {
        if (stdout)
            System.out.println(m.toString());
        if (m.getLogLevel() == GSLoggable.LogLevel.ERROR || m.getLogLevel() == GSLoggable.LogLevel.FATAL)
            failed = true;
        log.add(m);
    }
}

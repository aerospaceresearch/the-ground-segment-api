package de.aerospaceengineering.groundsegment.logging;

import java.util.Date;

public class GSLogMessage {
    private GSLoggable.LogLevel log;
    private String desc;
    private Date date;

    public GSLoggable.LogLevel getLogLevel(){
        return log;
    }

    public String getDescription(){
        return desc;
    }

    public Date getDate(){
        return date;
    }

    @Override
    public String toString(){
        String msg = "";
        switch (log){
            case INFO:
                msg = "INFO  : ";
                break;
            case WARN:
                msg = "WARN  : ";
                break;
            case ERROR:
                msg = "ERROR : ";
                break;
            case FATAL:
                msg = "FATAL : ";
                break;
        }
        msg = msg + date.getHours()+"-"+date.getMinutes()+"-"+date.getSeconds() + " : " +  desc;
        return msg;
    }

    public GSLogMessage(GSLoggable.LogLevel l, String description, Date d){
        log = l;
        desc = description;
        date = d;
    }
}

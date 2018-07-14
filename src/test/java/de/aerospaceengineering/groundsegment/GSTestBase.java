package de.aerospaceengineering.groundsegment;

import de.aerospaceengineering.groundsegment.logging.GSLogPool;
import org.apache.commons.io.FileUtils;

import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.nio.file.Path;
import java.util.GregorianCalendar;

import static org.junit.jupiter.api.Assertions.fail;

public abstract class GSTestBase {

    protected String tmpdir;
    protected String hotdir;
    protected String cmddir;

    protected void createDirs(){
        tmpdir = System.getProperty("java.io.tmpdir").replace("\\", "\\\\") + "test" + GregorianCalendar.getInstance().getTimeInMillis();
        hotdir = System.getProperty("java.io.tmpdir").replace("\\", "\\\\") + "test" + File.separator + File.separator + "hotfolder";
        cmddir = System.getProperty("java.io.tmpdir").replace("\\", "\\\\") + "test" + File.separator + File.separator + "commands";
        deleteDirs();
        new File(tmpdir).mkdirs();
        new File(hotdir).mkdirs();
        new File(cmddir).mkdirs();
        GSLogPool.clear();
        GSLogPool.enableStdoutLogging(true);
    }

    protected void deleteDirs(){
        try {
            FileUtils.deleteDirectory(new File(tmpdir));
            FileUtils.deleteDirectory(new File(hotdir));
            FileUtils.deleteDirectory(new File(cmddir));
            GSLogPool.clear();
            GSLogPool.enableStdoutLogging(false);
        } catch (IOException e) {
            fail("Unable to delete temporary files");
            return;
        }
    }

    protected Path writeConfig(String s) throws IOException {
        File ret = new File(tmpdir + File.separator + "config.json");
        ret.createNewFile();
        try (PrintWriter o = new PrintWriter(ret.toString())) {
            o.println(s);
        }
        return ret.toPath();
    }

    protected void sendLocalhost(Integer p, String s) throws IOException {
            Socket socket = null;
            OutputStreamWriter osw;
            try {
                socket = new Socket(InetAddress.getByName(null), p);
                osw =new OutputStreamWriter(socket.getOutputStream(), "UTF-8");
                osw.write(s, 0, s.length());
                osw.flush();
            } catch (IOException e) {
                System.err.print(e);
            } finally {
                socket.close();
            }
    }

    protected Path writeHotFolder(String s) throws IOException {
        File ret = new File(hotdir + File.separator + File.separator + "test"+GregorianCalendar.getInstance().getTimeInMillis() + "json");
        ret.createNewFile();
        try (PrintWriter o = new PrintWriter(ret.toString())) {
            o.println(s);
        }
        return ret.toPath();
    }
}

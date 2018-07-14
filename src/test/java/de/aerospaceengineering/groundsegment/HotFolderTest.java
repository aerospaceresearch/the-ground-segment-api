package de.aerospaceengineering.groundsegment;

import de.aerospaceengineering.groundsegment.exception.GSException;
import de.aerospaceengineering.groundsegment.logging.GSLogPool;
import org.junit.jupiter.api.Test;
import java.io.IOException;
import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.fail;

public class HotFolderTest extends GSTestBase {

    @Test
    public void ValidHotFolderInput() {
        createDirs();
        try {
            Path cfg = writeConfig("{ \"commanddir\" : \".\", \"listeners\" : [{\"hotfolder\" : \"" + hotdir + "\"}]}");
            try {
                writeHotFolder("{ \"name\" : \"test\", \"command\" : \"echo\" , \"args\" : \"test\" }");
                writeHotFolder("{ \"name\" : \"test\", \"command\" : \"echo\" , \"args\" : \"test\" }");
                GSDriver d = null;
                try {
                    d = new GSDriver(cfg);
                } catch (GSException e) {
                    fail("Exception on valid configuration");
                }
                Thread.sleep(20000);
                d.interrupt();
                if(GSLogPool.isFailed()){
                    fail("Unexpected error during hotfolder execution");
                }
            } catch (InterruptedException e) {
                fail("Could not wait for hotfolder execution");
            }
        } catch (IOException e) {
            fail("File creation failed");
        } finally {
            deleteDirs();
        }
    }

    @Test
    public void InvalidHotFolderInput() {
        createDirs();
        try {
            Path cfg = writeConfig("{ \"commanddir\" : \".\", \"listeners\" : [{\"hotfolder\" : \"" + hotdir + "\"}]}");
            try {
                writeHotFolder("{ \"command\" : \"echo\" , \"args\" : \"test\" }");
                GSDriver d = null;
                try {
                    d = new GSDriver(cfg);
                    Thread.sleep(20000);
                    d.interrupt();
                    if(! GSLogPool.isFailed()) {
                        fail("Invalid command not found");
                    }
                } catch (GSException e) {
                    Thread.sleep(20000);
                    d.interrupt();
                    return;
                }
            } catch (InterruptedException e) {
                fail("Interrupted thread exception");
            }
        } catch (IOException e) {
            fail("File creation failed");
        } finally {
            deleteDirs();
        }
    }
}

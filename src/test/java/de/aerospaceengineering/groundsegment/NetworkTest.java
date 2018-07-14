package de.aerospaceengineering.groundsegment;

import de.aerospaceengineering.groundsegment.exception.GSException;
import de.aerospaceengineering.groundsegment.logging.GSLogPool;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Path;

import static org.junit.jupiter.api.Assertions.fail;

public class NetworkTest extends GSTestBase {

    @Test
    public void InvalidNetworkInput() {
        createDirs();
        try {
            Path cfg = writeConfig("{ \"commanddir\" : \".\", \"listeners\" : [{\"network\" : \"3003\"}]}");
            GSDriver d = null;
            try {
                d = new GSDriver(cfg);
            } catch (GSException e) {
                fail("Exception on valid configuration");
            }
            sendLocalhost(3003, "{ \"name\" : \"test\", \"command\" : \"echo\"}");
            try {
                Thread.sleep(20000);
            } catch (InterruptedException e){
                fail("Thread interruption exception");
            }
            d.interrupt();
            if (! GSLogPool.isFailed()) {
                fail("Expected Exception not thrown on invalid input ");
            }
        } catch (IOException e) {
            fail("Error writing configuration");
        } finally {
            deleteDirs();
        }
    }

    @Test
    public void ValidNetworkInput() {
        createDirs();
        try {
            Path cfg = writeConfig("{ \"commanddir\" : \".\", \"listeners\" : [{\"network\" : \"3003\"}]}");
            GSDriver d = null;
            try {
                d = new GSDriver(cfg);
            } catch (GSException e) {
                fail("Exception on valid configuration");
            }
            sendLocalhost(3003, "{ \"name\" : \"test\", \"command\" : \"echo\" , \"args\" : \"test\" }");
            try {
                Thread.sleep(20000);
            } catch (InterruptedException e){
                fail("Thread interruption exception");
            }
            d.interrupt();
            if (GSLogPool.isFailed()) {
                 fail("Error during network receiving");
            }
        } catch (IOException e) {
            fail("Error writing configuration");
        } finally {
            deleteDirs();
        }
    }
}

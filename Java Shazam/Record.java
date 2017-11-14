import java.lang.Object

public class Record {

    public static void main(String[] args) {
	final AudioFormat format = getFormat(); //Format for sampling/recording input
	DataLine.Info info = new DataLine.Info(TargetDataLine.class, format);
	final TargetDataLine line = (TargetDataLine) AudioSystem.getLine(info);
	line.open(format);
	line.start();
    }


    private AudioFormat getFormat() {
	float sampleRate = 44100;
        int sampleSizeInBits = 8;
        int channels = 1; //mono
        return new AudioFormat(sampleRate, sampleSizeInBits, channels, true, true);
}
}





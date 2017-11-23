private class Data {

    private int time;
    private int freqHash;
    private String name;

    public Data(String name, int songHash, int time) {
        this.songId = freqHash;
        this.time = time;
	this.name = name;
    }
	
    public int getTime() {
        return time;
    }
    public int getSongHash() {
        return freqHash;
    }
    public String getName() {
        return name;
    }
}

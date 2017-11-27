import package Java Shazam;
package Samples;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.HashMap;


public class Database {

     private Hashmap<String, Music> Library;
     private Hashmap<long, Data> DataLibrary;
     private static final int hash_factor = 2;
     public final int[] bins = new int[] { 40, 80, 120, 180, 300 };  

     public static void main(String[] args) {
         library = new Hashmap<String, Music>();
         /*** 1) load in music from txt file**/
         /*** 2) Fingerprint song into other database***/ 
	 try {
	     File file = new File("TrackList.txt");
	     FileReader fileReader = new FileReader(file);
	     BufferedReader bufferedReader = new BufferedReader(fileReader);

	     while ((line = bufferedReader.readLine()) != null) {
		 Music track = new Music(line);
		 library.put(line, track);
		 fingerprint(track);
	         System.out.println(line);
	     }
	     fileReader.close();
	     System.out.println("Finished loading for TrackList.txt");
         } catch (IOException e) {
	     e.printStackTrace();
	 }
     }
     

     public void fingerprint(Music song) {
	 Clip track = song.getSound();
         int size = 1024;
	 int iterations = track.getFrameLength();
         for(int i = 0; i < iterations; i+=size) {
	     Complex[] chunk = fft();
	     long hashcode = hash();
	     Datalibrary.put(hashcode, new Data(song.getName(), hashcode, i));
	 }
     }

     /*** 
     Use to Hash the selected frequencies in a given window. 
     Arguments:
     Line = input string of frequencies
     ***/
     private long hash(String line) {
         String[] p = line.split("\t");
         long p1 = Long.parseLong(p[0]);
         long p2 = Long.parseLong(p[1]);
         long p3 = Long.parseLong(p[2]);
         long p4 = Long.parseLong(p[3]);
         return  (p4-(p4%hash_factor)) * 100000000 + (p3-(p3%hash_factor)) * 100000 + (p2-(p2%	hash_factor)) * 100 + (p1-(p1%hash_factor));
     }


}

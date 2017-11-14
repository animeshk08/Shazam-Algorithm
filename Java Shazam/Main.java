


public final class Main {


     private static final int FUZ_FACTOR = 2;

     public static void main(String[] args) {
	
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
         return  (p4-(p4%FUZ_FACTOR)) * 100000000 + (p3-(p3%FUZ_FACTOR)) * 100000 + (p2-(p2%	FUZ_FACTOR)) * 100 + (p1-(p1%FUZ_FACTOR));
     }
}

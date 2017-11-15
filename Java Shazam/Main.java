


public final class Main {


     private static final int hash_factor = 2;
     public final int[] bins = new int[] { 40, 80, 120, 180, 300 };

     public static void main(String[] args) {



     }

     /*** 
     Used to find which frequency range we are in
     Arguments:
     freq = input frequency
     Output = index within bins
     ***/
     public int getIndex(int freq) {
         int i = 0;
         while (bin[i] < freq)
             i++;
         return i;
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

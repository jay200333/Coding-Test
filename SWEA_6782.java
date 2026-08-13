import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class SWEA_6782 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());
    for (int t = 1; t <= T; t++) {
      long n = Long.parseLong(br.readLine());
      long answer = 0;

      while (n > 2) {
        if (Math.sqrt((double)n) == (long)Math.sqrt(n)) {
          n = (long)Math.sqrt(n);
          answer++;
        }
        else {
          double power = Math.ceil(Math.sqrt(n));
          long b = (long)Math.pow(power, 2);
          answer += (b - n);
          n = b;
        }
      }
      System.out.println(String.format("#%d %d", t, answer));
    }
  }
}
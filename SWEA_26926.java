import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import static java.lang.Math.*;
import java.util.*; 

public class SWEA_26926 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

    int T = Integer.parseInt(br.readLine());
    for (int t = 1; t <= T; t++) {
      int n = Integer.parseInt(br.readLine());
      ArrayList<Integer> scores = new ArrayList<>();
      StringTokenizer st = new StringTokenizer((br.readLine()));
      for (int i = 0; i < n; i++) {
        scores.add(Integer.parseInt(st.nextToken()));
      }
      int answer = 0;
      for (int i = n-2; i >=0; i--) {
        int count = 0;
        for (int j = n-1; j > i; j--) {
          if (scores.get(i) > scores.get(j)){
            count++;
          }
        }
        answer = max(answer, count);
      }
      System.out.println(String.format("#%d %d", t, answer));
    }
  }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

public class SWEA_26923 {
  public static void main(String[] args) throws IOException {
    InputStream in = System.in;
    InputStreamReader reader = new InputStreamReader(in);
    BufferedReader br = new BufferedReader(reader);

    int T = Integer.parseInt(br.readLine());
    for (int t = 1; t <= T; t++) {

      int n = Integer.parseInt(br.readLine());
      ArrayList<Integer> countList = new ArrayList<>();
      StringTokenizer st = new StringTokenizer((br.readLine()));
      for (int i = 0; i < n; i++) {
        countList.add(Integer.parseInt(st.nextToken()));
      }
      int answer = Collections.max(countList) - Collections.min(countList);
      System.out.println(String.format("#%d %d", t, answer));
    }
  }
}

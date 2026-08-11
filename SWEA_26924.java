import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class SWEA_26924 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());
    for (int t = 1; t <= T; t++) {
      StringTokenizer st = new StringTokenizer((br.readLine()));

      int k = Integer.parseInt(st.nextToken());
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());

      ArrayList<Integer> courseList = new ArrayList<>();
      courseList.add(0);
      st = new StringTokenizer((br.readLine()));

      for (int i = 0; i < m; i++) {
        courseList.add(Integer.parseInt(st.nextToken()));
      }
      courseList.add(n);
      Collections.sort(courseList);
      
      int cur_idx = 0;
      int answer = 0;
      
      while(cur_idx < courseList.size() - 1){
        int next_idx = cur_idx;
        while(next_idx < courseList.size() - 1 && (courseList.get(next_idx + 1) - courseList.get(cur_idx)) <= k){
          next_idx++;
        }

        if (next_idx == cur_idx) {
          answer = 0;
          break;
        }

        if (courseList.get(next_idx) < n) {
          answer++;
        }

        cur_idx = next_idx;
      }

      System.out.println(String.format("#%d %d", t, answer));
    }
  }
}

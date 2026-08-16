import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());

    for (int t = 1; t <= T; t++) {
      Object answer;
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      int countA = binsect_search(1, n, a);
      int countB = binsect_search(1, n, b);
      if (countA == countB) {
        answer = 0;
      }
      else if (countA > countB) {
        answer = 'B';
      }
      else answer = 'A';
      System.out.println(String.format("#%d %s", t, answer));
    }
  }

  public static int binsect_search(int start, int end, int target) {
    int count = 0;
    while (start <= end) {
      int mid = (int)((start + end) / 2);
      if (target == mid) return count;
      else if (target > mid) {
        start = mid;
      }
      else {
        end = mid;
      }
      count++;
    }
    return Integer.MAX_VALUE;
  }
}

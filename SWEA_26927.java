import java.util.*;

public class SWEA_26927 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int T = sc.nextInt();
        
        for (int t = 1; t <= T; t++) {
            int n = sc.nextInt();
            String numbersStr = sc.next();
            
            Map<Integer, Integer> counter = new HashMap<>();
            
            for (int i = 0; i < numbersStr.length(); i++) {
                int num = numbersStr.charAt(i) - '0';
                counter.put(num, counter.getOrDefault(num, 0) + 1);
            }
            
            List<Integer> keys = new ArrayList<>(counter.keySet());
            
            Collections.sort(keys, (a, b) -> {
                int countA = counter.get(a);
                int countB = counter.get(b);
                
                if (countA != countB) {
                    return Integer.compare(countB, countA);
                }
                return Integer.compare(b, a);
            });
            
            int mostFrequentNum = keys.get(0);
            int maxCount = counter.get(mostFrequentNum);
            
            System.out.printf("#%d %d %d%n", t, mostFrequentNum, maxCount);
        }
        
        sc.close();
    }
}
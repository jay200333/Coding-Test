
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class SWEA_4193 {

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    static int n;
    static int[][] graph;
    static int startX, startY, targetX, targetY;

    static class Node {

        int x, y;

        Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine().trim());

        for (int t = 1; t < T + 1; t++) {
            n = Integer.parseInt(br.readLine().trim());
            graph = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            st = new StringTokenizer(br.readLine());
            startX = Integer.parseInt(st.nextToken());
            startY = Integer.parseInt(st.nextToken());
            
            st = new StringTokenizer(br.readLine());
            targetX = Integer.parseInt(st.nextToken());
            targetY = Integer.parseInt(st.nextToken());

            int answer = bfs();
            System.out.println("#" + t + " " + answer);
        }
    }

    static int bfs() {
      Queue<Node> queue = new LinkedList<>();
            boolean[][] visited = new boolean[n][n];
            
            visited[startX][startY] = true;
            queue.add(new Node(startX, startY));

            int answer = 0;
        
        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            boolean[][] waitingNodes = new boolean[n][n];
            
            for (int q = 0; q < queueSize; q++) {
                Node cur = queue.poll();
                
                if (cur.x == targetX && cur.y == targetY) {
                    return answer;
                }
                
                for (int i = 0; i < 4; i++) {
                    int nx = cur.x + dx[i];
                    int ny = cur.y + dy[i];
                    
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n || graph[nx][ny] == 1) {
                        continue;
                    }
                    
                    if (graph[nx][ny] == 0 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        queue.add(new Node(nx, ny));
                    }

                    // 소용돌이 대기 or 이동
                    else if (graph[nx][ny] == 2 && !visited[nx][ny]) {
                        if ((answer+1) % 3 == 0) {
                            visited[nx][ny] = true;
                            queue.add(new Node(nx, ny));
                        } else {
                            if (!waitingNodes[cur.x][cur.y]) {
                                waitingNodes[cur.x][cur.y] = true;
                                queue.add(new Node(cur.x, cur.y));
                            }
                        }
                    }
                }
            }
            answer++;
        }
        return -1;
    }
}

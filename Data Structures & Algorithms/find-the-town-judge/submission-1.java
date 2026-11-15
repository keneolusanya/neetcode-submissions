class Solution {
    public int findJudge(int n, int[][] trust) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        // initialize adjacency list
        for (int i = 1; i < n + 1; i++) {        
            adj.put(i, new ArrayList<>());
        }   

        // update adjacency list with trust
        for (int i = 0; i < trust.length; i++) {     
            adj.get(trust[i][0]).add(trust[i][1]);
        }
        
        // candidate must trust no one
        int cand = -1;
        for (int i = 1; i < n + 1; i++) {     
            if (adj.get(i).size() == 0) {
                cand = i;
                break;
            }
        }

        // may return early (everyone trusts someone)
        if (cand == -1) {
            return cand;
        }

        // make sure no one trusts thay candidate
        for (int key: adj.keySet()) {
            if (key != cand) {
                if (!adj.get(key).contains(cand)) {
                    return -1;
                }
            }
        }

        return cand;
    }
}
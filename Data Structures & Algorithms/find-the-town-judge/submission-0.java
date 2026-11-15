class Solution {
    public int findJudge(int n, int[][] trust) {
        // judge trusts no one and everyone else trusts the judge
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 1; i < n + 1; i++) {        
            adj.put(i, new ArrayList<>());
        }   

        for (int i = 0; i < trust.length; i++) {     
            adj.get(trust[i][0]).add(trust[i][1]);
        }

        // doesn't trust anyone
        // everyone trusts them


        int cand = -1;
        // check who doesn't trust anyone
        for (int i = 1; i < n + 1; i++) {     
            if (adj.get(i).size() == 0) {
                cand = i;
                break;
            }
        }

        if (cand == -1) {
            return cand;
        }

        // check if everyone trusts them
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
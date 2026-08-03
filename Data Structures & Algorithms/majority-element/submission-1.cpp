class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        int a = nums.size() / 2;
        std::unordered_map<int, int> myMap;

        for (int i = 0; i < nums.size(); i++) {
            if (myMap[nums[i]] == a) {
                return nums[i];
            }
            myMap[nums[i]]++;
        }
    }
};
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    bool hasCycle(ListNode* head) {
        std::set<ListNode*> my_set;
        ListNode *curr = head;

        while(curr != nullptr){
            ListNode *curr_pt = curr;
            if (my_set.find(curr_pt) != my_set.end()) { 
                return true;
            } 
            my_set.insert(curr_pt);
            curr = curr->next;
        }

        return false;
    }
};

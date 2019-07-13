/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // 思路同Python解法
        ListNode *rst = new ListNode(-1), *current = rst;
        while(l1 && l2){
            if(l1->val <= l2->val){
                current->next = l1;
                l1 = l1->next;
            }
            else{
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        current->next = l1?l1:l2;
        return rst->next;

    }
};

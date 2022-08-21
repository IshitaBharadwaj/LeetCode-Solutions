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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *p=head;
        ListNode *q=NULL;
        while(p!=NULL){
            q=p;
            p=p->next;
            while(p!=NULL && q->val==p->val){
                p=p->next;
                q->next=p;
                
            }
        }
        return head;
    }
};
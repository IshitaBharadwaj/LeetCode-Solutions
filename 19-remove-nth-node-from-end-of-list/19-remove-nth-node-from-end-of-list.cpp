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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *p=head;
        int count=0;
        while(p!=NULL){
            count++;
            p=p->next;
        }
        int remove= count-n;
        int i=0;
        ListNode *q=head;
        ListNode *r=NULL;
        if(i==remove){
            head=head->next;
        }
        else{
            while(i<remove && q!=NULL){
                r=q;
                q=q->next;
                i+=1;
            }
            r->next=q->next;    

        }
        return head;
        
    }
};
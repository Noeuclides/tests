SinglyLinkedListNode* removeNodesJav(SinglyLinkedListNode* listHead, int x) {
   
    SinglyLinkedListNode *headref;
    SinglyLinkedListNode *prev;

    headref = listHead;

    while (listHead != NULL || listHead->data > x){
        listHead = listHead->next; 
    }
    headref = listHead;
    prev = listHead;
    while (prev != NULL){
        
        if(headref != NULL)
        {
            headref = headref->next;
            if (headref->data > x){
                prev->next = headref->next;
            }
        }
        if(prev->next != NULL)
            prev = prev->next;
    }

    return(listHead);   
    
}



    version 2

    SinglyLinkedListNode* removeNodes(SinglyLinkedListNode* listHead, int x) {
    SinglyLinkedListNode *deln;
    SinglyLinkedListNode *prev;

    deln = listHead;
    while (deln == listHead && deln != NULL){
        if (deln->data > x){
            listHead = listHead->next;
            deln = listHead;
        }
        else{
            deln = deln->next;
        }
    }
    prev = listHead;
    for (;deln != NULL; deln = deln->next){
        if (deln->data > x){
            prev->next = deln->next;
            deln = prev;
        }
        prev = deln;
    }
    return(listHead);   

}
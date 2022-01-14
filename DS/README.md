# Data Structres

## 1. Linked List

- Linked lists are an ordered collection of objects.

- Linked lists differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.

    ### Node

    - Each element of a linked list is called a __node__, and every node has two different fields:

        1. __Data__ contains the value to be stored in the node.
        2. __Next__ contains a reference to the next node on the list.

    ![Node](images/LL_Node.webp)

- A linked list is a collection of nodes.

- The __first node is called the head__, and it’s used as the starting point for any iteration through the list.

- The last node must have its next reference pointing to None to determine the end of the list

![A simple Linked List](images/LL.webp)

### Common LL methods

1. Insert at front
2. Insert at end
3. Delete at front
4. Delete at end
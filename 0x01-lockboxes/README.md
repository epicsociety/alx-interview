Create a new list of keys from the opened boxes

The first box is open and hence

```
keysForBoxes = list(set(box[0] | {0}))
```

The iterate through this list, open the boxes that you can and add the new keys in the list

Do this until the last key in the list has opened a box

Then check if the list of keys is equal to the list of boxes

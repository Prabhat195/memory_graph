# Memory Graph - Common Mistakes (Hindi Explanation)

These examples are provided to help Hindi-speaking students understand common Python memory concepts using the `memory_graph` package.

## 1. List Aliasing (लिस्ट अलियासिंग)
**Hindi Explanation:** 
कई बार छात्रों को लगता है कि `list_b = list_a` लिखने से एक नई लिस्ट बन जाती है। लेकिन असल में दोनों वेरिएबल्स एक ही मेमोरी लोकेशन को पॉइंट करते हैं (इसे Aliasing कहते हैं)। इसलिए अगर हम `list_b` में कुछ जोड़ते हैं, तो `list_a` भी बदल जाता है। `memory_graph` इसे बहुत स्पष्ट रूप से दिखाता है।

**English Translation:** 
Often, students think writing `list_b = list_a` creates a new, independent list. But in reality, both variables point to the exact same memory location (this is called Aliasing). Therefore, if we append an item to `list_b`, `list_a` is also modified. `memory_graph` visualizes this shared reference very clearly.

**Code Example:**
```python
import memory_graph

# A common mistake students make with lists
list_a = [10, 20, 30]
list_b = list_a  # Students often think this creates a new independent list

list_b.append(40) # Modifying list_b also modifies list_a

memory_graph.render(locals(), 'aliasing_graph.png')


## 2. Shallow Copy vs Deep Copy (शैलो कॉपी और डीप कॉपी)
**Hindi Explanation:** 
नेस्टेड लिस्ट्स (लिस्ट के अंदर लिस्ट) में `.copy()` का इस्तेमाल करने पर सिर्फ बाहर की लिस्ट कॉपी होती है (इसे Shallow Copy कहते हैं)। अंदर की लिस्ट्स अभी भी पुराने वाले रेफरेंस ही शेयर करती हैं। इसका मतलब है कि अंदर के एलिमेंट को बदलने से दोनों लिस्ट बदल जाती हैं। अगर हमें पूरी तरह से नई कॉपी चाहिए, तो हमें `copy.deepcopy()` का इस्तेमाल करना होगा।

**English Translation:** 
When using `.copy()` on nested lists (lists inside lists), only the outer list is copied (this is a Shallow Copy). The inner lists still share the old memory references. This means modifying an inner element changes both lists. To get a completely independent copy, students must learn to use `copy.deepcopy()`.

**Code Example:**
```python
import memory_graph
import copy

# Dealing with 2D arrays/nested lists
original_matrix = [[1, 2], [3, 4]]
copied_matrix = original_matrix.copy() 

# This changes both matrices!
copied_matrix[0][0] = 99 

memory_graph.render(locals(), 'shallow_copy_graph.png')

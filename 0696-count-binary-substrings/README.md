<h2><a href="https://leetcode.com/problems/count-binary-substrings">696. Count Binary Substrings</a></h2><h3>Easy</h3><hr><p>Given a binary string <code>s</code>, return the number of non-empty substrings that have the same number of <code>0</code>&#39;s and <code>1</code>&#39;s, and all the <code>0</code>&#39;s and all the <code>1</code>&#39;s in these substrings are grouped consecutively.</p>

<p>Substrings that occur multiple times are counted the number of times they occur.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;00110011&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 substrings that have equal number of consecutive 1&#39;s and 0&#39;s: &quot;0011&quot;, &quot;01&quot;, &quot;1100&quot;, &quot;10&quot;, &quot;0011&quot;, and &quot;01&quot;.
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, &quot;00110011&quot; is not a valid substring because all the 0&#39;s (and 1&#39;s) are not grouped together.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;10101&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 substrings: &quot;10&quot;, &quot;01&quot;, &quot;10&quot;, &quot;01&quot; that have equal number of consecutive 1&#39;s and 0&#39;s.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

For your code:

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        n = len(s)
        count1 = 0
        while(j<n):
            while(j<n and s[j]!='1'):
                j+=1
            count0 = (j-i)
            i = j
            ans+=min(count0,count1)
            while(j<n and s[j]!='0'):
                j+=1
            count1 = (j-i)
            i = j
            ans+=min(count0,count1)
        return ans
```

### Time Complexity: **O(n)**

* The pointer `j` only moves **forward**.
* It never moves backward.
* The first inner `while` scans consecutive `0`s.
* The second inner `while` scans consecutive `1`s.
* Every character is visited at most once by `j`.

So the total number of iterations across all loops is at most `n`.

**Time Complexity = O(n)**

---

### Space Complexity: **O(1)**

You only use a few integer variables:

* `i`
* `j`
* `ans`
* `count0`
* `count1`
* `n`

No extra array, list, stack, or hash map is used.

**Space Complexity = O(1)**

---

**Final Answer:**

* **Time Complexity:** **O(n)**
* **Space Complexity:** **O(1)**


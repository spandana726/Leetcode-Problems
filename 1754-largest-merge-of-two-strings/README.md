<h2><a href="https://leetcode.com/problems/largest-merge-of-two-strings">1880. Largest Merge Of Two Strings</a></h2><h3>Medium</h3><hr><p>You are given two strings <code>word1</code> and <code>word2</code>. You want to construct a string <code>merge</code> in the following way: while either <code>word1</code> or <code>word2</code> are non-empty, choose <strong>one</strong> of the following options:</p>

<ul>
	<li>If <code>word1</code> is non-empty, append the <strong>first</strong> character in <code>word1</code> to <code>merge</code> and delete it from <code>word1</code>.

	<ul>
		<li>For example, if <code>word1 = &quot;abc&quot; </code>and <code>merge = &quot;dv&quot;</code>, then after choosing this operation, <code>word1 = &quot;bc&quot;</code> and <code>merge = &quot;dva&quot;</code>.</li>
	</ul>
	</li>
	<li>If <code>word2</code> is non-empty, append the <strong>first</strong> character in <code>word2</code> to <code>merge</code> and delete it from <code>word2</code>.
	<ul>
		<li>For example, if <code>word2 = &quot;abc&quot; </code>and <code>merge = &quot;&quot;</code>, then after choosing this operation, <code>word2 = &quot;bc&quot;</code> and <code>merge = &quot;a&quot;</code>.</li>
	</ul>
	</li>
</ul>

<p>Return <em>the lexicographically <strong>largest</strong> </em><code>merge</code><em> you can construct</em>.</p>

<p>A string <code>a</code> is lexicographically larger than a string <code>b</code> (of the same length) if in the first position where <code>a</code> and <code>b</code> differ, <code>a</code> has a character strictly larger than the corresponding character in <code>b</code>. For example, <code>&quot;abcd&quot;</code> is lexicographically larger than <code>&quot;abcc&quot;</code> because the first position they differ is at the fourth character, and <code>d</code> is greater than <code>c</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;cabaa&quot;, word2 = &quot;bcaaa&quot;
<strong>Output:</strong> &quot;cbcabaaaaa&quot;
<strong>Explanation:</strong> One way to get the lexicographically largest merge is:
- Take from word1: merge = &quot;c&quot;, word1 = &quot;abaa&quot;, word2 = &quot;bcaaa&quot;
- Take from word2: merge = &quot;cb&quot;, word1 = &quot;abaa&quot;, word2 = &quot;caaa&quot;
- Take from word2: merge = &quot;cbc&quot;, word1 = &quot;abaa&quot;, word2 = &quot;aaa&quot;
- Take from word1: merge = &quot;cbca&quot;, word1 = &quot;baa&quot;, word2 = &quot;aaa&quot;
- Take from word1: merge = &quot;cbcab&quot;, word1 = &quot;aa&quot;, word2 = &quot;aaa&quot;
- Append the remaining 5 a&#39;s from word1 and word2 at the end of merge.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;abcabc&quot;, word2 = &quot;abdcaba&quot;
<strong>Output:</strong> &quot;abdcabcabcaba&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 3000</code></li>
	<li><code>word1</code> and <code>word2</code> consist only of lowercase English letters.</li>
</ul>
Let:

* (m = \text{len(word1)})
* (n = \text{len(word2)})

### Time Complexity

The `while` loop runs at most:

```text
m + n
```

iterations because in each iteration either `i` or `j` increases.

However, when characters are equal, you do:

```python
word1[i:] > word2[j:]
```

Creating and comparing these slices is **not O(1)**.

* `word1[i:]` creates a new substring.
* `word2[j:]` creates another new substring.
* Comparing them may scan many characters.

In the worst case (for example, when the strings contain many equal prefixes like `"aaaaaaaa..."`), each comparison can take **O(m + n)**.

Since this can happen in **O(m + n)** iterations:

[
\boxed{O((m+n)^2)}
]

If both strings have length (N):

[
\boxed{O(N^2)}
]

---

### Space Complexity

Ignoring the output string, each slice

```python
word1[i:]
word2[j:]
```

creates new strings.

The largest slices together can occupy:

[
\boxed{O(m+n)}
]

extra space during an iteration.

Also, the output strings `s` and `k` together store all characters:

[
\boxed{O(m+n)}
]

So:

* **Auxiliary space (excluding the output):** (\boxed{O(m+n)})
* **Including the output:** (\boxed{O(m+n)})

---

### Final Answer

* **Time Complexity:** (\boxed{O((m+n)^2)}) (or **O(N²)** when both strings have length (N))
* **Auxiliary Space:** (\boxed{O(m+n)})
* **Space including the output:** (\boxed{O(m+n)})

Your solution is correct, but the repeated slicing (`word1[i:]` and `word2[j:]`) is what makes it quadratic. An optimized solution avoids creating slices and achieves better performance.

<h2><a href="https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends">1850. Minimum Length of String After Deleting Similar Ends</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code> consisting only of characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>. You are asked to apply the following algorithm on the string any number of times:</p>

<ol>
	<li>Pick a <strong>non-empty</strong> prefix from the string <code>s</code> where all the characters in the prefix are equal.</li>
	<li>Pick a <strong>non-empty</strong> suffix from the string <code>s</code> where all the characters in this suffix are equal.</li>
	<li>The prefix and the suffix should not intersect at any index.</li>
	<li>The characters from the prefix and suffix must be the same.</li>
	<li>Delete both the prefix and the suffix.</li>
</ol>

<p>Return <em>the <strong>minimum length</strong> of </em><code>s</code> <em>after performing the above operation any number of times (possibly zero times)</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ca&quot;
<strong>Output:</strong> 2
<strong>Explanation: </strong>You can&#39;t remove any characters, so the string stays as is.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cabaabac&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> An optimal sequence of operations is:
- Take prefix = &quot;c&quot; and suffix = &quot;c&quot; and remove them, s = &quot;abaaba&quot;.
- Take prefix = &quot;a&quot; and suffix = &quot;a&quot; and remove them, s = &quot;baab&quot;.
- Take prefix = &quot;b&quot; and suffix = &quot;b&quot; and remove them, s = &quot;aa&quot;.
- Take prefix = &quot;a&quot; and suffix = &quot;a&quot; and remove them, s = &quot;&quot;.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabccabba&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> An optimal sequence of operations is:
- Take prefix = &quot;aa&quot; and suffix = &quot;a&quot; and remove them, s = &quot;bccabb&quot;.
- Take prefix = &quot;b&quot; and suffix = &quot;bb&quot; and remove them, s = &quot;cca&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> only consists of characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</li>
</ul>

That's the important part: **you do not return immediately when `i == j`**.

Take:

```text
s = "aaa"

0 1 2
a a a
```

Initially:

```text
i = 0
j = 2
```

The ends are equal, so:

```python
ch = s[i]   # 'a'
```

Now the left loop runs:

```python
while i <= j and s[i] == ch:
    i += 1
```

Trace it:

```text
i = 0, j = 2   → 0 <= 2 ✅ → i = 1
i = 1, j = 2   → 1 <= 2 ✅ → i = 2
i = 2, j = 2   → 2 <= 2 ✅ → i = 3
i = 3, j = 2   → 3 <= 2 ❌ stop
```

Notice what happened:

* When `i == j == 2`, the middle `'a'` was **also removed**, so `i` became `3`.

Now the second loop doesn't run because:

```python
i <= j
```

is

```text
3 <= 2  ❌
```

Finally:

```python
return j - i + 1
```

becomes

```text
2 - 3 + 1 = 0
```

which is correct because the entire string was removed.

---

### Your doubt was:

> "When `i = 2` and `j = 2`, won't `j - i + 1` be `1`?"

It **would** be `1` **if you stopped there**.

But you **don't stop** when `i == j`. Because the condition is `i <= j`, the loop executes **one more time**, removing that last middle character and making:

```text
i = 3
j = 2
```

Only **after the loop finishes** do you calculate:

```text
j - i + 1 = 0
```

That's exactly why the `=` in `i <= j` is necessary.

If you'd like, I can also trace `"aabccbaa"` step by step with the values of `i` and `j` at every iteration. That example makes the whole algorithm click for most people.
Time Complexity: O(n)
i only moves forward.
j only moves backward.
Neither pointer ever moves in the opposite direction.
Each character is visited at most once by i and at most once by j.

So the total work is proportional to the length of the string.

Time Complexity = O(n)

Space Complexity: O(1)

You only use a few variables:

i
j
ch

No extra arrays, lists, stacks, or hash maps are used.

Space Complexity = O(1)

Final Answer
Time Complexity: O(n)
Space Complexity: O(1)

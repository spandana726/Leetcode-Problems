<h2><a href="https://leetcode.com/problems/move-pieces-to-obtain-a-string">2414. Move Pieces to Obtain a String</a></h2><h3>Medium</h3><hr><p>You are given two strings <code>start</code> and <code>target</code>, both of length <code>n</code>. Each string consists <strong>only</strong> of the characters <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, and <code>&#39;_&#39;</code> where:</p>

<ul>
	<li>The characters <code>&#39;L&#39;</code> and <code>&#39;R&#39;</code> represent pieces, where a piece <code>&#39;L&#39;</code> can move to the <strong>left</strong> only if there is a <strong>blank</strong> space directly to its left, and a piece <code>&#39;R&#39;</code> can move to the <strong>right</strong> only if there is a <strong>blank</strong> space directly to its right.</li>
	<li>The character <code>&#39;_&#39;</code> represents a blank space that can be occupied by <strong>any</strong> of the <code>&#39;L&#39;</code> or <code>&#39;R&#39;</code> pieces.</li>
</ul>

<p>Return <code>true</code> <em>if it is possible to obtain the string</em> <code>target</code><em> by moving the pieces of the string </em><code>start</code><em> <strong>any</strong> number of times</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> start = &quot;_L__R__R_&quot;, target = &quot;L______RR&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to &quot;<strong>L</strong>___R__R_&quot;.
- Move the last piece one step to the right, start becomes equal to &quot;L___R___<strong>R</strong>&quot;.
- Move the second piece three steps to the right, start becomes equal to &quot;L______<strong>R</strong>R&quot;.
Since it is possible to get the string target from start, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> start = &quot;R_L_&quot;, target = &quot;__LR&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The &#39;R&#39; piece in the string start can move one step to the right to obtain &quot;_<strong>R</strong>L_&quot;.
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> start = &quot;_R&quot;, target = &quot;R_&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == start.length == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>start</code> and <code>target</code> consist of the characters <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, and <code>&#39;_&#39;</code>.</li>
</ul>
Cases that test each rule individually
✅ Same order after removing _
start  = "__L_R__R"
target = "L___R__R"

Expected: True

❌ Different order
start  = "__LR"
target = "__RL"

Expected: False

❌ L moves right
start  = "L___"
target = "__L_"

Expected: False

❌ R moves left
start  = "__R_"
target = "_R__"

Expected: False

✅ L moves left many steps
start  = "___L"
target = "L___"

Expected: True

✅ R moves right many steps
start  = "R___"
target = "___R"

Expected: True

❌ Remaining piece in start
start  = "__L"
target = "___"

Expected: False

❌ Remaining piece in target
start  = "___"
target = "__L"

Expected: False

The four most important hidden tests

These are the ones that most incorrect solutions fail:

1.
start  = "_L"
target = "LR"
Expected = False

2.
start  = "__"
target = "_L"
Expected = False

3.
start  = "__L"
target = "___"
Expected = False

4.
start  = "____"
target = "____"
Expected = True

If your code passes these four, plus the official examples, you're covering the main edge cases:

skipping multiple underscores,
illegal L movement,
illegal R movement,
changed piece order,
and unmatched remaining pieces.

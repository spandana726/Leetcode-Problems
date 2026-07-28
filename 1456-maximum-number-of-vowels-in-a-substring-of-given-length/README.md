<h2><a href="https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length">1567. Maximum Number of Vowels in a Substring of Given Length</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the maximum number of vowel letters in any substring of </em><code>s</code><em> with length </em><code>k</code>.</p>

<p><strong>Vowel letters</strong> in English are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abciiidef&quot;, k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The substring &quot;iii&quot; contains 3 vowel letters.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aeiou&quot;, k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Any substring of length 2 contains 2 vowels.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, k = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> &quot;lee&quot;, &quot;eet&quot; and &quot;ode&quot; contain 2 vowels.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>
##Time Complexity
The outer loop:
for j in range(n):

runs n times.

Inside the loop:
Dictionary insertion/deletion: O(1) on average.
Window adjustment: O(1).
But this part:
for ch in dic.keys():

iterates over all distinct characters in the current window.

In the worst case, the window can contain k distinct characters, so this loop takes O(k).

Therefore:

Outer loop: O(n)
Inner loop: O(k)

Overall Time Complexity:

O(n×k)
	​

Space Complexity

You are storing character frequencies in dic.

At any time, the dictionary contains only characters in the current window.
In the worst case, all k characters in the window are distinct.

So the dictionary size is at most k.

Additionally:

a = set('aeiou') stores only 5 characters, which is O(1).

Overall Space Complexity:

O(k)
	​

Summary
Time Complexity: O(n × k)
Space Complexity: O(k)

Note: If the input is guaranteed to contain only lowercase English letters (26 characters), then the loop over dic.keys() is bounded by 26, making the practical time O(n). However, in interview analysis, since the dictionary size depends on the window size, it is generally analyzed as O(n × k).

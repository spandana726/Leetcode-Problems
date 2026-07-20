<h2><a href="https://leetcode.com/problems/find-all-anagrams-in-a-string">438. Find All Anagrams in a String</a></h2><h3>Medium</h3><hr><p>Given two strings <code>s</code> and <code>p</code>, return an array of all the start indices of <code>p</code>&#39;s <span data-keyword="anagram">anagrams</span> in <code>s</code>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbaebabacd&quot;, p = &quot;abc&quot;
<strong>Output:</strong> [0,6]
<strong>Explanation:</strong>
The substring with start index = 0 is &quot;cba&quot;, which is an anagram of &quot;abc&quot;.
The substring with start index = 6 is &quot;bac&quot;, which is an anagram of &quot;abc&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abab&quot;, p = &quot;ab&quot;
<strong>Output:</strong> [0,1,2]
<strong>Explanation:</strong>
The substring with start index = 0 is &quot;ab&quot;, which is an anagram of &quot;ab&quot;.
The substring with start index = 1 is &quot;ba&quot;, which is an anagram of &quot;ab&quot;.
The substring with start index = 2 is &quot;ab&quot;, which is an anagram of &quot;ab&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, p.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>p</code> consist of lowercase English letters.</li>
</ul>


**Time Complexity**
Building the target map d:
Runs m times.
O(m)
Sliding window:
r traverses s once → O(n)
l only moves forward and overall moves at most n times.
Dictionary insert, delete, and lookup are O(1) on average.
Comparing mp == d:
Python compares the dictionaries key by key.
If the alphabet is fixed (e.g., lowercase English letters), there can be at most 26 keys, so this comparison is O(26) = O(1).
More generally, if the character set is unrestricted, it is O(k), where k is the number of distinct characters in the window.
Overall Time Complexity
For this LeetCode problem (lowercase English letters):
O(m + n) ≈ O(n)
General case (arbitrary characters):
O(m + n × k), where k is the number of distinct characters.
Space Complexity

You use:

d → frequency map of p
mp → frequency map of the current window
ls → stores the answer
d: O(k)
mp: O(k)
ls: O(a), where a is the number of starting indices found (this is the output space).

If interviewers ask for auxiliary space (excluding the output list):

Auxiliary Space: O(k)

For this problem, k ≤ 26, so it's effectively:

Auxiliary Space: O(1)
Interview answer
Time Complexity: O(n + m) (or simply O(n) since m ≤ n), because we build one frequency map for p and scan s once.
Auxiliary Space: O(1) because the frequency maps contain at most 26 lowercase English letters.
Output Space: O(a), where a is the number of anagram starting indices returned.

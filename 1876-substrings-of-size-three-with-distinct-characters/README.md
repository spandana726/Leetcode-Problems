<h2><a href="https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters">1987. Substrings of Size Three with Distinct Characters</a></h2><h3>Easy</h3><hr><p>A string is <strong>good</strong> if there are no repeated characters.</p>

<p>Given a string <code>s</code>​​​​​, return <em>the number of <strong>good substrings</strong> of length <strong>three </strong>in </em><code>s</code>​​​​​​.</p>

<p>Note that if there are multiple occurrences of the same substring, every occurrence should be counted.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;xyzzaz&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are 4 substrings of size 3: &quot;xyz&quot;, &quot;yzz&quot;, &quot;zza&quot;, and &quot;zaz&quot;. 
The only good substring of length 3 is &quot;xyz&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aababcabc&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 7 substrings of size 3: &quot;aab&quot;, &quot;aba&quot;, &quot;bab&quot;, &quot;abc&quot;, &quot;bca&quot;, &quot;cab&quot;, and &quot;abc&quot;.
The good substrings are &quot;abc&quot;, &quot;bca&quot;, &quot;cab&quot;, and &quot;abc&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code>​​​​​​ consists of lowercase English letters.</li>
</ul>










Time Complexity: O(n)

Here's why:

The for loop runs n times.
Each iteration performs:
One dictionary insertion/update → O(1) average.
At most one dictionary removal → O(1) average.
len(mp) → O(1).
The left pointer (l) only moves forward and can move at most n times in total.

So the total work is proportional to n.

Time Complexity = O(n)

Space Complexity: O(1)

The window size is fixed at 3.

That means the dictionary can never store more than 3 distinct characters.

For example:

Window = "abc"

mp = {
'a':1,
'b':1,
'c':1
}

Maximum size of mp = 3, which is a constant.

Space Complexity = O(1)

Interview explanation

You can say:

Time Complexity: O(n), because both pointers (l and r) move only forward, and each character is added to and removed from the hash map at most once.

Space Complexity: O(1), because the sliding window size is fixed at 3, so the hash map stores at most 3 characters.

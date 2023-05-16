# 수열 정렬

### 문제
P[0], P[1], ...., P[N-1]은 0부터 N-1까지(포함)의 수를 한 번씩 포함하고 있는 수열이다. 수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다. 적용하는 방법은 B[P[i]] = A[i]이다.

배열 A가 주어졌을 때, 수열 P를 적용한 결과가 비내림차순이 되는 수열을 찾는 프로그램을 작성하시오. 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다. 만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.
<br></br>

### 입력
첫째 줄에 배열 A의 크기 N이 주어진다. 둘째 줄에는 배열 A의 원소가 0번부터 차례대로 주어진다. N은 50보다 작거나 같은 자연수이고, 배열의 원소는 1,000보다 작거나 같은 자연수이다.
<br></br>

### 출력
첫째 줄에 비내림차순으로 만드는 수열 P를 출력한다.
<br></br>
#

### 예제 입력 1
<pre class="sampledata" id="sample-output-1" style="background-color: #f7f7f9; border-radius: 5px; border: 1px solid rgb(225, 225, 232); box-sizing: border-box; color: #333333; font-family: Menlo, Monaco, &quot;Source Code Pro&quot;, consolas, monospace; font-size: 18px; line-height: 1.42857; margin-bottom: 10px; margin-top: 0px; overflow-wrap: normal; overflow: scroll auto; padding: 8px; word-break: normal;">3
2 3 1</pre>

### 예제 출력 1
<pre class="sampledata" id="sample-output-1" style="background-color: #f7f7f9; border-radius: 5px; border: 1px solid rgb(225, 225, 232); box-sizing: border-box; color: #333333; font-family: Menlo, Monaco, &quot;Source Code Pro&quot;, consolas, monospace; font-size: 18px; line-height: 1.42857; margin-bottom: 10px; margin-top: 0px; overflow-wrap: normal; overflow: scroll auto; padding: 8px; word-break: normal;">1 2 0</pre>
<br></br>

### 예제 입력 2
<pre class="sampledata" id="sample-output-1" style="background-color: #f7f7f9; border-radius: 5px; border: 1px solid rgb(225, 225, 232); box-sizing: border-box; color: #333333; font-family: Menlo, Monaco, &quot;Source Code Pro&quot;, consolas, monospace; font-size: 18px; line-height: 1.42857; margin-bottom: 10px; margin-top: 0px; overflow-wrap: normal; overflow: scroll auto; padding: 8px; word-break: normal;">4
2 1 3 1</pre>

### 예제 출력 2
<pre class="sampledata" id="sample-output-1" style="background-color: #f7f7f9; border-radius: 5px; border: 1px solid rgb(225, 225, 232); box-sizing: border-box; color: #333333; font-family: Menlo, Monaco, &quot;Source Code Pro&quot;, consolas, monospace; font-size: 18px; line-height: 1.42857; margin-bottom: 10px; margin-top: 0px; overflow-wrap: normal; overflow: scroll auto; padding: 8px; word-break: normal;">2 0 3 1</pre>
<br></br>

### 예제 입력 3
<pre class="sampledata" id="sample-output-1" style="background-color: #f7f7f9; border-radius: 5px; border: 1px solid rgb(225, 225, 232); box-sizing: border-box; color: #333333; font-family: Menlo, Monaco, &quot;Source Code Pro&quot;, consolas, monospace; font-size: 18px; line-height: 1.42857; margin-bottom: 10px; margin-top: 0px; overflow-wrap: normal; overflow: scroll auto; padding: 8px; word-break: normal;">8
4 1 6 1 3 6 1 4</pre>

### 예제 출력 3
<pre class="sampledata" id="sample-output-1" style="background-color: #f7f7f9; border-radius: 5px; border: 1px solid rgb(225, 225, 232); box-sizing: border-box; color: #333333; font-family: Menlo, Monaco, &quot;Source Code Pro&quot;, consolas, monospace; font-size: 18px; line-height: 1.42857; margin-bottom: 10px; margin-top: 0px; overflow-wrap: normal; overflow: scroll auto; padding: 8px; word-break: normal;">4 0 6 1 3 7 2 5</pre>
<br></br>

#### 링크
[1015번: 수열 정렬](https://www.acmicpc.net/problem/1015)

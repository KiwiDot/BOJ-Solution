# 터렛

### 문제
조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.
<div class="separator" style="clear: both; text-align: center;"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEiksjfDZkZa7ymMDjJRIV7coRdjs49Qq98Egm08JUs8Xcs7fSU1lp0JGIBGXCVSIFwIp6stNj87x9VaCfosb3MAkpjTz92O5TdSXbSsBFIraEWsHCZUy_5L4Hm3B3UP5CbhTXPncBhPeIrDBT3CNoAtDSfWayszqEUYS1T7Zprx_QFhtjIcwhevbrMPjw" style="margin-left: auto; margin-right: auto;"><img alt="" data-original-height="271" data-original-width="274" height="166" src="https://blogger.googleusercontent.com/img/a/AVvXsEiksjfDZkZa7ymMDjJRIV7coRdjs49Qq98Egm08JUs8Xcs7fSU1lp0JGIBGXCVSIFwIp6stNj87x9VaCfosb3MAkpjTz92O5TdSXbSsBFIraEWsHCZUy_5L4Hm3B3UP5CbhTXPncBhPeIrDBT3CNoAtDSfWayszqEUYS1T7Zprx_QFhtjIcwhevbrMPjw=w168-h166" width="168" /></a></div><br />
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
<br></br>

### 입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 음이 아닌 정수이다.
<br></br>

### 출력
각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
<br></br>
#
### 예제 입력 1
<pre class="sampledata" id="sample-input-1" style="background-color: #f7f7f9; border-radius: 5px; border: 1px solid rgb(225, 225, 232); box-sizing: border-box; color: #333333; font-family: Menlo, Monaco, &quot;Source Code Pro&quot;, consolas, monospace; font-size: 18px; line-height: 1.42857; margin-bottom: 10px; margin-top: 0px; overflow-wrap: normal; overflow: scroll auto; padding: 8px; word-break: normal;">3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5</pre>

### 예제 출력 1
<pre class="sampledata" id="sample-output-1" style="background-color: #f7f7f9; border-radius: 5px; border: 1px solid rgb(225, 225, 232); box-sizing: border-box; color: #333333; font-family: Menlo, Monaco, &quot;Source Code Pro&quot;, consolas, monospace; font-size: 18px; line-height: 1.42857; margin-bottom: 10px; margin-top: 0px; overflow-wrap: normal; overflow: scroll auto; padding: 8px; word-break: normal;">2
1
0</pre>
<br></br>

#### 링크
[1002번: 터렛](https://www.acmicpc.net/problem/1002)

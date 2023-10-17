<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Rishitha Vanapally (rv437)</td></tr>
<tr><td> <em>Generated: </em> 10/16/2023 7:52:05 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/rv437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T20.36.34q1%20add%20.png.webp?alt=media&token=5d7cc2dd-33a8-4fbf-a357-2830c5a6661b"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function is used to perform addition function in MyCalc.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T20.44.00q1%20sub.png.webp?alt=media&token=b3513329-79e7-49ff-93fe-efc014b14d71"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function is used to perform subtraction function in MyCalc.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T20.45.07q1%20mul.png.webp?alt=media&token=1e40c15d-bfaf-4e6e-aeb9-98b2f8ca4cbb"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function is used to perform multiplication function in MyCalc.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T20.46.55q1%20div.png.webp?alt=media&token=a62d4625-3327-45ac-8878-ba8f47f2fbc0"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function is used to perform the division function and it also handles<br>errors for dividing by zero in MyCalc.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T21.10.03num%20add%20num.png.webp?alt=media&token=c442098c-df82-481b-9442-910a37a78b50"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this test case we are performing the number add number function<br>where two numbers are added together.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T21.12.22ans%20add%20num.png.webp?alt=media&token=3f943300-1c8f-427c-8c64-d69f6f3c993b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this test case we are performing the ans add number function<br>where two numbers are added together by taking one of the arguments (number)<br>as the previous answer according to that test case.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T22.46.59num%20sub%20num.png.webp?alt=media&token=7413a223-b41b-4c5c-85ed-ec8a876b0840"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this test case we are performing the number sub number function<br>where two numbers are subtracted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T22.49.03ans%20sub%20num.png.webp?alt=media&token=9456411b-ff66-484f-83d2-c20e89f6d122"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this test case we are performing the ans-sub-number function where two<br>numbers are subtracted by taking one of the arguments (number) as the previous<br>answer according to that test case.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T22.50.52num%20mul%20num.png.webp?alt=media&token=37e632de-0bc7-45c9-9f06-56f94ecad32d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this test case we are performing the number mult number function<br>where two numbers are multiplied together.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T22.52.14ans%20mul%20num.png.webp?alt=media&token=72c85424-9bf2-408b-b78a-0a2c2c11abe2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this test case we are performing the ans mult number function<br>where two numbers are multiplied together by taking one of the arguments (number)<br>as the previous answer according to that test case.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T22.53.41num%20div%20num.png.webp?alt=media&token=64bdcb5f-f713-4087-b235-77f6eac1bbdc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this test case we are performing the number div number function<br>where two numbers are divided.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-16T22.54.38ans%20div%20num.png.webp?alt=media&token=b9238d85-1cde-4c1f-8fcf-0ed614b8c3e2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this test case we are performing the ans div number function<br>where two numbers are divided, by taking one of the arguments (number) as<br>the previous answer according to that test case.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>In this module, I have learned about&nbsp;&quot;parametrized fixtures&quot; which refer to configuring and<br>using fixtures with varying parameters. Fixtures are reusable pieces of code that help<br>set up the environment for tests, ensuring consistent conditions for each test run.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>Here we have used different test cases for all the respective functions which<br>import the working function from MyCalc.py and then run those test cases for<br>add, sub, mult, and div and their test cases with using the previous<br>answer. Generally, fixtures and parameterized tests are essential concepts used to enhance code<br>reusability and maintainability in the testing process. Fixtures help in reducing redundant code<br>by creating a common setup for multiple tests. When the test function runs,<br>my_calc is automatically instantiated by pytest due to the defined fixture, and this<br>instance is used within the test function for testing the functionality of the<br>MyCalc class.<div>By using fixtures, you ensure that each test has a clean and<br>consistent instance of MyCalc to work with, promoting maintainability and code reuse.</div><div><div><br></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/12">https://github.com/rishithareddy19/rv437-IS601-007/pull/12</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/rv437" target="_blank">Grading</a></td></tr></table>
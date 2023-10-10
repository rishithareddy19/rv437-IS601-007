<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Rishitha Vanapally (rv437)</td></tr>
<tr><td> <em>Generated: </em> 10/9/2023 11:08:22 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/rv437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-09T23.29.21q1%20sub%20task%201.png.webp?alt=media&token=e3da94d9-3b14-4875-855a-d6158b975921"/></td></tr>
<tr><td> <em>Caption:</em> <p>We are using this function to add different tasks in the tracker app<br>and if some field is missing we will get an error saying that<br>particular field is missing.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-09T23.28.53qq1%20subtask%202.png.webp?alt=media&token=c1d1c2f4-c232-4737-af2c-f7e1847adb91"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this screenshot, the output is shown when a task is added successfully<br>and an error message also pops up when we do not give the<br>value for one of the required fields.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>As mentioned in the checklist the code mentions all the requirements mentioned in<br>the above checklist.<div><span style="font-size: 13px;">1)update lastActivity with the current datetime value</span></div><div><span style="font-size: 13px;">2)</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;set the name, description, and due date (all must be provided)</span></div><div><span style="font-size:<br>13px;">3)</span><span style="font-size: 13px;">due date must match one of the formats mentioned in str_to_datetime()</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;4)</span><span style="font-size: 13px;">add the new task to the tasks list</span></div><div><span style="font-size: 13px;">5)</span>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;output a message confirming the new task was added or if the<br>addition was rejected due to missing data</span></div><div><span style="font-size: 13px;">6)</span><span style="font-size: 13px;">make sure save()<br>is still called last in this function</span></div><div><span style="font-size: 13px;">7)</span><span style="font-size: 13px;">includes your ucid<br>and date as a comment&nbsp;</span></div><div><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;">We are using this function<br>to add different tasks in the tracker app and if some field is<br>missing we will get an error saying that particular field is missing.</span><br></div><div><span style="font-size:<br>13px;"><br></span><div>the output is shown when a task is added successfully and an error<br>message also pops up when we do not give the value for one<br>of the required field.<br><div><br></div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-09T23.46.57q2%20subtask%201.png.webp?alt=media&token=2b7cbc35-e7ec-4837-a3a3-07376acc2900"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this code we have created a function where it helps in updating<br>and it mentions the previous the details even before we enter the new<br>ones and we will get a message if no changes are made to<br>that particular task . <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p>As mentioned in the checklist the code satisfies everything condition and it even<br>gives a message when a task which is out of the list is<br>selected , and it shows the following :<div><br></div><div><span style="font-size: 13px;">1)get the task by<br>index</span><br></div><div><span style="font-size: 13px;">2)</span><span style="font-size: 13px;">consider index out of bounds scenarios and include appropriate<br>message(s) for invalid index</span></div><div><span style="font-size: 13px;">3)show the existing value of each property where<br>the TODOs are marked in the text of the inputs (replace the TODO<br>related text with the found task&#39;s data)</span><br></div><div><span style="font-size: 13px;">4)I have included my ucid<br>and date accordingly .</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-09T23.53.42q3%20sub%20task%201%20and%202.png.webp?alt=media&token=98cbc6dc-235e-495e-a757-6a2c5d6e0e3e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in this function it helps update the tasks accordingly with the help<br>of process_update function and then shows them in the lists_tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-09T23.57.24q3%20sub%20task%201%20and%202.png.webp?alt=media&token=729240af-a23a-49ee-acd6-177cd7fe89c2"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this image we can see that the task was updated successfully and<br>when we do not update anything their is a particular message which says<br>no changes provided , task not updated which lets the user know that<br>there we no changes to be made.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p>Here we have written the code where every condition is satisfied and&nbsp;we can<br>see that the task was updated successfully when we do not update anything<br>their is a particular message that says no changes provided, a task not<br>updated which lets the user know that there we no changes to be<br>made, and when we try to update a task which does not exist<br>then an invalid text index message pops that is an invalid bound exception<br>where it lets us know that it does not exist.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.02.36q4%20subtask1%20and%202.png.webp?alt=media&token=a3409cc9-55d1-4f8c-b5dc-16476cb8f7ec"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here using this function we can mark a task as its done and<br>then it gets updated automatically in the lists_tasks .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.05.35q4%20subtask1%20and%202.png.webp?alt=media&token=62a978f3-9e3e-4986-8002-f6e9ec1617ad"/></td></tr>
<tr><td> <em>Caption:</em> <p>As mentioned previously here we make sure the task is changed to done<br>and when we do that the particular message pops up accordingly where its<br>successful and if its already done it says the task is already completed,and<br>if its out of the ists the it says its invalid.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p>As mentioned earlier everything is mentioned in the code and it satisfies all<br>the requirements and I even mentioned my ucid and the date when I<br>wrote the code.<div>Here using this function we can mark a task as it&#39;s<br>done and then it gets updated automatically in the lists_tasks .</div><div><div>As mentioned previously<br>here we make sure the task is changed to done and when we<br>do that the particular message pops up accordingly where it&#39;s successful if its<br>already done it says the task is already completed, and if it&#39;s out<br>of the ists it says it&#39;s invalid.<br></div></div><div>and here when this is done it<br>gets updated in the lists_tasks where it puts a cross mark in the<br>start of the task that is in the square brackets when we view<br>the list again.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.11.55q5%20subtask%201%20and%202.png.webp?alt=media&token=55303b23-b13c-41d3-8bb9-bfc5dcf18491"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this image there’s the required code which helps to view the particular<br>task completely and it even shows the status of the task like for<br>example if the task is completed then it says its completed orelse a<br>&#39;-&#39; symbol is printed. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.15.52q5%20subtask%201%20and%202.png.webp?alt=media&token=d071ae8a-939f-4bdc-8cb3-c971cd29f3b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this image we can see the output which helps in viewing a<br>particular task where we can see the complete info of that task and<br>if we select a task wich is not present in the app it<br>prints a message like invalid task index .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.23.35q5%20subtas%203.png.webp?alt=media&token=4b2594e3-6428-45e1-a2c5-1b2dcf6dc71c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here it shows the number of tasks present in the tracker app and<br>when we choose the list option from the menu it prints all the<br>tasks which are present int app .<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.26.20Q6%20subtask1%20and%202.png.webp?alt=media&token=e12e0238-8b75-44aa-bea1-3416a23cf148"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here we can use the above code to delete a particular task .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.27.36Q6%20subtask1%20and%202.png.webp?alt=media&token=102890e0-8ba6-4db5-8587-74f9be99ac26"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here we can delete a task and then a meesage pops up if<br>the process is successful and if not then it says that its invalid.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p>As mentioned earlier&nbsp;<div>Here we can use the above code to delete a particular<br>task .<br></div><div>Here we can delete a task and then a meesage pops up<br>if the process is successful and if not then it says that its<br>invalid.<br></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.30.18q7%20subtask%201%20and%202.png.webp?alt=media&token=8b37dba7-9555-4ec5-955e-731514345f9a"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this part the code is used to get the incompleted lists of<br>tasks from the tracker app where it mentions the task and its due<br>time accordingly .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.33.46q7%20subtask%201%20and%202.png.webp?alt=media&token=2901ab83-26d9-4590-b424-63dc3252b8bd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here as its mentioned in the code we print the incomplete tasks and<br>we get the output with the number of incomplete tasks and their due<br>time which is given accordingly and if everything is marked done or completed<br>then it says no tasks are pending.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>Everything is clearly in the code and it satisfies every condition&nbsp;<div>In this part,<br>the code is used to get the incompleted lists of tasks from the<br>tracker app where it mentions the task and its due time accordingly .<br></div><div>Here<br>as it&#39;s mentioned in the code we print the incomplete tasks and we<br>get the output with the number of incomplete tasks and their due time<br>which is given accordingly and if everything is marked done or completed then<br>it says no tasks are pending.<br></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.36.48q8%20subtask1%20and%202.png.webp?alt=media&token=c9e36bc9-b11b-42c0-b8b4-c1e46135726d"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this segment, we have written the code to print the overdue tasks<br>which means it tells which tasks are past the time that is which<br>are out of line , that is when the given due date is<br>older than the present time.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.38.48q8%20subtask1%20and%202.png.webp?alt=media&token=eeea1697-507d-4e5e-abe2-4aea34ae21be"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here we have executed the above code and got the output where it<br>shows the overdue tasks with their names and their due time accordingly just<br>like how its in incomplete tasks and when there are no tasks overdue<br>that is when everything is up to date then it says no tasks<br>are overdue.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p>As mentioned earlier everything is according to the checklist :<div>In this segment, we<br>have written the code to print the overdue tasks which means it tells<br>which tasks are past the time that is which are out of line,<br>that is when the given due date is older than the present time.<br></div><div>Here<br>we have executed the above code and got the output where it shows<br>the overdue tasks with their names and their due time accordingly just like<br>how its in incomplete tasks and when there are no tasks overdue that<br>is when everything is up to date then it says no tasks are<br>overdue.<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.43.44q9%20subtask1%20and%202.png.webp?alt=media&token=8713911b-f139-4b4b-a028-7b453b152c70"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here we have written a code to get the remaining time for a<br>particular task that tells us the leftover time for that particular task and<br>then it also shows how long the task was overdue and even gives<br>an invalid bound message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T00.47.32q9%20subtask1%20and%202.png.webp?alt=media&token=1c57b558-1856-42fc-bad9-221afedcb62e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here as mentioned in the code everything gets executed and the output <br>is generated when we select the remaining option from the menu bar and<br>then we get the output as time remaining with the exact time in<br>days hours minutes and seconds for the task wich we selected and then<br>if that particular task is overdue it prints the time in the same<br>format as above and tells the task is overdue by so an so<br>time .and an invalid message also is available if we select a task<br>wich does not exist.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p>Everything is according to the checklist and then&nbsp;<div>Here we have written a code<br>to get the remaining time for a particular task that tells us the<br>leftover time for that particular task and then it also shows how long<br>the task was overdue and even gives an invalid bound message.</div><div><br><div>Here as mentioned<br>in the code everything gets executed and the output&nbsp; is generated when we<br>select the remaining option from the menu bar and then we get the<br>output as time remaining with the exact time in days hours minutes and<br>seconds for the task wich we selected and then if that particular task<br>is overdue it prints the time in the same format as above and<br>tells the task is overdue by so an so time .and an invalid<br>message also is available if we select a task wich does not exist.<br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T02.10.28q10%20subtask%201.png.webp?alt=media&token=dcd8a3f9-d786-433e-b71b-bc12484080ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here in this image i have tried to execute all the options present<br>in the menu bar to the tasks added previously and got the outputs<br>accordingly .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-10-10T01.41.09json.png.webp?alt=media&token=c388f099-3559-49c1-a22b-0ea2785e60b7"/></td></tr>
<tr><td> <em>Caption:</em> <p>In this part we get all tasks which were added their corresponding info<br>in the .json file.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>Because of the instructions given by the prof after following those step by<br>step&nbsp; there were no issues .<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/7">https://github.com/rishithareddy19/rv437-IS601-007/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/rv437" target="_blank">Grading</a></td></tr></table>
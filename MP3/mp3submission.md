<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Rishitha Vanapally (rv437)</td></tr>
<tr><td> <em>Generated: </em> 12/2/2023 1:18:54 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/rv437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.13.10d1%20and%20d2.png.webp?alt=media&token=97010b6d-2903-4a39-80ba-80f34d1bc256"/></td></tr>
<tr><td> <em>Caption:</em> <p>this page shows the home page where i included my ucid and my<br>name .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.14.35index%20code.png.webp?alt=media&token=c32fb9f8-16c0-4808-8995-5ffa74b538f3"/></td></tr>
<tr><td> <em>Caption:</em> <p>here the above image includes the code of index html.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.15.29d1%20and%20d2.png.webp?alt=media&token=24683d44-bfee-4633-938c-39f601126ec2"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the nav bar for this page.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.19.15Screen%20Shot%202023-11-30%20at%207.18.23%20PM.png.webp?alt=media&token=0a288693-4929-408d-9319-644949c2dbfe"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains the nav code.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.22.08Screen%20Shot%202023-11-30%20at%207.22.02%20PM.png.webp?alt=media&token=43c90dea-374f-4793-ab49-035c1df4dd87"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains the admin code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.22.49Screen%20Shot%202023-11-30%20at%207.22.45%20PM.png.webp?alt=media&token=05edda0b-8e3c-46c5-83c1-74beabd92a67"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains the admin code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.23.03Screen%20Shot%202023-11-30%20at%207.23.00%20PM.png.webp?alt=media&token=d75f4d89-ecff-42df-ad61-e6b097df9418"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains the admin c<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.26.29Screen%20Shot%202023-11-30%20at%207.24.38%20PM.png.webp?alt=media&token=95097bd3-e9b6-4420-af0c-012a093925af"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the create page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T00.55.43Screen%20Shot%202023-11-30%20at%207.55.31%20PM.png.webp?alt=media&token=71adc948-3572-436f-8cad-6dc6d3d96152"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the edit page.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.27.36Screen%20Shot%202023-11-30%20at%207.57.25%20PM.png.webp?alt=media&token=6ee99d62-c3af-443d-a8dc-ff529cfffbb8"/></td></tr>
<tr><td> <em>Caption:</em> <p>here it shows the fields required which helps in create and edit view<br>of donations.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.30.44Screen%20Shot%202023-11-30%20at%207.57.49%20PM.png.webp?alt=media&token=5b6e4757-b8d6-443b-bed7-508af87cd87e"/></td></tr>
<tr><td> <em>Caption:</em> <p>here it shows the fields required which helps in create and edit view<br>of donations.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.31.18Screen%20Shot%202023-11-30%20at%207.58.03%20PM.png.webp?alt=media&token=02f25225-852b-49ba-89e8-c236c1ffac83"/></td></tr>
<tr><td> <em>Caption:</em> <p>here it shows the fields required which helps in create and edit view<br>of donations.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.35.00don%20search.png.webp?alt=media&token=e3cfd508-c5bf-43e4-a68c-8956c850bfed"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the search page without any filters applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.36.50search%20with%20filter.png.webp?alt=media&token=4b3aa83c-94a5-4adb-8081-41ba54880c9c"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the search page when an organization with a certain<br>company is applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.51.16Screen%20Shot%202023-12-01%20at%2012.50.20%20PM.png.webp?alt=media&token=5348bb8e-5f93-4d03-9398-eccb255f1c5a"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the code for the search page .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.52.51Screen%20Shot%202023-12-01%20at%2012.50.29%20PM.png.webp?alt=media&token=d1d7ff12-913c-413a-a254-42f300f4fde8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Html code for serach form page .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.53.21Screen%20Shot%202023-12-01%20at%2012.50.41%20PM.png.webp?alt=media&token=3ebd1c74-310e-44bb-89ec-1af1d3cc50ac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Html code for serach form page .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T17.53.44Screen%20Shot%202023-12-01%20at%2012.50.48%20PM.png.webp?alt=media&token=5e67873b-6bde-46ce-b9bc-24aa45ed3915"/></td></tr>
<tr><td> <em>Caption:</em> <p>Html code for serach form page .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.09.56Screen%20Shot%202023-12-01%20at%201.08.00%20PM.png.webp?alt=media&token=068c4f34-8e44-4a9e-94cb-225fe80c2844"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image contains donations search route code.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.25.06Screen%20Shot%202023-12-01%20at%201.08.24%20PM.png.webp?alt=media&token=b51b0029-2e2f-48b2-9867-197fc19e1a1d"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains the search todo from 1-8.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.27.50Screen%20Shot%202023-12-01%20at%201.08.38%20PM.png.webp?alt=media&token=0bfefc94-43a1-44b2-a50d-387192692816"/></td></tr>
<tr><td> <em>Caption:</em> <p>it contains the search todo from 9-12<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.33.21Screen%20Shot%202023-12-01%20at%201.30.34%20PM.png.webp?alt=media&token=e26a4f8e-11a5-49a3-91cf-68fccb9bd004"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image contains add todo 1,2.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.35.36Screen%20Shot%202023-12-01%20at%201.30.42%20PM.png.webp?alt=media&token=34292ae7-a269-40e8-af26-4e7c8f392e24"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image has add todos from 3-9.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.37.26Screen%20Shot%202023-12-01%20at%201.31.02%20PM.png.webp?alt=media&token=05e3778d-c2c3-4d46-931a-cbec43fc8d69"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image has todos 10,11, and 7.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.41.57Screen%20Shot%202023-12-01%20at%201.39.54%20PM.png.webp?alt=media&token=714849b8-27ec-4e1e-bf2a-c499f6b6e614"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the edit code with todo 1,2.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.45.10Screen%20Shot%202023-12-01%20at%201.40.04%20PM.png.webp?alt=media&token=1fb4edfb-4ae0-47af-9190-780712a81927"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the edit todos from 3-10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T18.47.07Screen%20Shot%202023-12-01%20at%201.40.12%20PM.png.webp?alt=media&token=4270d7de-9c17-4a9d-9062-8df4b426e069"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the todo from 11-13<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T19.10.01Screen%20Shot%202023-12-01%20at%201.40.24%20PM.png.webp?alt=media&token=67aa6dde-08fc-4376-a0ff-3912e0dee2d5"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the todo 14 and 15.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T19.43.07Screen%20Shot%202023-12-01%20at%202.43.02%20PM.png.webp?alt=media&token=ef68efaf-73e8-4d6c-95aa-8a4e3b20d179"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the delete user friendly message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T19.45.52Screen%20Shot%202023-12-01%20at%202.44.49%20PM.png.webp?alt=media&token=faf142e7-353b-4eba-88da-5df525e6329e"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the delete todo 1-5<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T19.48.41create%20name.png.webp?alt=media&token=1b115e57-af58-40ae-887f-f1f3033949a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the create  page for the organization .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T20.00.21edit%20org.png.webp?alt=media&token=4e26f7d0-9446-4ce0-a4e2-95519eea3f04"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the edit page of the organization .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T20.01.02Screen%20Shot%202023-12-01%20at%202.58.32%20PM.png.webp?alt=media&token=80f770f4-409d-4c49-889a-e6fca63c6279"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the code for create and edit pages.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T20.01.58Screen%20Shot%202023-12-01%20at%202.58.40%20PM.png.webp?alt=media&token=3a3239b5-4576-4219-aae7-6a8f8b85c265"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the code for create and edit pages.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T20.13.13Screen%20Shot%202023-12-01%20at%203.08.30%20PM.png.webp?alt=media&token=df224d63-15bc-4094-b0ff-754a09cc55d2"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the search page of organization .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T20.14.40Screen%20Shot%202023-12-01%20at%203.10.39%20PM.png.webp?alt=media&token=4a8c9eee-bdaa-4bf9-986c-f75554868475"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the search page with a filter.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T20.15.32Screen%20Shot%202023-12-01%20at%203.11.30%20PM.png.webp?alt=media&token=1ec33fe6-05ca-426e-a8ef-deeb799675fd"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the search page code  of the organization .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T20.19.12Screen%20Shot%202023-12-01%20at%203.11.41%20PM.png.webp?alt=media&token=5b9addfc-1413-4f51-a90e-e7debac8e432"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the search page code  of the organization .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T20.20.40Screen%20Shot%202023-12-01%20at%203.11.54%20PM.png.webp?alt=media&token=5d07f8ad-d993-4440-b4c2-376ef8f72889"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the search page code  of the organization .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T21.44.30Screen%20Shot%202023-12-01%20at%204.44.07%20PM.png.webp?alt=media&token=68dea3e9-73db-4b25-ae72-2bb1485ea454"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the search todos from 1-4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T21.44.47Screen%20Shot%202023-12-01%20at%204.44.21%20PM.png.webp?alt=media&token=9f56d548-ccd1-4122-95d9-64dc3dc1f4ab"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the search todos from 5-9.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T21.46.39Screen%20Shot%202023-12-01%20at%204.45.37%20PM.png.webp?alt=media&token=32e589f6-080a-4cab-99a3-e5325d9d527a"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the add todos from 1-3.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T21.47.54Screen%20Shot%202023-12-01%20at%204.45.45%20PM.png.webp?alt=media&token=39e17908-1805-4ced-a7f7-edb92a736bb2"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the add todos from 4-10.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T21.49.02Screen%20Shot%202023-12-01%20at%204.45.56%20PM.png.webp?alt=media&token=1745ceb0-f130-4d83-8d55-d704facd6278"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the todos 10 and 11.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T21.56.47Screen%20Shot%202023-12-01%20at%204.53.54%20PM.png.webp?alt=media&token=6ee64a8a-f69c-4a88-9266-ac6f0667d251"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the edit todos 1 and 2 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T21.59.17Screen%20Shot%202023-12-01%20at%204.54.04%20PM.png.webp?alt=media&token=61e1da18-53d9-49c2-b7f8-8d5cff2ead57"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the edit todos 3-10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T22.00.29Screen%20Shot%202023-12-01%20at%204.55.48%20PM.png.webp?alt=media&token=4810a4df-c33e-4e0f-96da-13c091e30e9f"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the edit todos 11-13.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T22.05.14Screen%20Shot%202023-12-01%20at%205.05.04%20PM.png.webp?alt=media&token=fdca5c16-43b0-436c-a5f2-48488ad96719"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the delete todos code from 1-5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T22.06.15Screen%20Shot%202023-12-01%20at%205.02.40%20PM.png.webp?alt=media&token=18939e6f-fb8c-4000-a562-d10e87902113"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the user friendly message when a record is deleted.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-02T05.36.41Screen%20Shot%202023-12-02%20at%2012.36.07%20AM.png.webp?alt=media&token=e4a2da9d-b8d5-496e-93b2-6c4ad0d1ab59"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows all the passing test cases for test_donations.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-02T06.04.13Screen%20Shot%202023-12-02%20at%201.04.03%20AM.png.webp?alt=media&token=4afed4dd-6683-48e4-8955-6caa6d9eda72"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the tests passing in test_organization.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-02T06.06.56Screen%20Shot%202023-12-02%20at%201.06.47%20AM.png.webp?alt=media&token=e17aac8f-bf79-411e-909a-954e890e2314"/></td></tr>
<tr><td> <em>Caption:</em> <p>here the test case has failed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-02T04.03.48Screen%20Shot%202023-12-01%20at%2011.01.10%20PM.png.webp?alt=media&token=63f7c131-df2d-4cb2-9001-8ec075f56306"/></td></tr>
<tr><td> <em>Caption:</em> <p>this shows the passing test cases of test_index.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>The failure in the test_upload_csv test indicates that the expected count of organization<br>inserts doesn&#39;t match the actual count.<div>The failures you&#39;re encountering in the test_organization_edit and<br>test_organization_add tests indicate issues related to the form loading and the response code<br>from the server.<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/30">https://github.com/rishithareddy19/rv437-IS601-007/pull/30</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T22.27.47Screen%20Shot%202023-12-01%20at%205.26.37%20PM.png.webp?alt=media&token=9448e568-8af5-477b-a81e-35952c834645"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows my commit history from github.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-01T22.25.04Screen%20Shot%202023-12-01%20at%205.22.47%20PM.png.webp?alt=media&token=2ebcbe64-c3e7-453e-8937-00720beb81a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows my wakatime dashboard.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-rv437-td-a3e8e7499009.herokuapp.com/">https://is601-007-rv437-td-a3e8e7499009.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/rv437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Rishitha Vanapally (rv437)</td></tr>
<tr><td> <em>Generated: </em> 11/17/2023 11:59:50 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/rv437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T18.59.20d1%20sub1%201.png.webp?alt=media&token=34abbda2-a4e3-47e2-8436-5a16763471f3"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the ivalid email validation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T18.59.55d1%20sub1%202%20and%20d6%20sub1.png.webp?alt=media&token=b3244d04-a1d6-434e-9840-47b59b365993"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows ivalid password validation.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.01.06d1%20sub1%203%20and%20d6%20sub1.png.webp?alt=media&token=287083b8-ebe6-497d-a8bd-409a1bcb63eb"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows when the passwords not match.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.01.44d1%20sub1%204%20and%20d6%20sub1.png.webp?alt=media&token=2fe35c91-0220-42b6-9aaa-28c354908f78"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows when the entered email is not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.02.29d1%20sub1%205.png.webp?alt=media&token=3ac3b0ad-4d44-47a4-870b-9e11fe42415d"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows when the given username is not available.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.03.11d1%20sub1%206.png.webp?alt=media&token=b342f5e3-fb4c-43cb-9f4a-2fe0709b87e7"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shws when everything is entered in a correct manner<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.05.02d1%20subtask2.png.webp?alt=media&token=d658eea2-cd0a-4359-bcdd-fff0a66bb78b"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the user data which were created accordingly .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/24">https://github.com/rishithareddy19/rv437-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><b>1. Form Handling :</b></div><div>The code uses Flask-WTF to create forms, like registration and<br>login forms. These forms define input fields and rules (validators). Forms are rendered<br>in HTML templates and displayed to users. Submitted form data is sent back<br>to the server for processing.</div><div><br></div><div><b>2. Validation Logic (Frontend and Backend):</b></div><div>Frontend:</div><div>HTML5 attributes and WTForms<br>validators handle initial validation on the user's device, improving user experience by catching<br>errors early.</div><div>Backend:</div><div>Server-side validation is done in the Flask application. The validate_username and validate_email<br>methods check if the submitted data meets specified criteria and raise a ValidationError<br>if not.</div><div><br></div><div><b>3. Password Handling:</b></div><div>Passwords are managed using the PasswordField from WTForms.</div><div>The EqualTo validator<br>ensures the password and confirms password fields match.</div><div>Password length is enforced with the<br>Length validator.</div><div>In login and profile forms, the password field can be optional, allowing<br>users to update other information without changing their password.</div><div><br></div><div><b>4. Database Utilization:</b></div><div>The provided code<br>doesn't explicitly show database interaction.</div><div>Typically, after form submission, data would be processed to<br>interact with a database (e.g., checking user credentials, and storing new registrations).</div><div>The code<br>assumes the database interaction is handled elsewhere in the application (possibly in routes<br>using these forms).</div><div>In essence, the code manages user input through forms, enforces rules,<br>and facilitates user registration, login, and profile updates in a Flask application. The<br>actual database interaction is assumed to be part of the larger application.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.11.43d2%20sub1%201.png.webp?alt=media&token=75788ecc-0feb-49d8-949b-787fd48fbfc6"/></td></tr>
<tr><td> <em>Caption:</em> <p>the image shows when the passwords do not match with the one stored<br>in the DB while registering .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.13.06d2%20sub1%202.png.webp?alt=media&token=6da0d479-43b4-4efd-89ff-4c4e57ebe352"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows when an entered email or user is not existing in the<br>database.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.13.55d2%20subtask2.png.webp?alt=media&token=6dcb23fe-ea3a-4bfa-aa7a-e370f82b5654"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows when the user is successfully logged in .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/24">https://github.com/rishithareddy19/rv437-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>The login process in the provided code involves the following key aspects:</div><div><b><br></b></div><div><b>Form Handling<br>:</b></div><div>The login functionality is managed through a Flask route named "/login" and a<br>corresponding form (LoginForm). The form includes fields for email or username and password.<br>The form is created using WTForms, simplifying validation and data handling.<br></div><div><b><br></b></div><div><b>Validation Logic (Frontend<br>and Backend) :</b></div><div>Frontend: The login form incorporates client-side validation using HTML5 attributes and<br>may utilize JavaScript to enhance the user experience by checking for required fields.<br></div><div>Backend:<br>Server-side validation is performed in the Flask route associated with the "/login" endpoint.<br>The validate_email method checks whether the provided input is a valid email address,<br>and the validate_username method ensures the username's validity. Password validation is handled by<br>comparing the entered password with the stored hashed password in the database.</div><div><b><br></b></div><div><b>Password Handling<br>:</b></div><div>Passwords are securely handled using hashing. The code likely uses a secure hashing<br>algorithm (such as bcrypt) to hash and store passwords in the database. During<br>login, the entered password is hashed and compared with the stored hash for<br>authentication.<br></div><div><b><br></b></div><div><b>Database Utilization:</b></div><div>The database is utilized to store user account information. The code likely<br>includes SQL queries to interact with the database, retrieving user data based on<br>the provided email or username during the login attempt. The password comparison is<br>crucial for authentication, ensuring that only users with valid credentials can log in.<br></div><div><b><br></b></div><div>In<br>summary, the provided code ensures secure user login by handling form input, implementing<br>both frontend and backend validation, securely managing passwords through hashing, and utilizing a<br>database for storing and retrieving user account information.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.17.09d3%20subtask1.png.webp?alt=media&token=b2b059e2-fb45-447c-a359-490d47b2160a"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the output when the user has successfully logged out<br>.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.18.11d3%20subtask2%20and%20d4%20sub1.png.webp?alt=media&token=f4570188-354d-4bb9-b178-5dae777fec0e"/></td></tr>
<tr><td> <em>Caption:</em> <p>when an unauthorized user tries to log into the login protected page it<br>does not give the unauthorized user permission to enter into it.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/24">https://github.com/rishithareddy19/rv437-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The code illustrates the user login process in a Flask application by first<br>validating the login form. Upon validation, the system queries the database for user<br>information based on the provided email or username. Bcrypt is then employed to<br>verify that the submitted password aligns with the hashed password stored in the<br>database. If the password check is successful, a User object is created, encompassing<br>essential user details, and additional information such as user roles is retrieved. Flask-Login<br>is utilized to log in the user, and Flask-Principal is informed of the<br>identity change. To ensure persistent user information across requests, the user object is<br>stored in the session as JSON. Flash messages are employed for user feedback,<br>conveying the outcome of the login process. Depending on the result, the user<br>is either redirected to the landing page or presented with the login form<br>again, accompanied by appropriate error messages.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.27.37d3%20subtask2%20and%20d4%20sub1.png.webp?alt=media&token=afd2a2e8-adb2-40cb-9b3b-529d59f92eb9"/></td></tr>
<tr><td> <em>Caption:</em> <p>when an unauthorized user tries to login into the login protected page it<br>does not give the unauthorized user permission to enter into it .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.28.38d4%20subtask2.png.webp?alt=media&token=8276bb37-d824-47e4-ab70-438ff0253289"/></td></tr>
<tr><td> <em>Caption:</em> <p>when the unauthorized user tries to login without having proper role then the<br>permission is denied and it does not allow them to see the contents<br>of the page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.30.26d4%20subtask3.png.webp?alt=media&token=e2d4d1c0-e76d-406c-996a-b6b9139dcbf0"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the roles table with admin user .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.32.18d4%20subtask3.png.webp?alt=media&token=2992db4b-6d0a-4873-ae14-ac63f86654e7"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the roles with admin user.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.32.48d4%20sub4.png.webp?alt=media&token=839a45c6-7bc5-4d34-bd0f-f46e973d68f4"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the user table which was added to the roles table.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.33.39d4%20subtask4.png.webp?alt=media&token=4b38445c-4eeb-4ad9-9713-84d4a0936e7c"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the roles table where we have added the id no 13<br>to the table.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/24">https://github.com/rishithareddy19/rv437-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>In the context of login-protected pages in a Flask application:</div><div><br></div><div><b>Session Usage:&nbsp;</b>Upon successful login,<br>user information is serialized and stored in the session for subsequent requests.</div><div>Flask-Login manages<br>user sessions and provides utilities for user authentication.</div><div><br></div><div><b>Login Decorator:&nbsp;</b>The @login_required decorator from Flask-Login<br>is applied to routes corresponding to protected pages.</div><div>Ensures that only authenticated users can<br>access these pages; otherwise, users are redirected to the login page.</div><div><br></div><div><b>Session Check-in Routes:&nbsp;</b>In<br>routes for protected pages, the code checks the user's authentication status using current_user<br>from Flask-Login.</div><div>If not authenticated, users are redirected to the login page before accessing<br>the protected content.</div><div><br></div><div><b>Session Helpers:&nbsp;</b>Custom session helpers or utilities may be used for tasks<br>like retrieving user information from the session or checking authentication status.</div><div>In summary, the<br>session is crucial for maintaining the user state post-login, the @login_required decorator ensures<br>page protection and session-related utilities help manage user data and authentication status throughout<br>the application.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>In a Flask application with role-protected pages, the session serves as a storage<br>mechanism for user information, including roles, ensuring continuity across different requests. After a<br>user logs in, their details, such as roles, are stored in the session.<br>Role-protected pages are specific sections of the application that only users with certain<br>roles can access. To manage this access, custom helpers or decorators, such as<br>&quot;@role_required&quot;, are employed. Flask-Principal, an extension for Flask, simplifies role and permission management<br>by associating roles with users. Routes for role-protected pages check the user&#39;s roles<br>stored in the session. If a user lacks the required role, access may<br>be redirected or denied, ensuring that only users with the appropriate roles can<br>access designated content. This framework enhances security, allowing users to interact with content<br>aligned with their assigned roles.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T03.28.58d5%20sub1.png.webp?alt=media&token=004af59c-95b7-41bc-a668-84692c996031"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the login page including the new styled nav bar<br>.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T03.30.34d5%20sub1%201.png.webp?alt=media&token=27720ec9-5c0d-4e8d-83ec-63e0e2a306cd"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the register page including the new styled bar.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T03.33.52d5%20sub1%202.png.webp?alt=media&token=ff3a161c-facc-4481-9551-a811d152ff9c"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the welcome page after styling where i have moved<br>it a little bit to the centre.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T03.37.15d5%20sub1%203.png.webp?alt=media&token=cd8ce918-b192-4aab-9945-340353a6bd03"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the new styled profile page and when we hover<br>on the nav bar we can see the various options like sample login<br>register etc accordingly .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/24">https://github.com/rishithareddy19/rv437-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>The CSS I created is designed to style the basic elements of an<br>HTML page, such as the navigation bar, forms, containers, and buttons. Here's a<br>high-level overview:</div><div><br></div><div><b>Body Styling:</b></div><div>The body has top and bottom padding to ensure content is<br>spaced properly.<br></div><div>The background color is set to a light grayish tone (#f0f0f0) for<br>a neutral background.</div><div><br></div><div><b>Navbar Styling:</b></div><div>The navbar has a green background color (#4caf50) for a<br>vibrant and cohesive look.<br></div><div>The text color for navbar elements (brand and links) is<br>set to white for better visibility.</div><div>The navbar-toggler-icon (used for responsive navigation) has a<br>white background.</div><div><br></div><div><b>Form Styling:</b></div><div>Forms have a margin-top of 20px for spacing.<br></div><div>The background color is<br>set to white (#fff) with padding, border radius, and a box shadow to<br>create a clean and well-defined form appearance.</div><div><br></div><div><b>Container Styling:</b></div><div>The container has a margin-top of<br>20px to provide spacing from the content above.<br></div><div><br></div><div><b>Styled Table for Sample Output:</b></div><div>The styled<br>table intended for clean data output in samples has a background color of<br>green (#4caf50) for the header.<br></div><div>Table cells (th and td) have padding and a<br>bottom border for a well-organized tabular display.</div><div><br></div><div><b>Button Styling (Login and Register):</b></div><div>The primary button<br>class (.btn-primary) has a green background color and border (#4caf50).<br></div><div>On hover, the button<br>background and border color change to a slightly darker shade (#45a049).</div><div><br></div><div>These styles contribute<br>to a visually appealing and user-friendly layout, with a consistent green color theme<br>for key elements like the navbar and buttons. The overall design aims for<br>clarity, readability, and a cohesive appearance across different sections of the webpage.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.44.13d1%20sub1%202%20and%20d6%20sub1.png.webp?alt=media&token=85a2709e-6494-4474-8a64-776e039ab1a5"/></td></tr>
<tr><td> <em>Caption:</em> <p>the image a user friendly message when the password is of not according<br>to the respected length.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.45.30d3%20subtask2%20and%20d4%20sub1.png.webp?alt=media&token=4dfde4cc-3ff2-4751-8f68-d262940a7bf7"/></td></tr>
<tr><td> <em>Caption:</em> <p>when an unauthorized user tries to login into the login protected page it<br>does not give the unauthorized user permission to enter into it .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-17T19.46.27d1%20sub1%204%20and%20d6%20sub1.png.webp?alt=media&token=cb0cc8b7-cc68-4576-8379-5291b6780be7"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows when the given email is not available that is someone already<br>registered with that email address .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/24">https://github.com/rishithareddy19/rv437-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>User-friendly messages are crafted by employing several strategies to handle technical details and<br>present information in a clear and understandable manner:&nbsp;</div><div><br></div><div><b>Error Handling:</b></div><div>We use try-except blocks to<br>catch technical errors, replacing them with simpler and user-friendly messages. This shields users<br>from complex technical details.</div><div><br></div><div><b>Flash Messages:</b></div><div>Short and clear messages are displayed using flash messages<br>to inform users about the success or failure of operations. These messages are<br>designed to be easily understood.<br></div><div><br></div><div><b>Logging:</b></div><div>While developers get detailed logs for debugging, users receive<br>concise messages. This ensures users aren't overwhelmed with technical information.<br></div><div><br></div><div><b>Condition Checks:</b></div><div>We check conditions<br>before executing actions and display user-friendly messages if something goes wrong. For instance,<br>before deleting a role, we ensure the necessary information is present.<br></div><div><br></div><div>Overall, these measures<br>ensure that users receive clear and understandable messages, making their interaction with the<br>application more positive, while still providing developers with the technical details they need<br>for troubleshooting.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T04.12.44d7%20sub1.png.webp?alt=media&token=1a5db46a-6ab5-4207-9443-5770f03d6013"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the user profile page with username and email filled properly.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/24">https://github.com/rishithareddy19/rv437-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The code retrieves user information from a database and shows it in a<br>form. The form is designed for updating user details, including the username, email,<br>and password. The password field is optional, allowing users to update other information<br>without changing their password. When users submit the form, the server handles the<br>update process, ensuring data validation and making the necessary changes in the database.<br>In essence, it&#39;s a straightforward process of displaying user details in a form<br>for potential updates, with the option to change the password if desired.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T04.17.31d8%20sub1%201.png.webp?alt=media&token=8ce7b70e-8b4e-412f-aafb-7306ac587d3e"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the username validation message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T04.19.11d8%20sub1%202.png.webp?alt=media&token=7d5b4bde-4356-461c-bb78-3932232d2ae5"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the email validation message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T04.20.18d8%20sub1%203.png.webp?alt=media&token=9cbaabb0-62d4-4b0c-b698-87caa46c735d"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows password validation that is when we enter a wrong<br>one.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T04.21.44d8%20sub1%204.png.webp?alt=media&token=8c2b4344-f2c8-4f56-88c6-a791d670b2c8"/></td></tr>
<tr><td> <em>Caption:</em> <p>the image shows the message when they don’t match.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T04.24.58d8%20sub1%205.png.webp?alt=media&token=381b0d1f-1cd6-4a99-9015-b7335a5086df"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows a message when the given email/username which was already in use.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T04.26.02d8%20sub%202%20before.png.webp?alt=media&token=ebc1bf68-a4ce-4b21-89c4-496e50d9fd16"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the user table before the changes are made to<br>the profile.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-11-18T04.28.44d8%20sub%202%20after.png.webp?alt=media&token=2ff5e50c-f926-4fbc-855a-f095b780788e"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the user table after the email id has been<br>changed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/24">https://github.com/rishithareddy19/rv437-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>The code is a test for the Flask web application's edit page, focusing<br>on the edit logic. Here's a simplified explanation:</div><div><br></div><div>Fixture Setup: The app fixture initializes<br>the Flask app and configures it. It also inserts a test record into<br>the database.</div><div>client and runner fixtures simulate a test client and CLI runner for<br>the app.</div><div><br></div><div>Test Scenario: the test_edit_page function simulates a request to the "/sample/edit" endpoint<br>with the query parameter id=-1.</div><div><br></div><div>Validation Check: The HTML response is parsed, and the<br>value of a form element with the name "value" is checked.</div><div><br></div><div>Assertion: The test<br>verifies that the value matches the expected value ("tcval").</div><div><br></div><div>Cleanup: The test client automatically<br>cleans up resources after the test.</div><div><br></div><div>In summary, the code sets up the app,<br>simulates an edit page request, checks the value in the response, and ensures<br>it matches the expected value. The&nbsp; code specifically focuses on the validation check<br>for the "value" field in the edit page form.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>The main issue I faced was when I was trying to run it<br>on Heroku then the challenge started I resolved them when I followed the<br>modules step by step, but the Professor helped me a lot and guided<br>me throughout the process.<div>Throughout this milestone, several key learnings emerged, including mastering form<br>handling and validation in web applications using Flask and WTForms, understanding database interactions<br>with Flask-SQLAlchemy, implementing Flask Blueprints for effective project structuring, styling web forms with<br>HTML and Bootstrap, writing tests using the pytest framework for Flask applications, incorporating<br>user authentication and authorization with Flask-Login and Flask-Principal, and becoming proficient in rendering<br>HTML templates using the Jinja2 template engine. These learnings contribute to a comprehensive<br>skill set for developing robust and well-organized Flask applications, and the resources utilized<br>include Flask documentation, Bootstrap documentation, and other relevant frameworks.<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://rv437-is601-007-prod-4abc3acad7b6.herokuapp.com/login">https://rv437-is601-007-prod-4abc3acad7b6.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/rv437" target="_blank">Grading</a></td></tr></table>
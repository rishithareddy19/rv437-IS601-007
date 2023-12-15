<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Rishitha Vanapally (rv437)</td></tr>
<tr><td> <em>Generated: </em> 12/14/2023 4:55:00 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/rv437" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <p>I have chosen the Edamam Food and Grocery Database&nbsp;<div>Link -&nbsp;<a href="https://rapidapi.com/edamam/api/edamam-food-and-grocery-database">https://rapidapi.com/edamam/api/edamam-food-and-grocery-database</a></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <p style="box-sizing: border-box; color: rgba(0, 0, 0, 0.65); font-family: Lato, sans-serif; font-size: 16px;">The<br>parser access point handles text search for foods as well as filters for<br>the foods like the presence of specific nutrient content or exclusion of allergens.</p><ul<br>style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px; padding-left: 2em; color: rgba(0, 0, 0, 0.65);<br>font-family: Lato, sans-serif; font-size: 16px;"><li style="box-sizing: border-box;">Search for a phrase or keyword using<br>NLP to get food entities from it.</li><li style="box-sizing: border-box; margin-top: 0.25em;">Get basic nutrition<br>facts and ingredients for each food</li><li style="box-sizing: border-box; margin-top: 0.25em;">Search for food by<br>given nutrient quantity for 28 nutrients</li><li style="box-sizing: border-box; margin-top: 0.25em;">Search for foods within<br>a given brand</li><li style="box-sizing: border-box; margin-top: 0.25em;">With the built-in food-logging context, it allows<br>for requests which do not contain quantity and suggest expected quantities for them.</li></ul><div><font<br>color="#ba0065" face="Lato, sans-serif"><span style="font-size: 16px;">I have chosen the first get&nbsp;</span></font><span style="background-color: rgb(244, 244,<br>245); font-family: Lato, sans-serif; text-wrap: nowrap;">Food Request Step 1 - Parser GET-</span><span style="background-color:<br>rgba(0, 0, 0, 0.08); font-family: Lato, sans-serif; text-wrap: nowrap;">/api/food-database/v2/parser</span></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <p><label style="box-sizing: border-box; touch-action: manipulation; font-size: 12px; font-family: Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu<br>Mono&quot;, monospace; display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px; padding: 0px;<br>user-select: text; cursor: pointer;">hints:</label><span style="box-sizing: border-box; font-family: Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;,<br>monospace; font-size: 12px; padding: 0px; cursor: pointer; color: rgba(0, 0, 0, 0.45); opacity:<br>0.75;"><span style="box-sizing: border-box;"><span style="box-sizing: border-box; margin-left: 0.3em; margin-right: 0.3em;">[]</span>&nbsp;20 items</span></span><ul style="box-sizing: border-box; margin:<br>0px; font-family: Consolas, Monaco, &quot;Andale Mono&quot;, &quot;Ubuntu Mono&quot;, monospace; font-size: 12px; padding: 0px;<br>list-style: none;"><li style="box-sizing: border-box; position: relative; padding-top: 0.25em; margin-left: 0.875em; padding-left: 0px;"><div style="color:<br>rgba(0, 0, 0, 0.65); box-sizing: border-box; display: inline-block; padding-right: 0.5em; padding-left: 0px; cursor:<br>pointer;"><div style="box-sizing: border-box; margin-left: 0px; transition: all 150ms ease 0s; transform: rotateZ(90deg); transform-origin:<br>45% 50%; position: relative; line-height: 1; font-size: 0.75em; height: 12px; display: inline-block; vertical-align:<br>middle; color: rgba(0, 0, 0, 0.6);">▶</div></div><label style="box-sizing: border-box; touch-action: manipulation; display: inline-block; color:<br>rgba(0, 0, 0, 0.6); margin: 0px; padding: 0px; user-select: text; cursor: pointer;">hints:</label><span style="box-sizing:<br>border-box; padding: 0px; cursor: pointer; color: rgba(0, 0, 0, 0.45); opacity: 0.75;"><span style="box-sizing:<br>border-box;"><span style="box-sizing: border-box; margin-left: 0.3em; margin-right: 0.3em;">[]</span>&nbsp;20 items</span></span><ul style="box-sizing: border-box; margin: 0px; color:<br>rgba(0, 0, 0, 0.65); padding: 0px; list-style: none;"><li style="box-sizing: border-box; position: relative; padding-top:<br>0.25em; margin-left: 0.875em; padding-left: 0px;"><div style="box-sizing: border-box; display: inline-block; padding-right: 0.5em; padding-left: 0px;<br>cursor: pointer;"><div style="box-sizing: border-box; margin-left: 0px; transition: all 150ms ease 0s; transform: rotateZ(90deg);<br>transform-origin: 45% 50%; position: relative; line-height: 1; font-size: 0.75em; height: 12px; display: inline-block;<br>vertical-align: middle; color: rgba(0, 0, 0, 0.6);">▶</div></div><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em<br>!important; display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px; padding: 0px; user-select:<br>text; cursor: pointer;">0:</label><span style="box-sizing: border-box; padding: 0px; cursor: pointer; color: rgba(0, 0, 0,<br>0.45); opacity: 0.75;"><span style="box-sizing: border-box;"><span style="box-sizing: border-box; margin-left: 0.3em; margin-right: 0.3em;">{}</span>&nbsp;2 keys</span></span><ul style="box-sizing:<br>border-box; margin: 0px; padding: 0px; list-style: none;"><li style="box-sizing: border-box; position: relative; padding-top: 0.25em;<br>margin-left: 0.875em; padding-left: 0px;"><div style="box-sizing: border-box; display: inline-block; padding-right: 0.5em; padding-left: 0px; cursor:<br>pointer;"><div style="box-sizing: border-box; margin-left: 0px; transition: all 150ms ease 0s; transform: rotateZ(90deg); transform-origin:<br>45% 50%; position: relative; line-height: 1; font-size: 0.75em; height: 12px; display: inline-block; vertical-align:<br>middle; color: rgba(0, 0, 0, 0.6);">▶</div></div><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important;<br>display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px; padding: 0px; user-select: text;<br>cursor: pointer;">food:</label><span style="box-sizing: border-box; padding: 0px; cursor: pointer; color: rgba(0, 0, 0, 0.45);<br>opacity: 0.75;"><span style="box-sizing: border-box;"><span style="box-sizing: border-box; margin-left: 0.3em; margin-right: 0.3em;">{}</span>&nbsp;8 keys</span></span><ul style="box-sizing: border-box;<br>margin: 0px; padding: 0px; list-style: none;"><li style="box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left:<br>0.875em; user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em; word-break: break-all;"><label style="box-sizing: border-box;<br>touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0, 0, 0, 0.6); margin:<br>0px 0.5em 0px 0px;">foodId:</label><span style="box-sizing: border-box; color: rgb(82, 196, 26);">&quot;food_bwrgmmqau78xrdazxx79obeezumz&quot;</span></li><li style="box-sizing: border-box; padding-top:<br>0.25em; padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em;<br>word-break: break-all;"><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0,<br>0, 0, 0.6); margin: 0px 0.5em 0px 0px;">uri:</label><span style="box-sizing: border-box; color: rgb(82, 196,<br>26);">&quot;<a href="http://www.edamam.com/ontologies/edamam.owl#Food_01001">http://www.edamam.com/ontologies/edamam.owl#Food_01001</a>&quot;</span></li><li style="box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word;<br>padding-left: 2.125em; text-indent: -0.5em; word-break: break-all;"><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important;<br>display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px 0.5em 0px 0px;">label:</label><span style="box-sizing:<br>border-box; color: rgb(82, 196, 26);">&quot;Butter, Salted&quot;</span></li><li style="box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left:<br>0.875em; user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em; word-break: break-all;"><label style="box-sizing: border-box;<br>touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0, 0, 0, 0.6); margin:<br>0px 0.5em 0px 0px;">knownAs:</label><span style="box-sizing: border-box; color: rgb(82, 196, 26);">&quot;Butter, salted&quot;</span></li><li style="box-sizing: border-box;<br>position: relative; padding-top: 0.25em; margin-left: 0.875em; padding-left: 0px;"><div style="box-sizing: border-box; display: inline-block; padding-right:<br>0.5em; padding-left: 0px; cursor: pointer;"><div style="box-sizing: border-box; margin-left: 0px; transition: all 150ms ease<br>0s; transform: rotateZ(90deg); transform-origin: 45% 50%; position: relative; line-height: 1; font-size: 0.75em; height:<br>12px; display: inline-block; vertical-align: middle; color: rgba(0, 0, 0, 0.6);">▶</div></div><label style="box-sizing: border-box; touch-action:<br>manipulation; font-size: 1em !important; display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px;<br>padding: 0px; user-select: text; cursor: pointer;">nutrients:</label><span style="box-sizing: border-box; padding: 0px; cursor: pointer; color:<br>rgba(0, 0, 0, 0.45); opacity: 0.75;"><span style="box-sizing: border-box;"><span style="box-sizing: border-box; margin-left: 0.3em; margin-right:<br>0.3em;">{}</span>&nbsp;5 keys</span></span><ul style="box-sizing: border-box; margin: 0px; padding: 0px; list-style: none;"><li style="box-sizing: border-box; padding-top:<br>0.25em; padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em;<br>word-break: break-all;"><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0,<br>0, 0, 0.6); margin: 0px 0.5em 0px 0px;">ENERC_KCAL:</label><span style="box-sizing: border-box; color: rgb(13, 147,<br>242);">717</span></li><li style="box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word;<br>padding-left: 2.125em; text-indent: -0.5em; word-break: break-all;"><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important;<br>display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px 0.5em 0px 0px;">PROCNT:</label><span style="box-sizing:<br>border-box; color: rgb(13, 147, 242);">0.85</span></li><li style="box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left: 0.875em;<br>user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em; word-break: break-all;"><label style="box-sizing: border-box; touch-action:<br>manipulation; font-size: 1em !important; display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px<br>0.5em 0px 0px;">FAT:</label><span style="box-sizing: border-box; color: rgb(13, 147, 242);">81.1</span></li><li style="box-sizing: border-box; padding-top: 0.25em;<br>padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em; word-break:<br>break-all;"><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0, 0,<br>0, 0.6); margin: 0px 0.5em 0px 0px;">CHOCDF:</label><span style="box-sizing: border-box; color: rgb(13, 147, 242);">0.06</span></li>&lt;li<br>style=&quot;box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word; padding-left:<br>2.125em; text-indent: -0.5em; word-break: break-all;&quot;&gt;<label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display:<br>inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px 0.5em 0px 0px;">FIBTG:</label><span style="box-sizing: border-box;<br>color: rgb(13, 147, 242);">0</span></li></ul></li><li style="box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left: 0.875em; user-select:<br>text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em; word-break: break-all;"><label style="box-sizing: border-box; touch-action: manipulation;<br>font-size: 1em !important; display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px 0.5em<br>0px 0px;">category:</label><span style="box-sizing: border-box; color: rgb(82, 196, 26);">&quot;Generic foods&quot;</span></li><li style="box-sizing: border-box; padding-top: 0.25em;<br>padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em; word-break:<br>break-all;"><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0, 0,<br>0, 0.6); margin: 0px 0.5em 0px 0px;">categoryLabel:</label><span style="box-sizing: border-box; color: rgb(82, 196, 26);">&quot;food&quot;</span></li>&lt;li<br>style=&quot;box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word; padding-left:<br>2.125em; text-indent: -0.5em; word-break: break-all;&quot;&gt;<label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display:<br>inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px 0.5em 0px 0px;">image:</label><span style="box-sizing: border-box;<br>color: rgb(82, 196, 26);">&quot;<a href="https://www.edamam.com/food-img/515/515af390107678fce1533a31ee4cc35b.jpeg">https://www.edamam.com/food-img/515/515af390107678fce1533a31ee4cc35b.jpeg</a>&quot;</span></li></ul></li><li style="box-sizing: border-box; position: relative; padding-top: 0.25em; margin-left: 0.875em; padding-left:<br>0px;"><div style="box-sizing: border-box; display: inline-block; padding-right: 0.5em; padding-left: 0px; cursor: pointer;"><div style="box-sizing: border-box;<br>margin-left: 0px; transition: all 150ms ease 0s; transform: rotateZ(90deg); transform-origin: 45% 50%; position:<br>relative; line-height: 1; font-size: 0.75em; height: 12px; display: inline-block; vertical-align: middle; color: rgba(0,<br>0, 0, 0.6);">▶</div></div><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display: inline-block; color:<br>rgba(0, 0, 0, 0.6); margin: 0px; padding: 0px; user-select: text; cursor: pointer;">measures:</label><span style="box-sizing:<br>border-box; padding: 0px; cursor: pointer; color: rgba(0, 0, 0, 0.45); opacity: 0.75;"><span style="box-sizing:<br>border-box;"><span style="box-sizing: border-box; margin-left: 0.3em; margin-right: 0.3em;">[]</span>&nbsp;11 items</span></span><ul style="box-sizing: border-box; margin: 0px; padding:<br>0px; list-style: none;"><li style="box-sizing: border-box; position: relative; padding-top: 0.25em; margin-left: 0.875em; padding-left: 0px;">&lt;div<br>style=&quot;box-sizing: border-box; display: inline-block; padding-right: 0.5em; padding-left: 0px; cursor: pointer;&quot;&gt;<div style="box-sizing: border-box; margin-left:<br>0px; transition: all 150ms ease 0s; transform: rotateZ(90deg); transform-origin: 45% 50%; position: relative;<br>line-height: 1; font-size: 0.75em; height: 12px; display: inline-block; vertical-align: middle; color: rgba(0, 0,<br>0, 0.6);">▶</div></div><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0,<br>0, 0, 0.6); margin: 0px; padding: 0px; user-select: text; cursor: pointer;">0:</label><span style="box-sizing: border-box;<br>padding: 0px; cursor: pointer; color: rgba(0, 0, 0, 0.45); opacity: 0.75;"><span style="box-sizing: border-box;">&lt;span<br>style=&quot;box-sizing: border-box; margin-left: 0.3em; margin-right: 0.3em;&quot;&gt;{}</span>&nbsp;3 keys</span></span><ul style="box-sizing: border-box; margin: 0px; padding: 0px;<br>list-style: none;"><li style="box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap:<br>break-word; padding-left: 2.125em; text-indent: -0.5em; word-break: break-all;"><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em<br>!important; display: inline-block; color: rgba(0, 0, 0, 0.6); margin: 0px 0.5em 0px 0px;">uri:</label>&lt;span<br>style=&quot;box-sizing: border-box; color: rgb(82, 196, 26);&quot;&gt;&quot;<a href="http://www.edamam.com/ontologies/edamam.owl#Measure_serving">http://www.edamam.com/ontologies/edamam.owl#Measure_serving</a>&quot;</span></li><li style="box-sizing: border-box; padding-top: 0.25em; padding-right: 0px; margin-left:<br>0.875em; user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em; word-break: break-all;"><label style="box-sizing: border-box;<br>touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0, 0, 0, 0.6); margin:<br>0px 0.5em 0px 0px;">label:</label><span style="box-sizing: border-box; color: rgb(82, 196, 26);">&quot;Serving&quot;</span></li><li style="box-sizing: border-box; padding-top:<br>0.25em; padding-right: 0px; margin-left: 0.875em; user-select: text; overflow-wrap: break-word; padding-left: 2.125em; text-indent: -0.5em;<br>word-break: break-all;"><label style="box-sizing: border-box; touch-action: manipulation; font-size: 1em !important; display: inline-block; color: rgba(0,<br>0, 0, 0.6); margin: 0px 0.5em 0px 0px;">weight:</label><span style="box-sizing: border-box; color: rgb(13, 147,<br>242);">14</span></li></ul></li></ul></li></ul></li></ul></li><ul style="box-sizing: border-box; margin: 0px; padding: 0px; list-style: none;"><li style="text-indent: -6px;"><font color="#0d93f2">I’m planning<br>to choose 10 fields from the above&nbsp;</font></li><li style="text-indent: -6px;"><font color="#0d93f2">1) Food ID</font></li><li style="text-indent:<br>-6px;"><font color="#0d93f2">2)URL</font></li><li style="text-indent: -6px;"><font color="#0d93f2">3)label</font></li><li style="text-indent: -6px;"><font color="#0d93f2">4)From Nutrients I have chosen&nbsp;</font>ENERC_KCAL, PROCNT,FAT,Carbohydrate<br>, fiber,category</li><li style="text-indent: -6px;">5)label,weight from measures&nbsp;</li></ul></ul><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <p>I’m planning to use the data to represent various foods along with their<br>nutritional value and the category to which it belongs. Here I’m planning on<br>showing the data list according to the taken API and where we can<br>add new data too.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T20.57.50data%20filled%20add.png.webp?alt=media&token=a51880a2-adc1-4500-b513-598c763626b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the valid data filled in .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T20.58.27data%20add.png.webp?alt=media&token=72099bb3-cbcc-4079-a550-2a2c3c360137"/></td></tr>
<tr><td> <em>Caption:</em> <p>the above image shows the valid data filled in .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T20.59.05d2%20success.png.webp?alt=media&token=78950ece-8fca-4c95-9ef6-7e3744a280b5"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the success message when added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T20.59.39invalid%20add.png.webp?alt=media&token=cf695972-eddc-4f24-8e64-1edb8ce597c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the message when invalid data is entered.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.00.28code%20for%20add.png.webp?alt=media&token=f49c0d5c-2850-47dd-b693-24533cbacb3c"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the code snippets for create page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.01.03code%20add.png.webp?alt=media&token=c9fd81d2-e0a1-400b-bf3b-37b43c42278d"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the code snippets for create page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.05.10database%20.png.webp?alt=media&token=b1eafbc5-2a5d-4e8b-8e64-6f963a106a64"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the database when its being included<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/33">https://github.com/rishithareddy19/rv437-IS601-007/pull/33</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.07.16list%20page.png.webp?alt=media&token=3816dc11-1e64-4a1e-b474-e67234d496b7"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the list items where every record is displayed .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.08.02kcal%20filter.png.webp?alt=media&token=d31786c5-f00c-4eb4-b2f9-4ab2c2ad4d4a"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the list when the energy kcal filter is applied where i<br>entered the value and it shows the records which contains them.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.10.53label%20filter.png.webp?alt=media&token=3c1390ae-f5b9-4060-a631-4107431bc435"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows when the label filter is applied <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.11.35no%20record%20image.png.webp?alt=media&token=91129f6b-19d8-458c-ad43-a82690ef4bdc"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows when there are no records.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.13.29list%20page.png.webp?alt=media&token=8317c564-806c-4720-8c87-862cfc2d2399"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the page where each record contains view edit and delete options.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/33">https://github.com/rishithareddy19/rv437-IS601-007/pull/33</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.14.14view%20page.png.webp?alt=media&token=3f192b6d-035f-461f-a5d5-c36ca94337d9"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the view page .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/33">https://github.com/rishithareddy19/rv437-IS601-007/pull/33</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.14.41edit%20page.png.webp?alt=media&token=63074702-52ff-42ca-b037-cd9cdceb1e05"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the edit page with existing data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.16.24edit%20invalid.png.webp?alt=media&token=c6c99571-1aaa-4826-bb8e-d47a6667f691"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the message when invalid data is being entered or trying to<br>be edited.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.18.06update%20msg.png.webp?alt=media&token=c63db1f2-6eb6-4591-a5e2-d128373b4003"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the image when the record is updated successfully .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.19.01before%20database.png.webp?alt=media&token=75d30656-9f20-4edc-89e6-df7b88ddb9d0"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the database before editing the records.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.27.48after%20database.png.webp?alt=media&token=6a924621-2409-424f-a717-02ee36920644"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the database after editing the record.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/33">https://github.com/rishithareddy19/rv437-IS601-007/pull/33</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.28.32delete%20record.png.webp?alt=media&token=99185f50-49a8-4ac4-afd0-0a2c9932c54d"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows when the record is deleted successfully <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.29.37delete%20smallcurd.png.webp?alt=media&token=2eaefecc-0d63-4f27-9f4d-6a7283b340a4"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the page after the record is deleted and its not being<br>displayed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.31.09before%20database.png.webp?alt=media&token=c2f5b586-a4ac-494a-bb76-6d1f216c383c"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the database before the record is deleted.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.31.47database%20after%20delet.png.webp?alt=media&token=6d329ef6-d426-4839-ba6d-9cf024419461"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows the database when the record is deleted successfully .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/33">https://github.com/rishithareddy19/rv437-IS601-007/pull/33</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.35.28Screen%20Shot%202023-12-14%20at%204.33.45%20PM.png.webp?alt=media&token=c80a023f-9d91-416f-b9e0-db90ce49458a"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows how the API data is being fetched where in api.py file<br>I have attached the api host link and their required credentials.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.39.36Screen%20Shot%202023-12-14%20at%204.33.21%20PM.png.webp?alt=media&token=3a896544-c972-419b-8d46-8d3a1c4f3580"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows how the data taken from the api is being transferred into<br>the database.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.40.36Screen%20Shot%202023-12-14%20at%204.39.15%20PM.png.webp?alt=media&token=c5475511-5b05-4fcf-b2bc-c72abc9275fd"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows how the data taken from the api is being transferred into<br>the database.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.42.37Screen%20Shot%202023-12-14%20at%204.34.07%20PM.png.webp?alt=media&token=1a59cf76-cb18-44cc-8067-b5101fc68358"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows how  the system is being triggered to fetch the data.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.43.13Screen%20Shot%202023-12-14%20at%204.34.14%20PM.png.webp?alt=media&token=c1d9115b-45fa-4c7b-a146-3dfaf8a5830f"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows how  the system is being triggered to fetch the data.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <div>Here's a brief overview of the steps involved in the data loading, transformation,<br>and application process:</div><div><br></div><div><b>Trigger:</b></div><div>The process begins when a user initiates an action or when<br>an application needs to load new data.</div><div><br></div><div><b>Extraction (Load):</b></div><div>Data is extracted from sources like<br>APIs, files, or databases.<br></div><div><br></div><div><b>Transformation:</b></div><div>Extracted data is cleaned and transformed into the desired format<br>for the target database.<br></div><div><br></div><div><b>Validation:</b></div><div>Data integrity is validated to ensure it meets predefined rules.<br></div><div><br></div><div><b>Loading<br>(Apply):</b></div><div>Transformed data is loaded into the target database.<br></div><div><br></div><div><b>Database Operations:</b></div><div>Database operations are performed to<br>insert, update, or delete records.<br></div><div><br></div><div><b>Logging and Monitoring:</b></div><div>Logging and monitoring track the success or<br>failure of the data loading process.<br></div><div><br></div><div><b>Error Handling:</b></div><div>Robust error handling manages unexpected issues during<br>data loading.<br></div><div><br></div><div><b>Notification (Optional):</b></div><div>Notifications may be sent to stakeholders or systems about process completion<br>or issues.<br></div><div><br></div><div><b>Scheduled or Triggered Repeat:</b></div><div>The process may be scheduled or triggered to run<br>at specific intervals or events.<br></div><div><br></div><div>This represents a basic ETL process used in data<br>integration, ensuring data quality and keeping the database up-to-date. Tools like Apache Kafka,<br>Talend, or Apache NiFi can be employed to automate and streamline these steps<br>based on specific requirements and technologies.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/rishithareddy19/rv437-IS601-007/pull/33">https://github.com/rishithareddy19/rv437-IS601-007/pull/33</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I have faced issues with the API where I could not get the<br>complete data so the Professor helped a lot and sir has advised me<br>to work on custom data. Coming to the learning part I have learned<br>how to create a web application using Python, and Flask framework where we<br>can even work with huge amounts of data.I have created a basic web<br>app with user login and then moved to create, edit, view, and delete<br>functions on the data.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://rv437-is601-007-prod-3811479d33dd.herokuapp.com/">https://rv437-is601-007-prod-3811479d33dd.herokuapp.com/</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.51.04waka.png.webp?alt=media&token=254daad4-4ed1-4002-8138-0c48d9fc80cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows my waka time.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Frv437%2F2023-12-14T21.51.26wak.png.webp?alt=media&token=1f77f318-5f87-4fa2-ad7b-a9dbcf8f79c5"/></td></tr>
<tr><td> <em>Caption:</em> <p>it shows my waka time.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/rv437" target="_blank">Grading</a></td></tr></table>
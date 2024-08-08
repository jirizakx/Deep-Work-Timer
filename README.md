<h1>Deep work timer</h1>
<br>
This is a simplistic deep work tracker.<br>
In case you want to upgrade it further, please do so.
<br>
<h3>Instalation:</h3>
<ol>
  <li>After downloading, add final directory of this script to path so that it can be used everywhere (e.g. export PATH="$HOME/bin/dw-timer/:$PATH" in .bashrc)</li>
  <li>Change the path also in the scripts (default is ~/bin/dw-timer)</li>
  <li>Make sure you have /dev/null (creation: mknod /dev/null c 1 3 ; chmod 666 /dev/null)</li>
</ol>
<h3>Usage:</h3>
<ul>
  <li>type dws for starting a session</li>
  <li>type dwe for ending a session, adding a session description and writing it to DWS_records.csv (DWS stands for Deep Work Session)</li>
  <li>type dwc to display current session time</li>
  <li>type dwt to display stats of last 7 recorded days and all-time DW time</li>
  <li>in case of accidental writing, forgetting of ending a session, etc., just adjust the data in DW_records.csv</li>
  <li>just to make sure everything works smoothly, add a description to the first session</li>
</ul>

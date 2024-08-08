<h1>Deep work timer</h1>
<br>
This is a simplistic deep work tracker.<br>
In case you want to upgrade it further, please do so.
<br>
<h3>Instalation:</h3>
<ol>
  <li>After downloading, add final directory of this script to path so that it can be used everywhere (e.g. <code>export PATH="$HOME/bin/dw-timer/:$PATH"</code> in .bashrc)</li>
  <li>Change the path also in the scripts (default is <code>~/bin/dw-timer</code>, only in the first <code>cd</code>)</li>
  <li>Make sure you have /dev/null (creation: <code>mknod /dev/null c 1 3 ; chmod 666 /dev/null</code>)</li>
</ol>
<h3>Usage:</h3>
<ul>
  <li>type <code>dws</code> for starting a session</li>
  <li>type <code>dwe</code> for ending a session, adding a session description and writing it to DWS_records.csv (DWS stands for Deep Work Session)</li>
  <li>type <code>dwc</code> to display current session time</li>
  <li>type <code>dwt</code> to display stats of last 7 recorded days and all-time DW time</li>
  <li>in case of accidental writing, forgetting of ending a session, etc., just adjust the data in DW_records.csv</li>
  <li>just to make sure everything works smoothly, add a description to the first session</li>
</ul>

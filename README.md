<b>UCL API Slack Bot</b>

Slack bot that uses the UCL API to get information about room bookings, module timetables, and UCL students/staff. Built for the UCL API Hackathon in October 2017.

<ul>Available commands:</ul>
<li>@roombot get rooms - Get all rooms in the system.</li>
<li>@roombot get rooms capacity {number} - Get all rooms with a minimum capacity of {number}.</li>
<li>@roombot search people {person} - Search for a person by name.</li>
<li>@roombot search people {email} - Search for a person by email.</ul>
  <li>@roombot module timetable {module code} - Get the timetable for a particular module.</li>
<li>@roombot my data - Get your UCL data.</li>
<li>@roombot my timetable - Get your personal timetable. (basically just a massive JSON dump at the moment, would not recommend)</li>
</ul>

<ul>To do:</ul>
<li>Replicate and fix occasional sorting bug</li>
<li>Look into slash commands for Slack</li>
<li>Prettier formatting</li>
<li>Personal timetable</li>
<li>Functions for newer (mostly timetable-related) endpoints</li>

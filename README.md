
</head>
<body>

<h1>Task Management System</h1>

<p>This is a simple voice-activated task management system. It allows users to add, remove, and display tasks using voice commands. The system also supports fuzzy matching to help recognize commands and task names even if they are not perfectly clear.</p>

<h2>Machine Learning Features</h2>
<p>The system incorporates basic machine learning principles using the <strong>Levenshtein Distance</strong> algorithm through the <code>fuzzywuzzy</code> library to match user commands and task names. This allows the system to recognize commands and tasks even when they are not perfectly spoken or written, making the task management system more user-friendly and tolerant of small errors.</p>

<h2>Features</h2>
<ul>
    <li><strong>Add tasks</strong>: Users can add a task by speaking the task they want to add.</li>
    <li><strong>Remove tasks</strong>: Users can remove tasks by saying the name of the task they want to delete. The system will find the closest match using fuzzy matching based on machine learning.</li>
    <li><strong>View tasks</strong>: Users can view all their current tasks with each task displayed on a new line.</li>
    <li><strong>Voice commands</strong>: The system uses Google Speech Recognition to listen to voice commands.</li>
    <li><strong>Sound alerts</strong>: Plays a sound when a task is added or removed successfully.</li>
</ul>

<h2>Voice Commands</h2>
<p>The following voice commands are supported:</p>
<ul>
    <li><code>insert</code>: To add a new task.</li>
    <li><code>remove</code>: To remove an existing task.</li>
    <li><code>my to do</code>: To list all the current tasks.</li>
    <li><code>exit</code>: To exit the application.</li>
</ul>

<h2>How It Works</h2>
<ol>
    <li><strong>Voice Recognition</strong>: The application listens for user commands through a microphone using <code>speech_recognition</code>.</li>
    <li><strong>Task Management</strong>: Tasks are saved in a JSON file (<code>tasks.json</code>), and the user can add, remove, and display tasks.</li>
    <li><strong>Fuzzy Matching with Machine Learning</strong>: <code>fuzzywuzzy</code> is used to match commands and task names, leveraging machine learning to handle small variations in input.</li>
    <li><strong>Sound Feedback</strong>: The <code>playsound</code> module is used to play a notification sound when a task is added or removed.</li>
</ol>

<h2>How to Run</h2>
<pre>
git clone https://github.com/your-username/task-management-system.git
pip install -r requirements.txt
python run.py
</pre>

<h2>Dependencies</h2>
<ul>
    <li><code>speech_recognition</code>: To recognize voice commands.</li>
    <li><code>fuzzywuzzy</code>: To match user input with possible commands and task names using machine learning.</li>
    <li><code>playsound</code>: To play sound notifications.</li>
    <li><code>pyaudio</code>: For capturing audio from the microphone.</li>
</ul>

<h2>File Structure</h2>
<pre>
.
├── run.py                 # Main script to run the application
├── TaskFunctions.py       # Task management functions (add, remove, load, save)
├── SpeechRecognition.py   # Function for capturing audio
├── Reminder.py            # Optional feature for setting reminders (in progress)
├── tasks.json             # JSON file storing tasks
├── word_number.txt        # Text file mapping words to numbers (for task removal)
└── README.md              # This README file
</pre>

<h2>Future Improvements</h2>
<ul>
    <li><strong>Reminders</strong>: Implement the reminder functionality to notify users after a specified amount of time.</li>
    <li><strong>Task Prioritization</strong>: Add task priority levels (low, medium, high).</li>
    <li><strong>Multiple languages</strong>: Support for voice commands in multiple languages.</li>
</ul>

<h2>Output Example</h2>
<p>Here is an example of the task management system in action:</p>
<img src="https://i.ibb.co/yyw325F/Screenshot-2024-09-26-185825.png" alt="Task Management System Output">

<h2>License and Collaboration</h2>
<p>This project is open-source and open for collaboration. If you have ideas, improvements, or want to contribute, feel free to create pull requests or contact me. All contributions are welcome!</p>

</body>
</html>

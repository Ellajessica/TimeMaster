<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TimeMaster - Django To-Do List App</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            color: #007BFF;
        }

        img {
            max-width: 100%;
            height: auto;
        }

        section {
            margin-bottom: 20px;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            margin-bottom: 10px;
        }

        a {
            color: #007BFF;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 4px;
        }
    </style>
</head>

<body>
    <h1>TimeMaster - Django To-Do List App</h1>

    

    <section>
        <h2>Features</h2>
        <ul>
            <li><strong>User Registration and Authentication:</strong> Users can create accounts, log in, and securely manage their to-do lists.</li>
            <li><strong>Task Management:</strong> Easily add, edit, mark as complete, and delete tasks.</li>
            <li><strong>Responsive Design:</strong> TimeMaster is designed to work seamlessly on various devices, providing a consistent user experience.</li>
        </ul>
    </section>

    <section>
        <h2>Installation</h2>
        <h3>Prerequisites</h3>
        <p>Before you begin, ensure you have the following installed:</p>
        <ul>
            <li>Python latest version</li>
            <li>Django latest version</li>
            
        </ul>

        <h3>Clone the Repository</h3>
        <pre><code>git clone https://github.com/your-username/TimeMaster.git
cd TimeMaster</code></pre>

        <h3>Install Dependencies</h3>
        <pre><code>pip install -r requirements.txt</code></pre>

        <h3>Configure Database</h3>
        <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

        <h3>Run the Development Server</h3>
        <pre><code>python manage.py runserver</code></pre>

        <p>Visit <a href=""http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a> in your browser to see TimeMaster in action.</p>
    </section>

    <section>
        <h2>Usage</h2>
        <ol>
            <li>Register a new account or log in with existing credentials.</li>
            <li>Access the dashboard to view, add, edit, or delete tasks.</li>
            <li>Organize your tasks by marking them as complete or incomplete.</li>
            <li>Log out when you're done.</li>
        </ol>
    </section>

    <section>
        <h2>Technologies Used</h2>
        <ul>
            <li>Django: Python Framework</li>
            <li>HTML, CSS, JavaScript: Frontend technologies for a responsive and interactive user interface.</li>
            
        </ul>
    </section>

    
</body>

</html>

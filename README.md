# CreditKeLin
<img src="https://static.vecteezy.com/system/resources/previews/000/386/795/original/illustration-of-payment-with-credit-card-vector.jpg" alt="Payment with Credit Card" width="200">

Hi there! This is an epic project for Web Programming-C at UFPS.

# Members
<div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 1;">
        <p>Kevin Jaimes 1152245</p>
        <p>Evelin Bermudez 1152278</p>
        <p>Santiago Duarte 1151992</p>
    </div>
    <div style="flex: 1; text-align: right;">
        <img src="https://lerecept.fr/wp-content/uploads/2022/12/personne.png" alt="Person" style="width: 50%; max-width: 300px;">
    </div>
</div>

# How to Install Locally

You can use "cmd" or "VS Terminal."

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px;">
    <div style="flex: 1; max-width: 50%;">
        <ol>
            <li><strong>Clone the Repository:</strong></li>
            <pre><code>git clone https://github.com/AndreyK-2305/CreditKeLin/tree/feature/initial-scaffolding</code></pre>
            <li><strong>Change Directory to "creditkelin":</strong></li>
            <pre><code>cd creditkelin</code></pre>
            <li><strong>Create a Virtual Environment:</strong></li>
            <pre><code>py -m venv venv</code></pre>
            <li><strong>Activate the Virtual Environment:</strong></li>
            <pre><code>.\venv\Scripts\activate.bat</code></pre>
            <li><strong>Install Django:</strong></li>
            <pre><code>pip install django</code></pre>
            <li><strong>Apply Migrations:</strong></li>
            <pre><code>py .\manage.py migrate</code></pre>
            <li><strong>Run the Server:</strong></li>
            <pre><code>py .\manage.py runserver</code></pre>
        </ol>
    </div>
    <div style="flex: 1; text-align: right;">
        <img src="https://th.bing.com/th/id/OIP.jE5ftU5yzsbW30WQ8xsw9QHaEK?rs=1&pid=ImgDetMain" alt="Installation Instructions" style="width: 70%; max-width: 400px; height: auto;">
    </div>
</div>

# How to Use the Makefile

The project includes a `Makefile` to simplify the management of common tasks. Below are the available commands:

<div style="font-size: 16px; line-height: 1.6;">

**Makefile Commands**

<ul style="list-style-type: none; padding: 0;">
    <li><strong><code>make venv</code></strong>: Creates a virtual environment.</li>
    <li><strong><code>make install</code></strong>: Installs the dependencies specified in <code>requirements.txt</code>.</li>
    <li><strong><code>make run</code></strong>: Runs the Django development server.</li>
    <li><strong><code>make migrate</code></strong>: Applies migrations to the database.</li>
    <li><strong><code>make makemigrations</code></strong>: Creates new migrations based on changes in the models.</li>
    <li><strong><code>make createsuperuser</code></strong>: Creates a superuser for the Django admin panel.</li>
    <li><strong><code>make clean</code></strong>: Deletes the virtual environment and cache files.</li>
    <li><strong><code>make lint</code></strong>: Runs <code>flake8</code> and <code>pylint</code> to check the style and quality of the code.</li>
</ul>

**Additional Notes**

<p>Make sure you have <code>flake8</code> and <code>pylint</code> installed in your virtual environment for the <code>make lint</code> command to work properly.</p>

</div>

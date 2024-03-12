from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock projects data
projects = [
    {"title": "Project 1", "description": "Description of Project 1", "demo": "https://example.com/demo1", "source": "https://github.com/user/project1"},
    {"title": "Project 2", "description": "Description of Project 2", "demo": "https://example.com/demo2", "source": "https://github.com/user/project2"}
]

@app.route('/projects')
def get_projects():
    return jsonify(projects)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    # Here you can process the contact form data
    # For example, send an email or store in a database
    return jsonify({"message": "Message received! We will get back to you soon."})

if __name__ == '__main__':
    app.run(debug=True)

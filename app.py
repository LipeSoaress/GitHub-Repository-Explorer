from flask import Flask, jsonify, render_template
from database import save_search, init_db
import requests
import sqlite3

app = Flask(__name__)

init_db()

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "github-repo-monitor"
}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/repo/<owner>/<repo>", methods=["GET"])
def get_repo_browser(owner, repo):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        return jsonify({"error": "GitHub API unavailable"}), 500

    if response.status_code != 200:
        return jsonify({"error": "Repo not found"}), 404

    repo_data = response.json()

    save_search(
        owner,
        repo_data["name"],
        repo_data["stargazers_count"],
        repo_data["forks_count"],
        repo_data["language"]
    )

    result = {
        "name": repo_data["name"],
        "owner": repo_data["owner"]["login"],
        "avatar": repo_data["owner"]["avatar_url"],
        "stars": repo_data["stargazers_count"],
        "forks": repo_data["forks_count"],
        "watchers": repo_data["watchers_count"],
        "language": repo_data["language"],
        "description": repo_data["description"],
        "updated_at": repo_data["updated_at"],
        "url": repo_data["html_url"]
    }

    return jsonify(result)


@app.route("/user/<username>", methods=["GET"])
def get_user_repos(username):

    url = f"https://api.github.com/users/{username}/repos?per_page=100"

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException:
        return jsonify({"error": "GitHub API unavailable"}), 500

    if response.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    repos = response.json()

    repos = sorted(repos, key=lambda r: r['stargazers_count'], reverse=True)[:10]

    save_search(owner=username)

    result = []

    for repo in repos:

        result.append({
            "name": repo["name"],
            "owner": repo["owner"]["login"],
            "avatar": repo["owner"]["avatar_url"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "watchers": repo["watchers_count"],
            "language": repo["language"],
            "description": repo["description"],
            "updated_at": repo["updated_at"],
            "url": repo["html_url"]
        })

    return jsonify(result)


@app.route("/repos", methods=["GET"])
def list_repos():

    conn = sqlite3.connect("repos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT owner, repo, stars, forks, language FROM searches")
    rows = cursor.fetchall()

    conn.close()

    result = []

    for row in rows:
        result.append({
            "owner": row[0],
            "repo": row[1],
            "stars": row[2],
            "forks": row[3],
            "description": "N/A",
            "updated_at": "N/A",
            "language": row[4]
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

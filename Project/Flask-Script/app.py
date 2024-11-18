from flask import Flask, render_template, request, redirect, url_for, flash
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages

domain_list = []

def mount():  # Mount cybershare folder
    MOUNT = subprocess.run(["mount", "-t", "nfs", "server:/path", "/mnt/cybershare"], capture_output=True, text=True)
    if MOUNT.returncode == 0:
        print('Share is mounted.')
        return True
    else:
        print('Could not mount share')
        print(MOUNT.stdout)
        print(MOUNT.stderr)
        return False

def isroot():  # Check if user is root
    if os.geteuid() == 0:
        print("DISCLAIMER - You are root")
        return True
    else:
        print("This script can only be run as root.")
        return False

def search(domain):  # Search for the domain in files
    try:
        # Create output directory if it does not exist
        os.makedirs(f"/home/assessments/{domain}", exist_ok=True)
        print(f'Searching for {domain} in all the leaked files. Please be patient...')
        subprocess.run(
            f"rg -a -F -i -p -N {domain} /mnt/cybershare/Data_Leaks >> /home/assessments/{domain}/{domain}.txt",
            shell=True, check=True
        )
        print(f'Search for {domain} is complete.')
        return True
    except subprocess.CalledProcessError as error:
        print(f'Error during search: {error}')
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_domains():
    if request.method == 'POST':
        domain = request.form['domain']
        if domain:
            domain_list.append(domain)
            flash(f"Domain '{domain}' added successfully!", "success")
        return redirect(url_for('index'))

@app.route('/run_search')
def run_search():
    if not isroot():
        flash("This script must be run as root.", "error")
        return redirect(url_for('index'))

    for domain in domain_list:
        if search(domain):
            flash(f"Search completed for {domain}", "success")
        else:
            flash(f"Error during search for {domain}", "error")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

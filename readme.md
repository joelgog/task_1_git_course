# Git and GitHub Exercise

Welcome to this practical exercise on Git and GitHub. This exercise is designed to give you hands-on experience with common Git operations and to understand the process of collaborating on a project using Git and GitHub.

This exercise must be completed in **groups of 2 or 3**.

## Steps:

### 1. Fork the Repository
First, one group member should fork the repository. This creates a copy of the repository in your own GitHub account.

To do this:

- Navigate to the main page of the repository
- In the top-right corner of the page, click "Fork"

### 2. Add Collaborators
Next, the person who forked the repository needs to add the other group members as collaborators.

To do this:

- Go to the main page of the forked repository in your account
- Click on the "Settings" tab
- In the left side-bar, click "Collaborators"
- Type the GitHub usernames of your group members and click "Add collaborator"

### 3. Clone the Repository
Now, each group member needs to clone the repository to their local machine. This allows you to work on the project locally.

To do this:

- Go to the main page of the repository
- Click the green "Code" button
- In the "Clone" tab, copy the URL for the repository
- Open Git Bash (or another terminal program)
- Navigate to the directory where you want to clone the repository
- Type `git clone` and then paste the URL you copied. Press Enter

### 4. Work on the Tasks
In your local copy of the repository, open the provided Python or R script. There are two tasks in each script, which are marked with comments. Work together with your group to complete these tasks.

Before starting to work on the tasks, make sure you create a new branch:

- Navigate to the directory of the repository in Git Bash (or another terminal program)
- Create a new branch by typing `git checkout -b branch-name`, replacing "branch-name" with a name for your branch (for example, "task-solutions").

### 5. Push Changes and Create Pull Request
Once you've completed the tasks, it's time to push your changes to GitHub and create a pull request.

To do this:

- Still within the directory of the repository in Git Bash (or another terminal program), stage your changes by typing `git add .`
- Commit your changes by typing `git commit -m "Completed tasks"`
- Push your changes by typing `git push origin branch-name`, replacing "branch-name" with the name of your branch
- Go to the main page of the original repository (not your forked copy)
- Click the "Pull requests" tab
- Click the "New pull request" button
- Click "compare across forks"
- In the "head repository" dropdown, select your forked copy of the repository
- In the "compare" dropdown, select the branch you've just pushed
- Click "Create pull request"

Now you're done! You've completed the tasks, pushed your changes to GitHub, and created a pull request. You've successfully collaborated on a project using Git and GitHub!

Remember to communicate effectively with your group members, and enjoy the process of collaborative coding.


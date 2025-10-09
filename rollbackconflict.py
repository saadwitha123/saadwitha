----What is Git Rollback?

Rollback in Git means undoing or going back to a previous version of your code.

It helps when you make a mistake in your code or commit and want to return to an earlier safe state.
 Ways to Roll Back in Git

There are 3 main ways, depending on what you need to do:

1.Undo the last commit but keep changes

If you just want to edit or fix the last commit (not lose your code):

git reset --soft HEAD~1


* This removes the last commit, but your files stay the same — you can recommit after fixing.

2. Undo the last commit and remove changes

If you want to completely delete the last commit and its changes:

git reset --hard HEAD~1


* This erases the last commit and all changes permanently (be careful).

3.Go back to a specific commit

If you want to roll back to a certain point in history:

git reset --hard <commit_id>


* You can find the commit ID using:

git log

4. Use git revert (safe way)

If you already pushed your commit to GitHub and want to undo it safely (without deleting history):

git revert <commit_id>



----What is a Conflict in Git?

A Git conflict happens when two people (or two branches) make different changes to the same part of a file, and Git doesn’t know which one to keep.

So, Git says:

“I don’t know which version you want — please fix it manually.”

 Example:

Imagine you and your friend are both editing the same file app.py.

You change line 10 to:

print("Hello from Saadwitha")


Your friend changes the same line to:

print("Hello from Varanganti")


Now, when you try to merge or pull, Git gets confused because both changes conflict.
# QuizzGame

## The goal of this project is to create a quizz app in Python.

In this app we will have two kinds of user:
 - Admin : who can create quizz.
 - User : Answer the quizz.
 
Some features are mandatory : 
   - Be able to log up and log in
   - Save of results 
   - Show good answers and score



## Making changes and creating a PR

If you are new to this sort of thing, check out this [free video course](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github) by Kent C. Dodds about how to contribute to an open source project. It walks you through the basics of using git and GitHub to contribute to an open source project.

Once you have a good understanding of git and GitHub, do the following.

- Fork the project and create a new branch of `master` with the name `pr/FEATURE` with "FEATURE" being a descriptive name of the changes you are making.
- Run `$ npm install` This will install dependencies and also run the linter, test suite, and build the project to make sure everything works okay.
- Assuming there are no problems, start making changes! Feel free to ask questions in the issue you created if you do not know how to approach a tricky nuance.
- Your commit messages should be descriptive of the changes made and reference any relevent issues: `"Fix minor Typescript errors, closes #200"`.
- Make sure to add tests for any substantial additions and that all the code follows the code styles (`$ npm run lint`).
- Once all the changes are in place, run `git fetch` and [rebase](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) onto `master` to maintain a simple history for everyone. `$ git rebase upstream/master pr/FEATURE`
  - **Note**: You are not rebasing on `origin/master` since that is just the master of _your_ fork, which will also be outdated. You might need to add the original project as a [remote](https://git-scm.com/docs/git-remote#Documentation/git-remote.txt-emaddem).
- Open a PR with your changes and wait for a response. You might have to make a few adjustments or rebase again before it is finally merged.
- Watch as a project collaborator merges your branch and celebrate! You have contributed to open source!
- If you have any questions along the way, you can always ask them in the original issue to ask for guidance.

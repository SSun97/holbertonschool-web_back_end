console.log('Before');

// getUser(1)
//     .then(user => getRepositories(user.gitHubUserName))
//     .then(repos => getcommits(repos[0]))
//     .then(commits => console.log('Commits', commits))
//     .catch(err => console.log('Error', err.message));

// Async and Await
async function displayCommits() {
    try {

        const user = await getUser(1);
        const repos = await getRepositories(user.gitHubUserName);
        const commits = await getcommits(repos[0]);
        console.log(commits);
    }
    catch(err) {
        console.log('Error', err.message);
    }
}

displayCommits()

function getUser(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Reading a user from a database...');
            resolve({ id: id, gitHubUserName: 'Simon' });
        }, 2000);
    });
}

function getRepositories(username) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('Getting repo for user' + username);
            // resolve(['repo1', 'repo2', 'repo3']);
            reject(new Error('Could not get the repos.'));
        }, 2000);
    });
}

function getcommits(repo) {
    return new Promise((resolve, reject) => {
        console.log('Calling GitHub API...');
        resolve(['commit']);
    })
}
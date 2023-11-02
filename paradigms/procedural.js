const form = document.getElementById('user-input');

function signupHandler(event){
    event.preventDefault();

    const usernameInput = document.getElementById('username');
    const enteredUsername = usernameInput.value;
    
    const passwordInput = document.getElementById('password');
    const enteredPassword = passwordInput.value;

    if(enteredUsername.trim().length === 0){
        alert('Invalid')
        return;
    }
    if(enteredPassword.trim().length <= 5){
        alert('Invalid')
        return;
    }

    const user = {userName: enteredUsername,
                  password: enteredPassword}

    console.log(user)
    console.log(user.userName + '! Welcome bro')


}

form.addEventListener('submit', signupHandler)
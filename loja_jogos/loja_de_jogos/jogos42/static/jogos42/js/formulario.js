document.addEventListener('DOMContentLoaded', function () {
    const emailInput = document.getElementById('id_email');
    const errorLabel = document.getElementById('email-error');

    emailInput.addEventListener('input', function () {
        const email = emailInput.value;
        if (email && !isValidEmail(email)) {
            errorLabel.textContent = 'Email inválido';
        } else {
            errorLabel.textContent = '';
        }
    });

    function isValidEmail(email) {

        return email.includes('@');
    }
});

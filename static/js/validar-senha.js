function validarSenha(senha) {
    const tem8Caracteres = senha.length >= 8;
    const maiusculas = senha.match(/[A-Z]/g) || [];
    const temNumero = /\d/.test(senha);
    const temEspecial = /[!@#$%^&*(),.?":{}|<>_\-\\[\]/]/.test(senha);

    return {
        valida:
            tem8Caracteres && maiusculas.length >= 1 && temNumero && temEspecial,
        erros: [
            !tem8Caracteres && 'Mínimo 8 caracteres. ',
            maiusculas.length < 1 && '1 letras maiúsculas',
            !temNumero && '1 número',
            !temEspecial && '1 caractere especial'
        ].filter(Boolean)
    };
}

document.addEventListener('DOMContentLoaded', () => {

    const senha = document.getElementById('senha');
    const retorno_input = document.getElementById('senha-validacao');

    if (!senha) return;

    senha.addEventListener('input', () => {

        const resultado = validarSenha(senha.value);

        if (resultado.valida) {

            retorno_input.innerHTML = '';

            senha.setCustomValidity('');

            return;
        }

        retorno_input.className = 'text-danger';
        retorno_input.innerHTML = resultado.erros.join(' ');

        senha.setCustomValidity('Senha inválida');
    });
});
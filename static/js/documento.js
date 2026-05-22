const MASK_CPF = '999.999.999-99';
const MASK_CNPJ = '99.999.999/9999-99';

function somenteNumeros(valor) {
    return valor.replace(/\D/g, '');
}

function aplicarMascaraDocumento(input) {

    if (!input) return;

    const valor = somenteNumeros(input.value);
    const mascara = valor.length <= 11 ? MASK_CPF : MASK_CNPJ;

    VMasker(input).unMask();
    VMasker(input).maskPattern(mascara);

    input.value = VMasker.toPattern(
        valor,
        mascara
    );
}

function validarDocumento(valor) {
    const documento = somenteNumeros(valor);

    if (documento.length === 11) {
        return validarCPF(documento);
    }

    if (documento.length === 14) {
        return validarCNPJ(documento);
    }

    return false;
}

function validarCPF(cpf) {
    if (/^(\d)\1{10}$/.test(cpf)) {
        return false;
    }

    let soma = 0;

    for (let i = 0; i < 9; i++) {
        soma += Number(cpf[i]) * (10 - i);
    }

    let digito = 11 - (soma % 11);
    digito = digito >= 10 ? 0 : digito;

    if (digito !== Number(cpf[9])) {
        return false;
    }

    soma = 0;

    for (let i = 0; i < 10; i++) {
        soma += Number(cpf[i]) * (11 - i);
    }

    digito = 11 - (soma % 11);
    digito = digito >= 10 ? 0 : digito;

    return digito === Number(cpf[10]);
}

function validarCNPJ(cnpj) {
    if (/^(\d)\1{13}$/.test(cnpj)) { return false; }

    function calcularDigito(base, pesos) {
        const soma = base.split('').reduce((total, numero, i) => { return total + Number(numero) * pesos[i]; }, 0);
        const resto = soma % 11;

        return resto < 2 ? 0 : 11 - resto;
    }

    const base = cnpj.slice(0, 12);
    const pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
    const pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];

    const digito1 = calcularDigito(base, pesos1);
    const digito2 = calcularDigito(base + digito1, pesos2);

    return cnpj === base + digito1 + digito2;
}
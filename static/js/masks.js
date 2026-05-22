function aplicarMascaras(campos) {

    if (campos.telefone) {

        aplicarMascaraTelefone(campos.telefone);

        campos.telefone.addEventListener('input', () => { aplicarMascaraTelefone(campos.telefone); });
    }

    if (campos.dataNascimento) {
        VMasker(campos.dataNascimento).maskPattern('99/99/9999');
    }

    if (campos.cep) {
        VMasker(campos.cep).maskPattern('99999-999');
    }
}

function aplicarMascaraTelefone(input) {
    if (!input) return;

    const valor = input.value.replace(/\D/g, '');
    const mascara = valor.length <= 10 ? '(99) 9999-9999' : '(99) 99999-9999';

    VMasker(input).unMask();
    VMasker(input).maskPattern(mascara);

    input.value = VMasker.toPattern(valor, mascara);
}
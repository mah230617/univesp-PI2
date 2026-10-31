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


    let valor = input.value.replace(/\D/g, "");


    if (valor.length > 11) {
        valor = valor.substring(0, 11);
    }


    if (valor.length <= 10) {

        input.value = valor.replace(
            /^(\d{2})(\d{4})(\d{0,4})$/,
            "($1) $2-$3"
        );


    } else {

        input.value = valor.replace(
            /^(\d{2})(\d{5})(\d{0,4})$/,
            "($1) $2-$3"
        );

    }

}
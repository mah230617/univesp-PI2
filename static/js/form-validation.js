document.addEventListener('DOMContentLoaded', () => {

    const campos = {
        documento:
            document.getElementById('cpfcnpj'),
        telefone:
            document.getElementById('telefone'),
        dataNascimento:
            document.getElementById('data_nascimento'),
        cep:
            document.getElementById('cep'),
        logradouro:
            document.getElementById('logradouro'),
        bairro:
            document.getElementById('bairro'),
        cidade:
            document.getElementById('cidade'),
        complemento:
            document.getElementById('complemento'),
        estado:
            document.getElementById('estado'),
        numero:
            document.getElementById('numero'),
        form:
            document.getElementById('form-dados')
    };

    if (campos.documento) {

        // máscara CPF/CNPJ inicial
        aplicarMascaraDocumento(campos.documento);

        campos.documento.addEventListener('input', () => { aplicarMascaraDocumento(campos.documento); });
        campos.documento.addEventListener('blur', () => { document.getElementById('cpfcnpj-retorno').innerText = !validarDocumento(campos.documento.value) ? 'CPF / CNPJ inválido!' : ''; });
    }

    // Máscara de Telefone, CEP e Data Nascimento
    aplicarMascaras(campos);

    // CEP
    if (campos.cep)
        campos.cep.addEventListener('blur', () => buscarCEP(campos));

    // validação submit
    if (campos.form) {
        campos.form.addEventListener('submit', (event) => {

            const valido = validarDocumento(campos.documento.value);

            if (!valido) {

                document.getElementById('cpfcnpj-retorno').innerText = 'CPF / CNPJ inválido!';

                campos.documento.focus();

                event.preventDefault();

                if (typeof esconderLoading === 'function') {
                    esconderLoading();
                }

                return;
            }

            if (typeof mostrarLoading === 'function') {
                mostrarLoading();
            }
        });
    }
});
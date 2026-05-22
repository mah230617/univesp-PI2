async function buscarCEP(campos) {
    const cep = campos.cep.value.replace(/\D/g, '');

    if (cep.length !== 8) { return; }

    try {
        mostrarLoading();

        const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);

        const data = await response.json();

        if (data.erro) { return; }

        campos.logradouro.value = data.logradouro || '';
        campos.bairro.value = data.bairro || '';
        campos.cidade.value = data.localidade || '';
        campos.complemento.value = '';
        campos.estado.value = data.uf || '';
        campos.numero.focus();

    } catch (erro) {
        console.error('Erro ao buscar CEP:', erro);
    } finally {
        esconderLoading();
    }
}
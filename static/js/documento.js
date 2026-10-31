const MASK_CPF = '999.999.999-99';
const MASK_CNPJ = '99.999.999/9999-99';


function somenteNumeros(valor) {
    return valor.replace(/\D/g, '');
}


function aplicarMascaraDocumento(input) {

    if (!input) return;


    let valor = somenteNumeros(input.value);


    // limita para CPF ou CNPJ
    if (valor.length > 14) {
        valor = valor.substring(0,14);
    }


    input.value = valor;


    if (valor.length <= 11) {

        VMasker(input).unMask();

        VMasker(input).maskPattern(
            MASK_CPF
        );

    } else {

        VMasker(input).unMask();

        VMasker(input).maskPattern(
            MASK_CNPJ
        );
    }


    // reaplica o valor depois da máscara
    input.value = formatarDocumento(valor);
}



function formatarDocumento(valor){

    if(valor.length <= 11){

        return valor
        .replace(/^(\d{3})(\d)/,'$1.$2')
        .replace(/^(\d{3})\.(\d{3})(\d)/,'$1.$2.$3')
        .replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d)/,'$1.$2.$3-$4');

    }


    return valor
    .replace(/^(\d{2})(\d)/,'$1.$2')
    .replace(/^(\d{2})\.(\d{3})(\d)/,'$1.$2.$3')
    .replace(/^(\d{2})\.(\d{3})\.(\d{3})(\d)/,'$1.$2.$3/$4')
    .replace(/^(\d{2})\.(\d{3})\.(\d{3})\/(\d{4})(\d)/,'$1.$2.$3/$4-$5');

}



function validarDocumento(valor){

    const documento = somenteNumeros(valor);


    if(documento.length === 11){
        return validarCPF(documento);
    }


    if(documento.length === 14){
        return validarCNPJ(documento);
    }


    return false;
}



function validarCPF(cpf){

    if(/^(\d)\1{10}$/.test(cpf)){
        return false;
    }


    let soma = 0;


    for(let i=0;i<9;i++){

        soma += Number(cpf[i])*(10-i);

    }


    let digito = 11-(soma%11);

    digito = digito >=10 ? 0 : digito;


    if(digito !== Number(cpf[9])){
        return false;
    }


    soma=0;


    for(let i=0;i<10;i++){

        soma += Number(cpf[i])*(11-i);

    }


    digito = 11-(soma%11);

    digito = digito>=10 ? 0 : digito;


    return digito === Number(cpf[10]);

}




function validarCNPJ(cnpj){

    if(/^(\d)\1{13}$/.test(cnpj)){
        return false;
    }


    let tamanho = cnpj.length-2;
    let numeros = cnpj.substring(0,tamanho);
    let digitos = cnpj.substring(tamanho);


    let soma=0;
    let pos=tamanho-7;


    for(let i=tamanho;i>=1;i--){

        soma += numeros.charAt(tamanho-i)*pos--;

        if(pos<2){
            pos=9;
        }
    }


    let resultado = soma%11<2 ? 0 : 11-(soma%11);


    if(resultado != digitos.charAt(0)){
        return false;
    }


    tamanho++;
    numeros = cnpj.substring(0,tamanho);


    soma=0;
    pos=tamanho-7;


    for(let i=tamanho;i>=1;i--){

        soma += numeros.charAt(tamanho-i)*pos--;

        if(pos<2){
            pos=9;
        }
    }


    resultado = soma%11<2 ? 0 : 11-(soma%11);


    return resultado == digitos.charAt(1);

}
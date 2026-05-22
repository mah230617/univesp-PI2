document.addEventListener('DOMContentLoaded', () => {

    const campo = document.getElementById('data_nascimento');

    if (!campo) return;

    flatpickr(campo, {
        locale: 'pt',
        dateFormat: 'd/m/Y',
        allowInput: true,
        disableMobile: true
    });
});
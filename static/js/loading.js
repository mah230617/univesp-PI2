function mostrarLoading() {
    document.getElementById('loading-overlay')?.classList.remove('d-none');
}

function esconderLoading() {
    document.getElementById('loading-overlay')?.classList.add('d-none');
}

document.addEventListener('DOMContentLoaded', esconderLoading);
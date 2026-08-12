function mostrarLoading() {
    document.getElementById('loading-overlay')?.classList.remove('d-none');
}

function esconderLoading() {
    document.getElementById('loading-overlay')?.classList.add('d-none');
}

document.addEventListener('DOMContentLoaded', esconderLoading);

document.addEventListener("DOMContentLoaded", () => {
    esconderLoading();

    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", (e) => {
            setTimeout(() => {
                if (!e.defaultPrevented) {
                    mostrarLoading();
                } else {
                    esconderLoading();
                }
            }, 0);
        });
    });
});
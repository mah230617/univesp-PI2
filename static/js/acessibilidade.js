// Controle de Acessibilidade (Fonte, Contraste e VLibras)
document.addEventListener('DOMContentLoaded', function () {
    const fontSizes = ['', 'font-sm', 'font-lg', 'font-xl'];
    let currentFontIndex = 0;

    // Carregar preferências salvas no localStorage
    if (localStorage.getItem('highContrast') === 'true') {
        document.body.classList.add('high-contrast');
        const btnContrast = document.getElementById('btn-contrast');
        if (btnContrast) btnContrast.setAttribute('aria-pressed', 'true');
    }

    const savedFont = localStorage.getItem('fontClass');
    if (savedFont && fontSizes.includes(savedFont)) {
        document.body.classList.add(savedFont);
        currentFontIndex = fontSizes.indexOf(savedFont);
    }

    // Botão de Alto Contraste
    const btnContrast = document.getElementById('btn-contrast');
    if (btnContrast) {
        btnContrast.addEventListener('click', function () {
            const isHighContrast = document.body.classList.toggle('high-contrast');
            btnContrast.setAttribute('aria-pressed', isHighContrast ? 'true' : 'false');
            localStorage.setItem('highContrast', isHighContrast);
        });
    }

    // Aumentar Fonte
    const btnIncreaseFont = document.getElementById('btn-font-increase');
    if (btnIncreaseFont) {
        btnIncreaseFont.addEventListener('click', function () {
            fontSizes.forEach(cls => cls && document.body.classList.remove(cls));
            if (currentFontIndex < fontSizes.length - 1) {
                currentFontIndex++;
            }
            if (fontSizes[currentFontIndex]) {
                document.body.classList.add(fontSizes[currentFontIndex]);
            }
            localStorage.setItem('fontClass', fontSizes[currentFontIndex]);
        });
    }

    // Diminuir Fonte
    const btnDecreaseFont = document.getElementById('btn-font-decrease');
    if (btnDecreaseFont) {
        btnDecreaseFont.addEventListener('click', function () {
            fontSizes.forEach(cls => cls && document.body.classList.remove(cls));
            if (currentFontIndex > 0) {
                currentFontIndex--;
            }
            if (fontSizes[currentFontIndex]) {
                document.body.classList.add(fontSizes[currentFontIndex]);
            }
            localStorage.setItem('fontClass', fontSizes[currentFontIndex]);
        });
    }

    // Resetar Fonte
    const btnResetFont = document.getElementById('btn-font-reset');
    if (btnResetFont) {
        btnResetFont.addEventListener('click', function () {
            fontSizes.forEach(cls => cls && document.body.classList.remove(cls));
            currentFontIndex = 0;
            localStorage.removeItem('fontClass');
        });
    }
});

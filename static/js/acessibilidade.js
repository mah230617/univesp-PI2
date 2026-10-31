// Controle de Acessibilidade (Fonte, Contraste e VLibras)
document.addEventListener('DOMContentLoaded', function () {
    const fontSizes = ['font-sm', '', 'font-lg', 'font-xl'];
    let currentFontIndex = fontSizes.indexOf(''); // Índice 1 (normal)

    function applyFontClass(newClass) {
        fontSizes.forEach(cls => {
            if (cls) {
                document.documentElement.classList.remove(cls);
                document.body.classList.remove(cls);
            }
        });
        if (newClass) {
            document.documentElement.classList.add(newClass);
            document.body.classList.add(newClass);
        }
    }

    // Carregar preferências salvas no localStorage
    if (localStorage.getItem('highContrast') === 'true') {
        document.body.classList.add('high-contrast');
        const btnContrast = document.getElementById('btn-contrast');
        if (btnContrast) btnContrast.setAttribute('aria-pressed', 'true');
    }

    const savedFont = localStorage.getItem('fontClass');
    if (savedFont && fontSizes.includes(savedFont)) {
        currentFontIndex = fontSizes.indexOf(savedFont);
        applyFontClass(savedFont);
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

    // Aumentar Fonte (A+)
    const btnIncreaseFont = document.getElementById('btn-font-increase');
    if (btnIncreaseFont) {
        btnIncreaseFont.addEventListener('click', function () {
            if (currentFontIndex < fontSizes.length - 1) {
                currentFontIndex++;
                const newClass = fontSizes[currentFontIndex];
                applyFontClass(newClass);
                if (newClass) {
                    localStorage.setItem('fontClass', newClass);
                } else {
                    localStorage.removeItem('fontClass');
                }
            }
        });
    }

    // Diminuir Fonte (A-)
    const btnDecreaseFont = document.getElementById('btn-font-decrease');
    if (btnDecreaseFont) {
        btnDecreaseFont.addEventListener('click', function () {
            if (currentFontIndex > 0) {
                currentFontIndex--;
                const newClass = fontSizes[currentFontIndex];
                applyFontClass(newClass);
                if (newClass) {
                    localStorage.setItem('fontClass', newClass);
                } else {
                    localStorage.removeItem('fontClass');
                }
            }
        });
    }

    // Resetar Fonte (A)
    const btnResetFont = document.getElementById('btn-font-reset');
    if (btnResetFont) {
        btnResetFont.addEventListener('click', function () {
            currentFontIndex = fontSizes.indexOf('');
            applyFontClass('');
            localStorage.removeItem('fontClass');
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const inputImagem = document.getElementById('id_imagem_maquina');
    const preview = document.getElementById('preview');

    if (inputImagem) {
        inputImagem.addEventListener('change', function() {
            const arquivo = this.files[0];

            if (arquivo) {
                const leitor = new FileReader();

                leitor.onload = function(e) {
                    preview.src = e.target.result; // Troca o placeholder pela foto real
                    preview.style.opacity = "1";   // Remove a transparência se tiver usado
                }

                leitor.readAsDataURL(arquivo);
            }
        });
    }
});
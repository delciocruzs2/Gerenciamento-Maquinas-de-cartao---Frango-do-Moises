function confirmarExclusao(url, valor) {
    if (confirm("Deseja realmente excluir o lançamento de R$ " + valor + "?")) {
        window.location.href = url;
    }
}
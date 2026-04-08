function confirmar_exclusao(id, nome) {
    if (confirm("Tem certeza que deseja excluir a máquina '" + nome + "'?")) {
        window.location.href = "/v1/maquinas/deletar_maquina/" + id + "/";
    }
}
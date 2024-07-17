document.addEventListener('DOMContentLoaded', function() {
    const mensajeExitoso = document.getElementById('exito');
    const mensajeError = document.getElementById('error');

    if (mensajeExitoso) {
        alert(mensajeExitoso.textContent);
    }

    if (mensajeError) {
        alert(mensajeError.textContent);
    }
});




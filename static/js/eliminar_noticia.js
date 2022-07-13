const btnsEliminacion = document.querySelectorAll('.btnEliminacion');

funtion (); {
    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click', function(e) {
            let confirmacion = confirm("¿Desea eliminar esta noticia?");
            if (!confirmacion) {
                e.preventDefault();
            }
        })
    });
};

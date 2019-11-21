

function confirmarEliminacion(id) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "¡Este cambio borrará el dato permanentemente!",
        icon: 'Advertencia',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, borrar',
        cancelButtonText:  'Cancelar'
      }).then((result) => {
        if (result.value) {
          // redirigir usuario a la ruta eliminar

          window.location.href= "/eliminar/" + id +"/";
        }
      })
}
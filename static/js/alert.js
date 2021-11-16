function conDel(id) {
  Swal.fire({
  title: 'Deseas eliminar el objeto con el id: '+id_alumnos+' de la lista',
  text: "Esta accion no se puede deshacer",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Si, si quiero eliminar'
}).then((result) => {
  if (result.value) {
    Swal.fire(
      'ELIMINADO',
      'Su archivo a sido eliminado',
      'success',
      window.setTimeout(window.location.href="eliminar/"+id_alumnos+"/", 50000)
    )
  }
})
}

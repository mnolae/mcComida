function urlModal(url, titulo){
    $('#ModalLabel').html(titulo);
    $('#ModalHeader').removeClass('bg-danger');
    $('#btnAceptar').removeClass('d-none');
    $('#btnCancelar').text('Cancelar');

    if (titulo.indexOf("Eliminar") == 0){
        $('#ModalLabel').html('<i class="fa fa-warning"></i> ' + titulo);
        $('#ModalHeader').addClass('bg-danger');
        $('#modalContenido').html('Se eliminará el elemento seleccionado de la base de datos.');
        $('#btnAceptar').attr('onclick', "window.location = '" + url + "'");

    } else if (titulo.indexOf("Editar") == 0 || titulo.indexOf("Nuevo") == 0){ 
        $.ajax({
            url: url, 
            success: function(result){
                $('#modalContenido').html(result);
                $('#formGenerico').attr('action', url);
                $('#btnAceptar').attr('onclick', "$('#btnSubmit').click()");
            }});

    } else {
        console.log('llega')
        $.ajax({
            url: url, 
            success: function(result){
                $('#modalContenido').html(result);
                $('#btnAceptar').addClass('d-none');
                $('#btnCancelar').text('Aceptar');
            }});
    }

}

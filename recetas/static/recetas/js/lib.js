function urlModal(url, titulo){
    $('#ModalLabel').html(titulo);
    $('#ModalHeader').removeClass('bg-danger');
//    $('#btnAceptar').addClass('btn-success');
//    $('#btnAceptar').removeClass('btn-danger');

    if (titulo.indexOf("Eliminar") == 0){
        $('#ModalLabel').html('<i class="fa fa-warning"></i> ' + titulo);
        $('#ModalHeader').addClass('bg-danger');
//        $('#btnAceptar').toggleClass('btn-success');
//        $('#btnAceptar').toggleClass('btn-danger');
        $('#modalContenido').html('Se eliminará el elemento seleccionado de la base de datos.');
        $('#btnAceptar').attr('onclick', "window.location = '" + url + "'");
    } else {
        $.ajax({
            url: url, 
            success: function(result){
                $('#modalContenido').html(result);
                $('#formGenerico').attr('action', url);
                $('#btnAceptar').attr('onclick', "$('#btnSubmit').click()");
            }});
    }

}

//Funcion para buscar en un dropdownlist de acuerdo al texto escrito en el textbox
//busca el elemnto del dropdown que inicie con el texto del textbox/inputtext
function buscar_dropdown_startswith(txtBox,cboBox,html_inicial){
  $( txtBox ).keyup(function(e){
    var nit = $(txtBox).val();
    if(e.keyCode=='8') //Si se borra algo, regresa el select al valor original (se hace esto porque se trababa antes)
    {
      $(cboBox).html(html_inicial);
    }
    if(nit==='')
    {
    }
    else {
      $(cboBox).html(html_inicial);
      $(cboBox+" option:starts-with("+nit+")").attr('selected', true);
      if($(cboBox+" option:starts-with("+nit+")").length==0){ //si el texto no coincide, se resetea el select
        $(cboBox).html(html_inicial);
      }
    }
  });
}


//Funcion para buscar en un dropdownlist de acuerdo al texto escrito en el textbox
//dependiendo del estado del checkbox enviado, puede buscar lo siguiente:
//(checked=False)busca el elemento del dropdown que inicie con el texto del textbox/inputtext
//(checked=True)busca el elemento del dropdown que contenga el texto del textbox/inputtext
//por último se envía el estado inicial de ese Combobox para que pueda ser restaurado
function buscar_dropdown_startswith_condicional(txtBox,cboBox,chkBox,html_inicial){
  $( txtBox ).keyup(function(e){
    var nit = $(txtBox).val();
    if(e.keyCode=='8') //Si se borra algo, regresa el select al valor original (se hace esto porque se trababa antes)
    {
      $(cboBox).html(html_inicial);
    }
    if(nit==='')
    {
    }
    else {
      if($(chkBox).is(':checked')) {
        $(cboBox).html(html_inicial);
        $(cboBox+" option:contains("+nit+")").attr('selected', true);
        if($(cboBox+" option:contains("+nit+")").length==0){ //si el texto no coincide, se resetea el select
          $(cboBox).html(html_inicial);
        }
      }
      else {
        $(cboBox).html(html_inicial);
        $(cboBox+" option:starts-with("+nit+")").attr('selected', true);
        if($(cboBox+" option:starts-with("+nit+")").length==0){ //si el texto no coincide, se resetea el select
          $(cboBox).html(html_inicial);
        }
      }
      /*
      $(cboBox).html(selectClienteDefault);
      $(cboBox+" > option").filter(function () {
          var texto=cboBox.text.split(parametrosplit);
          console.log(texto);
          var buscaresto=texto[indicesplit];
          console.log(buscaresto);
          var posicion=cboBox.text().indexof(buscaresto);
          console.log(posicion);
          return this.value.substring(posicion,cboBox.text().length) === buscaresto;
      }).attr('selected', true);*/
      //$(cboBox+" option:starts-with("+nit+")").attr('selected', true);
      //if($(cboBox+" option:starts-with("+nit+")").length==0){ //si el texto no coincide, se resetea el select
      //  $(cboBox).html(selectClienteDefault);
      //}
    }
  });
}


//Funcion que muestra lo que se le envie como segundo parametro
//al dar clic al checkbox del primer parametro. Tambien lo puede ocultar
//de acuerdo al estado del checkbox.
//El primer parmetro se envia sin el #
function click_ocultar_mostrar(activador,seoculta){
  $( '#'+activador ).on({
      //mouseenter: function() {
      //    console.log( "hovered over a div" );
      //},
      //mouseleave: function() {
      //    console.log( "mouse left a div" );
      //},
      click: function() {
        if(document.getElementById(activador).checked) {
          $(seoculta).show();
        }
        else {
          $(seoculta).hide();
        }
      }
  });
}


//Función que comprueba si el dropdown tiene un elemento seleccionado y pasa al txtbox de destino,
//de lo contrario muestra una alerta y devuelve el dropdown a su estado original.
//(txtboxInicial,txtboxDestino,dropDownBusqueda,mensaje)
function comprobar_pasarsiguiente_mostrarmensaje(txtboxInicial,txtboxDestino,dropDownBusqueda,mensaje)
{
  $( txtboxInicial ).keydown(function(e){ //Keydown es para que al presionarse la tecla haga algo.
                                                      //El parámetro "e" captura la tecla del teclado
    var keyCode = e.keyCode || e.which; //se declara una variable que capturará cualquiera de esos dos valores
    if (keyCode==13) { //keycode obtiene el valor ascii de la tecla presionada
     e.preventDefault(); //previene que se realice la acción por defecto que efectuaría el navegador con esa tecla
      var valor=$(dropDownBusqueda+" option:selected").val();
      if(valor==='')
      {
        $(dropDownBusqueda).html(selectClienteDefault);
        alert(mensaje);
      }
      else {
        $(txtboxDestino).focus();
      }
    }
  });
}

//Funcion para sumar la columna de una tabla
//se le envia como primer parametro, el selector de la clase aplicada a la columna de la tabla_productos
//luego como segundo, el nombre del 'number input' donde se escribira el resultado
/*
function sumar_valor_parcial(clase, escribiraqui)
{
  var sum=0;
  $(clase).each(function() {
      sum += parseFloat($(this).text());
  });
  $(escribiraqui).val(sum);
}
*/

//La siguiente funcion envia los datos del arreglo_parametros, que son objetos del DOM
//hacia un View vinculado a la URL. El arreglo de parametros debe ser creado con los
//id's de los elementos del DOM, en forma de string
//se llama asi:
//var parametros=['#id_codigoestilo_producto','#id_bodega_idbodega','#id_marca_id_marca','#id_tipo_producto_idtipo_producto','#id_talla_idtalla','#id_estilo_idestilo','#id_color_idcolor','#id_genero_idgener'];
//aun no funciona
//var json_recibido = obtener_con_ajax(parametros,"/Buscar/ProductoCaracteristicas/");
/*
function obtener_con_ajax(arreglo_parametros,URL_del_view) {
    var contenido_a_enviar={};
    $.each( arreglo_parametros, function( index, value ){
      var datos=$(value).attr('id') +':'+$(value).val()+',';
      contenido_a_enviar[$(value).attr('id')] = $(value).val();
    });

    console.log(JSON.stringify(contenido_a_enviar));
    $.ajax({
        url : URL_del_view, // La URL que llama a la vista
        type : "POST", // Metodo http para realizar el request (peticion al servidor)
        data : contenido_a_enviar, // Datos enviados con el request en formato JSON
        success : function(json) {
          console.log("xxxxxxxxxxxxxxx");
          console.log(json.consulta);
          return json;
        },
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! Ha ocurrido un error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
            console.log(xhr.status + ": " + xhr.responseText); // Se envia el codigo del status y el texto que ha devuelto el response
        }
    });
};
*/
/*
function lista_desplegable(select_enviado){
  document.getElementById(select_enviado).addEventListener('click', onClickHandler);
  document.getElementById(select_enviado).addEventListener('mousedown', onMouseDownHandler);

  function onMouseDownHandler(e){
  	var el = e.currentTarget;

      if(el.hasAttribute('size') && el.getAttribute('size') == '1'){
      	e.preventDefault();
      }
  }
  function onClickHandler(e) {
   	var el = e.currentTarget;

      if (el.getAttribute('size') == '1') {
          el.className += " selectOpen";
          el.setAttribute('size', '3');
      }
      else {
          el.className = '';
          el.setAttribute('size', '1');
      }
  }
}
*/

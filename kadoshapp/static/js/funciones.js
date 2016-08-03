//Funcion para buscar en un dropdownlist de acuerdo al texto escrito en el textbox
//busca el elemnto del dropdown que inicie con el texto del textbox/inputtext
function buscar_dropdown_startswith(txtBox,cboBox){
  $( txtBox ).keyup(function(e){
    var nit = $(txtBox).val();
    if(e.keyCode=='8') //Si se borra algo, regresa el select al valor original (se hace esto porque se trababa antes)
    {
      $(cboBox).html(selectDefault);
    }
    if(nit==='')
    {
    }
    else {
      $(cboBox).html(selectDefault);
      $(cboBox+" option:starts-with("+nit+")").attr('selected', true);
      if($(cboBox+" option:starts-with("+nit+")").length==0){ //si el texto no coincide, se resetea el select
        $(cboBox).html(selectDefault);
      }
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

//Función que cmprueba si el texto del textbox es igual al del dropdown
//si es asi pasa el cursor a otro textbox, de lo contrario muestra una alerta
//y devuelve el dropdown a su estado original. Se le envia ademas el parametro para que se haga un split
//del texto del elemento seleccionado en el dropdwon. Y otro parametro para saber que posicion del arreglo
//resultante del split, es la que se usara para la comparacion
function comprobar_pasarsiguiente_mostrarmensaje(txtboxInicial,txtboxDestino,dropDownBusqueda,mensaje,parametrosplit,posicionarreglosplit)
{
  $( txtboxInicial ).keydown(function(e){ //Keydown es para que al presionarse la tecla haga algo.
                                                      //El parámetro "e" captura la tecla del teclado
    var keyCode = e.keyCode || e.which; //se declara una variable que capturará cualquiera de esos dos valores
    if (e.keyCode==13) { //keycode obtiene el valor ascii de la tecla presionada
      e.preventDefault(); //previene que se realice la acción por defecto que efectuaría el navegador con esa tecla
      var text=$(dropDownBusqueda+" option:selected").text().split(parametrosplit);
      var nit = $(txtboxInicial).val();
      if(text[posicionarreglosplit]===nit)
      {
        $(txtboxDestino).focus();
      }
      else {
        //$('input#id_nit_del_cliente').val('');
        //$(txtboxDestino).focus();
        $(dropDownBusqueda).html(selectDefault);
        alert(mensaje);
      }
    }
    //$('input#id_nit_del_cliente').focus();
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

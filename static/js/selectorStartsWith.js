//Función que crea un selector starts-with
$.extend($.expr[":"], {
  "starts-with": function(elem, i, data, set) {
    var text = $.trim($(elem).text()),
    term = data[3];
    // first index is 0
    return text.indexOf(term) === 0;
    },
  "ends-with": function(elem, i, data, set) {
    var text = $.trim($(elem).text()),
    term = data[3];
    // last index is last possible
    return text.lastIndexOf(term) === text.length - term.length;
    }
});

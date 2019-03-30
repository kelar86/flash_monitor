(function ($) {
    $(function () {
        var category = $('#id_category');
        var controls = $('.form-row.field-control');

        function toggleControl(value) {
            value == 'CONTROL_ALERT' ? controls.show() : controls.hide();
        } 
        
        category.change(function () { toggleControl($(this).val()); });
    });

})(django.jQuery); 